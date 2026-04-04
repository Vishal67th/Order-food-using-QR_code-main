from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib import messages
from cafe.models import *
from django.core.files.storage import FileSystemStorage
from datetime import date, datetime, timedelta
import json, ast
from itertools import groupby
from django.db.models import Sum
import qrcode
from django.http import HttpResponse
from io import BytesIO
from django.core.files.base import ContentFile

User = get_user_model()
from django.contrib.auth import update_session_auth_hash

def edit_profile(request):
    if request.user.is_anonymous:
        messages.error(request, 'Please Login first!')
        return redirect('login')

    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name  = request.POST.get('last_name', '')
        user.email      = request.POST.get('email', '')

        phone = request.POST.get('phone', '').strip()
        if phone:
            user.phone = phone

        pw1 = request.POST.get('password1', '').strip()
        pw2 = request.POST.get('password2', '').strip()
        if pw1 and pw2:
            if pw1 == pw2:
                user.set_password(pw1)
                update_session_auth_hash(request, user)
            else:
                messages.error(request, 'Passwords do not match!')
                return redirect('edit_profile')

        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    return render(request, 'edit_profile.html')


def home(request):
    total_orders = order.objects.count()
    total_customers = User.objects.filter(cafe_manager=False).count()
    total_revenue = sum([int(o.price) for o in order.objects.all()])
    context = {
        'total_orders': total_orders,
        'total_customers': total_customers,
        'total_revenue': total_revenue,
    }
    return render(request, 'home.html', context)


def menu(request):
    menu_items = menu_item.objects.all().order_by('list_order')

    # ✅ FIX: Normalize category to lowercase to prevent duplicate groups
    # e.g. 'Bread' and 'bread' will now be treated as the same category
    items_by_category = {}
    for item in menu_items:
        key = item.category.lower().strip()  # normalize here
        if key not in items_by_category:
            items_by_category[key] = []
        items_by_category[key].append(item)

    context = {'items_by_category': items_by_category}
    return render(request, 'menu.html', context)


def parse_items_json(items_json_str):
    """
    ✅ Helper: Parses items_json string into a clean dict.
    Supports both list format [qty, name, price] and dict format {quantity, name, price}.
    Returns {} on failure.
    """
    if not items_json_str or not items_json_str.strip():
        return {}
    try:
        parsed = json.loads(items_json_str)
        if not isinstance(parsed, dict):
            return {}

        cleaned = {}
        for key, value in parsed.items():
            try:
                if isinstance(value, dict):
                    qty   = value.get('quantity', 0)
                    name  = value.get('name', '')
                    price = value.get('price', 0)
                    if qty and name:
                        cleaned[key] = [qty, name, price]

                elif isinstance(value, (list, tuple)) and len(value) >= 3:
                    qty, name, price = value[0], value[1], value[2]
                    if qty and name:
                        cleaned[key] = [qty, name, price]

            except (IndexError, TypeError, KeyError):
                pass

        return cleaned

    except (json.JSONDecodeError, ValueError):
        return {}


def all_orders(request):
    # ✅ FIX 1: Fetch all orders sorted by table first, then by time.
    # groupby() only groups CONSECUTIVE identical keys — so we must sort by table.
    orders = order.objects.all().order_by('table', '-order_time')

    # ✅ FIX 2: Use a plain dict instead of groupby to avoid missing orders.
    order_by_table = {}
    for ord in orders:
        table_key = ord.table
        if table_key not in order_by_table:
            order_by_table[table_key] = []

        # ✅ FIX 3: Parse items_json using the shared helper
        ord.items_json = parse_items_json(ord.items_json)
        order_by_table[table_key].append(ord)

    context = {'order_by_table': order_by_table}
    return render(request, 'all_orders.html', context)


def offers(request):
    return render(request, 'offers.html')


def reviews(request):
    if request.method == 'POST':
        fname = request.user.first_name
        lname = request.user.last_name
        cmt = request.POST.get('comment')
        date_today = date.today()
        review = rating(name=fname + ' ' + lname, comment=cmt, r_date=date_today)
        review.save()

    all_reviews = rating.objects.all().order_by('-r_date')
    context = {'reviews': all_reviews}
    return render(request, 'reviews.html', context)


def profile(request):
    if request.user.is_anonymous:
        messages.error(request, 'Please Login first!!')
        return redirect('login')
    return render(request, 'profile.html')


