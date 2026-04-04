# ⚡ Quick Reference Guide

## 🚀 Start Application

```bash
# Navigate to project
cd Order-food-using-QR_code-main/Order-food-using-QR_code-main

# Start server
python manage.py runserver
```

**Access at**: http://127.0.0.1:8000/

---

## 👤 Admin Credentials

**Phone**: (Your created phone number)  
**Password**: (Your created password)

To create admin:
```bash
python manage.py createsuperuser
```

---

## 📍 Important URLs

| URL | Purpose | Access |
|-----|---------|--------|
| `/` | Home/Menu | All |
| `/menu` | Browse Menu | All |
| `/cart` | Shopping Cart | All |
| `/login` | Login Page | All |
| `/signup` | Register | All |
| `/logout` | Logout | Logged In |
| `/profile` | User Profile | Logged In |
| `/my_orders` | Your Orders | Logged In |
| `/reviews` | Reviews | All |
| `/manage_menu` | Add Items | Admin |
| `/all_orders` | Monitor Orders | Admin |
| `/generate_bill` | Create Bill | Admin |
| `/view_bills` | Bill History | Admin |
| `/qr_code/table1` | QR for table | Admin |
| `/admin` | Django Admin | Admin |

---

## 🎯 Main Features

### For Customers
- ✅ Browse menu by category
- ✅ Add items to cart
- ✅ Place orders
- ✅ View order history
- ✅ Write reviews
- ✅ Manage profile

### For Admin
- ✅ Add/remove menu items
- ✅ Monitor all orders
- ✅ Generate bills
- ✅ Generate QR codes
- ✅ View revenue stats
- ✅ Manage system

---

## 🛒 Shopping Cart

### Add Items
1. On Menu page
2. Click "Add to cart"
3. See cart counter increase

### Manage Items
- **Increase**: Click "+"
- **Decrease**: Click "-"
- **Remove**: Decrease to 0
- **Clear all**: "Clear Cart" button

### Place Order
1. Go to Cart page
2. Review items
3. Click "Place Order"
4. Login or continue as guest
5. Select table/takeaway
6. Confirm

---

## 👨‍💼 Admin Workflow

### Add Menu Item
1. Login as admin
2. Go to "Add Item"
3. Fill: Name, Category, Price, Description
4. Upload image
5. Click "Add Dish"

### Monitor Orders
1. Click "View All Orders"
2. See orders grouped by table
3. Track customer info
4. See total per order

### Generate Bills
1. Click "Generate Bill" button
2. Review item breakdown
3. Check total amount
4. Click "Print Bill"

### Check Analytics
1. Go to dashboard
2. See:
   - Total orders placed
   - Total registered customers
   - Total revenue earned

---

## 🔑 Keyboard Shortcuts

| Action | Method |
|--------|--------|
| Reload page | F5 or Ctrl+R |
| Go back | Alt+← |
| Search | Ctrl+F |
| Print | Ctrl+P |

---

## 📱 Mobile Access

The system is fully mobile-responsive:
- Browse menu on phone
- Add to cart on tablet
- Place orders from any device
- Admin features on mobile

---

## 💾 Database Commands

### Create Migrations
```bash
python manage.py makemigrations
```

### Apply Migrations
```bash
python manage.py migrate
```

### Create Admin
```bash
python manage.py createsuperuser
```

### Access Django Shell
```bash
python manage.py shell
```

### Reset Database
```bash
python manage.py flush  # Delete all data
python manage.py migrate  # Recreate tables
```

---

## 🐛 Common Issues

### Problem: Server won't start
```bash
# Port in use? Use different port
python manage.py runserver 8001
```

### Problem: Image not showing
- Check image uploaded correctly
- Verify /media folder exists
- Check image file permissions

### Problem: Cart empty after refresh
- Browser localStorage cleared?
- Try incognito mode
- Check browser console for JS errors

### Problem: Admin login fails
- Phone number correct? (10 digits)
- Password correct?
- Check caps lock
- Try resetting password via admin panel

---

## 📊 Quick Stats

### Database Counts
Check in Django shell:
```python
python manage.py shell
from cafe.models import *
print(Order.objects.count())  # Total orders
print(User.objects.count())   # Total users
print(menu_item.objects.count())  # Menu items
print(bill.objects.count())   # Bills generated
```

---

## 🎨 Customization

### Change App Name
Edit in `base.html`:
```html
<a class="navbar-brand" href="/">YourName's</a>
```

### Change Colors
Edit in `base.html` `<style>`:
```css
bg-danger → bg-primary, bg-success, etc.
```

### Modify Categories
Edit in `views.py` manage_menu function and template

---

## 📞 Help & Support

### Django Admin Panel
- URL: `/admin`
- Direct database access
- Create/edit/delete records
- Advanced management

### Django Shell
```bash
python manage.py shell
# Run any Python code
# Access models directly
# Debug issues
```

### Check Logs
- Terminal output shows:
  - HTTP requests
  - Errors
  - Warnings
  - Database queries

---

## ✅ Verification Checklist

- [ ] Server running on http://127.0.0.1:8000
- [ ] Can view menu items
- [ ] Can add items to cart
- [ ] Can logout and login
- [ ] Can view orders as admin
- [ ] Can generate bills
- [ ] Can generate QR codes
- [ ] Can access admin panel

---

## 🎓 Learning Resources

- Django Docs: https://docs.djangoproject.com/
- Bootstrap Docs: https://getbootstrap.com/docs/
- jQuery Docs: https://api.jquery.com/
- Python Docs: https://docs.python.org/

---

## 📝 Notes

- All phone numbers are unique
- Cart stored in browser (LocalStorage)
- Orders saved to database
- Bills auto-generated and saved
- Admin has full system access
- System uses SQLite database
- All times in IST (+5:30 from UTC)

---

## 🎯 Next Steps

1. ✅ Start the server
2. ✅ Create admin account
3. ✅ Add menu items
4. ✅ Generate QR codes
5. ✅ Test customer flow
6. ✅ Generate sample bills
7. ✅ Customize branding
8. ✅ Deploy (see Production Guide)

---

**Happy Ordering! 🍕🍔🍜**

*For detailed documentation, see README.md and FEATURES.md*
