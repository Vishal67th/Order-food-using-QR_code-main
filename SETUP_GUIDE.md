# Complete Setup Guide - Home of Flavours Food Ordering System

## ⚙️ First Time Setup

### 1. Initial Configuration (Already Done)
- ✅ Django project created
- ✅ Virtual environment configured
- ✅ Dependencies installed
- ✅ Database migrations created
- ✅ Server running on http://127.0.0.1:8000

### 2. Create Admin Account
If not created yet, run:
```bash
python manage.py createsuperuser
```

**Example credentials:**
- Phone: `9876543210`
- Password: `admin123`

## 🚀 Quick Start (3 Steps)

### Step 1: Start the Server
```bash
cd Order-food-using-QR_code-main
.\.venv\Scripts\python.exe manage.py runserver
```

### Step 2: Access the Application
- **Customer**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin

### Step 3: Login as Admin
- Phone: `your_phone_number`
- Password: `your_password`

## 📋 Admin Features Setup

### Add Menu Items
1. Login as Admin
2. Go to "Dashboard" or "Menu"
3. Click "Add Item"
4. Fill in:
   - Dish Name
   - Category (Papad, Starter, Gravy, Bread, Dal, Rice, Dessert, Beverage)
   - Price
   - Description
   - Upload Image
5. Click "Add Dish"

### Generate QR Codes for Tables
1. Login as Admin
2. Navigate to URL: `http://127.0.0.1:8000/qr_code/table1`
3. Generate QR codes for each table (table1, table2, table3, etc.)
4. Print and place at each table

### View Orders
1. Go to "View All Orders"
2. Orders are grouped by table
3. Click "Generate Bill" when ready

### Generate Bills
1. Click "Generate Bill" button
2. Review items and total
3. Click "Print Bill"
4. Bill is saved to database

## 🎯 Customer Flow

### Step 1: Browse Menu
- Click on "Menu" in navigation
- View items by category
- Click "Add to cart"

### Step 2: Manage Cart
- See cart count increase
- Go to "Cart" page
- Adjust quantities if needed

### Step 3: Place Order
- Click "Place Order"
- Either login or continue as guest
- Order is saved

### Step 4: View Orders
- If logged in: Go to "My Orders"
- See order history
- Track order status

## 📊 Dashboard Overview

### Admin Dashboard Shows:
- **Total Orders**: Number of orders placed
- **Total Customers**: Registered users
- **Total Revenue**: Sum of all completed orders

### Quick Actions:
- View All Orders
- Add New Menu Item
- View Bills

## 🔐 User Authentication

### Login
- Phone number required
- Password required
- Supports multiple login attempts

### Signup
- Enter first and last name
- Enter phone number (10 digits)
- Create password
- Confirm password
- Creates account automatically

### Logout
- Click "Logout" button
- Redirects to login page

## 🛒 Cart Features

### Local Storage Based
- Cart saved in browser
- Persists between page refreshes
- Survives browser restart

### Cart Operations
- **Add Item**: Click item and add to cart
- **Increase Qty**: Click "+" button
- **Decrease Qty**: Click "-" button
- **Clear Cart**: Click "Clear Cart" button
- **View Total**: Shown at bottom

## 📝 Reviews System

### Write a Review
1. Login to your account
2. Go to "Reviews"
3. Write comment (max 250 chars)
4. Click "Submit Review"

### View Reviews
- All customer reviews displayed
- Shows customer name and date
- Latest reviews first

## 🎨 Template Structure

### Base Template (base.html)
- Navigation bar
- Message alerts
- Footer
- Script includes
- Cart counter

### Menu Template
- Category-based organization
- Add to cart buttons
- Admin delete buttons

### Cart Template
- Item list
- Quantity controls
- Total calculation
- Order placement

### Admin Templates
- All orders list
- Menu management
- Bill generation
- Bill history

## 💾 Database Models

### User Model
```
- Phone (unique)
- First Name
- Last Name
- Password
- Is Superuser
- Order Count
```

### MenuItem Model
```
- Name
- Category
- Description
- Image
- Price
- Display Order
```

### Order Model
```
- Order ID (auto)
- Items JSON
- Customer Name
- Phone
- Table/Takeaway
- Price
- Order Time
- Bill Clear Status
```

### Bill Model
```
- Bill ID (auto)
- Order Items
- Customer Name
- Phone
- Total Amount
- Bill Time
```

## 🎬 Common Workflows

### Admin Workflow
1. Login as admin
2. Add menu items
3. Generate QR codes for tables
4. Distribute QR codes to tables
5. Monitor orders in real-time
6. Generate bill when service ends
7. View revenue analytics

### Customer (Dine-in) Workflow
1. Scan QR code on table
2. Browse menu
3. Add items to cart
4. Place order (may login)
5. Wait for order
6. Eat and enjoy
7. Admin generates bill for table

### Customer (Takeaway) Workflow
1. Visit website directly
2. Browse menu
3. Add items to cart
4. Select "Takeaway" option
5. Place order
6. Provide phone number
7. Wait for order
8. Pay and take order

### Customer (Registered User) Workflow
1. Login with phone
2. Browse menu
3. Add items
4. Place order
5. Get confirmation
6. View all previous orders in "My Orders"
7. Accumulate order count for loyalty

## 🔧 Customization

### Change Restaurant Name
- Edit `base.html` navbar
- Change "SnackDonald's" to your restaurant name
- Update in admin panel

### Modify Categories
- Edit `views.py` manage_menu function
- Add new categories in the if-elif chain
- Add to dropdown in manage_menu.html

### Change Colors
- Modify `base.html` - Bootstrap classes
- bg-danger → other bootstrap colors
- btn-primary → other button colors

### Add New Features
- Add models in `models.py`
- Create views in `views.py`
- Create templates in `templates/`
- Update `urls.py`
- Run migrations

## 📱 Responsive Design

- Mobile-friendly (Bootstrap 5)
- Tablet-friendly
- Desktop-optimized
- Touch-friendly buttons
- Responsive navigation

## 🐛 Troubleshooting

### Issue: "Port 8000 already in use"
```bash
# Use different port
python manage.py runserver 8001
```

### Issue: "Image not uploading"
```bash
# Check MEDIA_ROOT in settings.py
# Ensure media/ folder exists
# Check file permissions
```

### Issue: "Static files not loading"
```bash
python manage.py collectstatic
```

### Issue: "Database locked"
```bash
# Delete db.sqlite3
# Run migrations again
python manage.py makemigrations
python manage.py migrate
```

### Issue: "Module not found"
```bash
# Reinstall dependencies
pip install -r requirements.txt
# Or manually:
pip install django pillow qrcode
```

## 📞 Support

- Check logs: `python manage.py`
- Admin panel: `/admin`
- Django docs: https://docs.djangoproject.com/

---

**Your Home of Flavours System is Ready! 🎉**
cd "c:\Users\thaku\OneDrive\Documents\Desktop\Order-food-using-QR_code-main\Order-food-using-QR_code-main\Order-food-using-QR_code-main"; & "c:/Users/thaku/OneDrive/Documents/Desktop/Order-food-using-QR_code-main/Order-food-using-QR_code-main/.venv/Scripts/python.exe" manage.py runserver