def manage_menu(request):
    if request.method == 'POST' and request.FILES['img']:
        if request.user.is_anonymous:
            messages.error(request, 'Please Login to continue!')
            return redirect('login')
        if not ((request.user.is_superuser) or (request.user.cafe_manager)):
            messages.error(request, 'Only Staff members are allowed!')
            return redirect('menu')
        else:
            name = request.POST.get('name')
            price = request.POST.get('price')
            desc = request.POST.get('desc')
            cat = request.POST.get('cat')
            img = request.FILES['img']

            # ✅ FIX: Always normalize category to lowercase before saving
            cat_lower = cat.lower().strip()

            if cat_lower == 'papad':       listing_order = 1
            elif cat_lower == 'starter':   listing_order = 2
            elif cat_lower == 'bread':     listing_order = 4
            elif cat_lower == 'gravy':     listing_order = 3
            elif cat_lower == 'dal':       listing_order = 5
            elif cat_lower == 'rice':      listing_order = 6
            elif cat_lower == 'dessert':   listing_order = 7
            elif cat_lower == 'beverage':  listing_order = 8
            else:                          listing_order = 9

            # ✅ FIX: Save category as lowercase (cat_lower) so it's consistent
            dish = menu_item(name=name, price=price, desc=desc,
                             category=cat_lower, pic=img, list_order=listing_order)
            dish.save()
            messages.success(request, 'Dish added successfully!')
            return redirect('menu')

    return render(request, 'manage_menu.html')


def delete_dish(request, item_id):
    dish = get_object_or_404(menu_item, id=item_id)
    if request.user.is_superuser:
        if request.method == 'POST':
            dish.delete()
            messages.success(request, 'Dish removed successfully!')
            return redirect('menu')
    else:
        messages.error(request, 'Only admins are allowed!')
        return redirect('menu')


def cart(request):
    if request.method == 'GET':
        return render(request, 'cart.html')

    if request.method == 'POST':
        try:
            if request.user.is_anonymous:
                name = 'Unknown'
                phone = 'Unknown'
            else:
                name = request.user.first_name + ' ' + request.user.last_name
                phone = request.user.phone

            items_json = request.POST.get('items_json', '{}')
            table_number = request.POST.get('table_value', 'null')
            total = request.POST.get('price', '0')

            if not items_json or items_json == '{}' or items_json == 'null':
                messages.error(request, 'Your cart is empty! Please add items before placing order.')
                return redirect('cart')

            try:
                if isinstance(items_json, str):
                    items_data = json.loads(items_json)
                else:
                    items_data = items_json

                if not items_data:
                    messages.error(request, 'Your cart is empty! Please add items before placing order.')
                    return redirect('cart')

                items_json = json.dumps(items_data)
            except (json.JSONDecodeError, ValueError) as e:
                print(f"JSON parsing error: {e}")
                messages.error(request, 'Invalid cart data. Please try again.')
                return redirect('cart')

            now = datetime.now()
            now_ist = now + timedelta(hours=5, minutes=30)

            if table_number == 'null' or table_number is None or table_number == '':
                table_number = 'Take Away'

            try:
                new_order = order(
                    name=name,
                    phone=phone,
                    items_json=items_json,
                    table=table_number,
                    order_time=now_ist,
                    price=total
                )
                new_order.save()
                print(f"✅ Order #{new_order.order_id} saved successfully!")

            except Exception as e:
                print(f"❌ Error saving order to database: {e}")
                messages.error(request, f'Error saving order: {str(e)}')
                return redirect('cart')

            if not request.user.is_anonymous:
                try:
                    usr = User.objects.get(phone=phone)
                    usr.order_count += 1
                    usr.save()
                except User.DoesNotExist:
                    print(f"⚠️ User with phone {phone} not found")

            messages.success(request, '✅ Order Placed Successfully! Thanks for ordering')
            return redirect('my_orders')

        except Exception as e:
            print(f"❌ Unexpected error placing order: {e}")
            messages.error(request, f'Error placing order: {str(e)}. Please try again.')
            return redirect('cart')


def my_orders(request):
    if request.user.is_anonymous:
        phone = request.GET.get('phone', 'Unknown')
    else:
        phone = request.user.phone

    # ✅ Sort by table first so groupby works correctly
    orders_list = order.objects.filter(phone=phone).order_by('table', '-order_time')

    # ✅ Use plain dict instead of groupby to avoid missing orders
    order_by_table = {}
    for ord in orders_list:
        table_key = ord.table
        if table_key not in order_by_table:
            order_by_table[table_key] = []

        # ✅ Use shared parse helper
        ord.items_json = parse_items_json(ord.items_json)
        order_by_table[table_key].append(ord)

    context = {
        'order_by_table': order_by_table,
        'total_orders': sum(len(orders) for orders in order_by_table.values())
    }
    return render(request, 'my_orders.html', context)


def Login(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(phone=phone, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully !')
            return redirect('profile')
        else:
            messages.error(request, 'Login failed, Invalid Credentials!')
            return redirect('login')
    return render(request, 'login.html')


def Logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully !')
    return redirect('login')


def signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('number')
        pass_word = request.POST.get('password')

        if User.objects.filter(phone=phone).exists():
            messages.error(request, 'Mobile number already registered. Please Login to continue')
            return redirect('login')

        my_user = User.objects.create_user(phone=phone, password=pass_word)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.save()
        messages.success(request, 'User created successfully !!')
        return redirect('login')

    return render(request, 'signup.html')


def generate_bill(request):
    t_number = request.GET.get('table')
    order_for_table = order.objects.filter(table=t_number, bill_clear=False)
    total_bill = 0
    now = datetime.now()
    now_ist = now + timedelta(hours=5, minutes=30)

    bill_items = []
    c_name = ''
    c_phone = ''
    for o in order_for_table:
        total_bill += int(o.price)
        o.bill_clear = True
        o.save()
        bill_items.append({'order_items': o.items_json})
        c_name = o.name
        c_phone = o.phone

    order_dict = {}
    try:
        for item in bill_items:
            for key, value in item.items():
                order_items = json.loads(value)

                for pr_key, pr_value in order_items.items():
                    try:
                        if isinstance(pr_value, dict):
                            item_name = pr_value.get('name', '').lower()
                            quantity = int(pr_value.get('quantity', 0))
                            price = int(pr_value.get('price', 0))

                            if item_name and quantity and price:
                                order_dict[item_name] = [quantity, (price * quantity)]

                        elif isinstance(pr_value, (list, tuple)) and len(pr_value) >= 3:
                            quantity = int(pr_value[0])
                            item_name = pr_value[1].lower()
                            price = int(pr_value[2])

                            if item_name and quantity and price:
                                order_dict[item_name] = [quantity, (price * quantity)]

                    except (TypeError, ValueError, KeyError, IndexError) as e:
                        print(f"⚠️ Error processing item {pr_key}: {e}")
                        continue

    except (json.JSONDecodeError, ValueError) as e:
        print(f"❌ Error parsing order items: {e}")
        messages.error(request, 'Error generating bill: Invalid order data')
        return redirect('all_orders')

    if not order_dict:
        messages.warning(request, 'No valid items found for this table')
        return redirect('all_orders')

    new_bill = bill(
        order_items=str(order_dict),
        name=c_name,
        bill_total=total_bill,
        phone=c_phone,
        bill_time=now_ist
    )
    new_bill.save()

    bill_tax = round(total_bill - total_bill / 1.05)
    bill_subtotal = total_bill - bill_tax

    context = {
        'order_dict': order_dict,
        'bill_total': total_bill,
        'bill_subtotal': bill_subtotal,
        'bill_tax': bill_tax,
        'name': c_name,
        'phone': c_phone,
        'inv_id': new_bill.id,
    }
    return render(request, 'generate_bill.html', context)


def view_bills(request):
    if request.user.is_anonymous:
        messages.error(request, 'You Must be an admin user to view this!')
        return redirect('')

    all_bills = bill.objects.all().order_by('-bill_time')
    for b in all_bills:
        try:
            if isinstance(b.order_items, str):
                try:
                    b.order_items = json.loads(b.order_items)
                except (json.JSONDecodeError, ValueError):
                    try:
                        b.order_items = ast.literal_eval(b.order_items)
                    except (ValueError, SyntaxError):
                        b.order_items = {'error': 'Could not parse order items'}
            else:
                b.order_items = b.order_items
        except Exception as e:
            print(f"Error parsing bill items: {e}")
            b.order_items = {'error': 'Could not parse order items'}

    context = {'bills': all_bills}
    return render(request, 'bills.html', context)


def generate_qr_code(request, table_number):
    if not request.user.is_superuser:
        messages.error(request, 'Only admins can generate QR codes!')
        return redirect('menu')

    qr_link = request.build_absolute_uri(f'/menu?table={table_number}')
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(qr_link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response


def qr_manager(request):
    if request.user.is_anonymous:
        messages.error(request, 'Please Login first!')
        return redirect('login')
    if not request.user.is_superuser:
        messages.error(request, 'Only admins can access QR Manager!')
        return redirect('menu')

    context = {
        'table_range': range(1, 11),
    }
    return render(request, 'qr_manager.html', context)


def forgot_password(request):
    if request.method == 'POST':
        phone = request.POST.get('phone', '').strip()
        if User.objects.filter(phone=phone).exists():
            request.session['reset_phone'] = phone
            return redirect('reset_password')
        else:
            messages.error(request, 'No account found with this mobile number.')
    return render(request, 'forgot_password.html')


def reset_password(request):
    phone = request.session.get('reset_phone')
    if not phone:
        messages.error(request, 'Session expired. Please try again.')
        return redirect('forgot_password')

    if request.method == 'POST':
        pw1 = request.POST.get('password1', '').strip()
        pw2 = request.POST.get('password2', '').strip()
        if pw1 != pw2:
            messages.error(request, 'Passwords do not match!')
        elif len(pw1) < 4:
            messages.error(request, 'Password must be at least 4 characters.')
        else:
            user = User.objects.get(phone=phone)
            user.set_password(pw1)
            user.save()
            del request.session['reset_phone']
            messages.success(request, 'Password reset successfully! Please log in.')
            return redirect('login')

    return render(request, 'reset_password.html')