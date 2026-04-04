# ⚡ Quick Reference Guide - All Buttons & Functions Working

## 🏠 Home Page (http://127.0.0.1:8000/)

### For Customers
```
┌─────────────────────────────────────┐
│ 🍔 Hungry? Order Now Button          │ → Goes to menu
│ Read Reviews Button                  │ → Shows customer reviews  
│ Stats: 500+ Items | 30min | 4.8★     │ → Information display
│ Featured This Week Button            │ → Links to menu
│ Browse Menu Button                   │ → Links to menu
└─────────────────────────────────────┘
```

### For Admin
```
┌─────────────────────────────────────┐
│ 📊 Admin Dashboard                   │
├─────────────────────────────────────┤
│ Total Orders: [Count] 🛒             │
│ Total Customers: [Count] 👥          │
│ Total Revenue: ₹[Amount] 💰          │
├─────────────────────────────────────┤
│ View All Orders Button               │ → /all_orders
│ Add New Menu Item Button             │ → /manage_menu
│ View Bills Button                    │ → /view_bills
│ View Menu Button                     │ → /menu
└─────────────────────────────────────┘
```

---

## 🍽️ Menu Page (http://127.0.0.1:8000/menu)

### Search & Filter
```
🔍 Search Bar
   ├─ Type dish name
   └─ Results filter in real-time

🏷️ Category Buttons
   ├─ All Dishes (shows all items)
   ├─ 🍚 Biryani
   ├─ 🍛 Curry
   ├─ 🥘 Bread
   ├─ 🥤 Beverages
   └─ 🍰 Desserts
```

### For Each Food Item
```
┌─────────────────────┐
│ [Food Image]        │
│ -10% Badge          │ (discount)
│ V Badge             │ (veg indicator)
├─────────────────────┤
│ Dish Name           │
│ ★★★★☆ (128 ratings)│
│ ⏱️ 25-30 min        │
│ ₹Free Delivery      │
│ ₹250 ₹300 (price)   │
│ [Add to Cart] ✓     │ → Adds to cart + notification
└─────────────────────┘
```

### Bottom Navigation
```
🛒 Go To Cart Button → Links to /cart
```

---

## 🛒 Cart Page (http://127.0.0.1:8000/cart)

### Left Side - Cart Items
```
📋 Show all items added:
   ├─ Item Name
   ├─ Price x Quantity
   └─ Item Total (Price × Qty)

🗑️ Clear Cart Button
   └─ Confirms deletion then clears all
```

### Right Side - Order Summary
```
┌──────────────────────┐
│ 📋 Order Summary     │
├──────────────────────┤
│ Items: [Count]       │
│ Subtotal: ₹[Amount]  │
│ Delivery: ₹0         │
│ Tax (5%): ₹[Amount]  │
│ ─────────────────────│
│ Total: ₹[FINAL]      │
├──────────────────────┤
│ ✅ Place Order       │ → Submits order
│ ➕ Add More Items    │ → Goes to /menu
│ ➖ Clear Cart        │ → Clears all items
└──────────────────────┘
```

### Empty Cart State
```
🎒 Your cart is empty!
📖 Browse Menu Button → /menu
```

---

## 👤 User Account Features

### Login (http://127.0.0.1:8000/login)
```
📱 Phone Number: [Input field]
🔐 Password: [Input field]
🔓 Login Button → Validates & logs in

📝 Sign Up Link → /signup
```

### Sign Up (http://127.0.0.1:8000/signup)
```
👤 First Name: [Input]
👤 Last Name: [Input]
📱 Phone Number: [Input]
🔐 Password: [Input]
🔐 Confirm Password: [Input]
✅ Sign Up Button

🔓 Already have account? Login Link → /login
```

### Profile (http://127.0.0.1:8000/profile)
```
Shows logged-in user information:
- Name
- Phone number
- Account status
```

### Logout
```
🚪 Logout Button (in navbar)
   └─ Logs out user and redirects to home
```

---

## 📦 Order Management

### My Orders (http://127.0.0.1:8000/my_orders)
```
🛍️ Order History
   ├─ Table/Order grouping
   ├─ Order items list
   ├─ Quantities
   └─ Order totals
```

### All Orders - Admin (http://127.0.0.1:8000/all_orders)
```
📊 All Orders in System
   ├─ Group by Table
   ├─ Customer name
   ├─ Customer phone
   ├─ Order items
   ├─ Order total
   └─ 📄 Generate Bill Button

Generate Bill Button Options:
   └─ Creates invoice & marks order complete
```

### Generate Bill (http://127.0.0.1:8000/generate_bill)
```
📋 Invoice Display
   ├─ Order items detailed list
   ├─ Item × Qty = Total
   ├─ Grand Total
   ├─ Customer information
   └─ 🖨️ Print Button
```

---

## ⭐ Reviews & Ratings (http://127.0.0.1:8000/reviews)

```
⭐ View All Reviews
   ├─ Customer name
   ├─ Rating/Comment
   └─ Date

✍️ Submit Review (if logged in)
   ├─ Comment text field
   └─ ✅ Submit Button
```

---

## 🍕 Manage Menu - Admin (http://127.0.0.1:8000/manage_menu)

```
➕ Add New Menu Item Form
   ├─ 📝 Item Name: [Input]
   ├─ 🏷️ Category: [Dropdown]
   │   ├─ Biryani
   │   ├─ Curry
   │   ├─ Bread
   │   ├─ Beverage
   │   └─ Dessert
   ├─ 📄 Description: [Text Area]
   ├─ 💰 Price: [Input]
   ├─ 🖼️ Image: [Upload]
   └─ ✅ Save Item Button
      └─ Item appears in menu immediately
```

---

## 🎟️ Special Features

### QR Code Generation (http://127.0.0.1:8000/qr_code/TableX)
```
1️⃣ Generate QR for each table
   └─ http://127.0.0.1:8000/qr_code/Table1

2️⃣ QR Code displays
   └─ Can be printed/displayed at table

3️⃣ When scanned
   └─ Links to menu with table parameter
   └─ Table value stored in localStorage
   └─ Order gets assigned to table
```

### Offers (http://127.0.0.1:8000/offers)
```
🎉 Special offers & deals displayed
```

### Bills (http://127.0.0.1:8000/view_bills)
```
📊 View all generated bills/invoices
```

---

## 🌐 Navigation Bar (Present on All Pages)

```
┌────────────────────────────────────────────────────────────────┐
│ 🏠 Logo / Brand Name  │  Menu  │  ...  │  🔔 Cart Badge │ 👤   │
│ (clickable → home)    │(→menu) │       │  [Item Count]  │(menu)│
├────────────────────────────────────────────────────────────────┤
│ When Logged Out:      When Logged In:      When Admin:        │
│ ├─ 🔓 Login           ├─ 👤 Profile        ├─ All above +    │
│ ├─ 📝 Sign Up         ├─ 🚪 Logout         ├─ Dashboard      │
│ └─ ...                └─ ...               └─ ...            │
└────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Complete User Journey

### Customer Journey
```
1. 🏠 Home Page
   ↓ [Click "Order Now"]
2. 🍽️ Menu Page  
   ↓ [Search/Filter items]
3. 🛒 Add items to cart
   ↓ [Click "Add to Cart"]
4. 📋 Cart Page
   ↓ [Review order]
5. ✅ Place Order
   ↓ [Order created]
6. 📦 Order Confirmation
   ↓ [Order appears in "My Orders"]
```

### Admin Journey
```
1. 🏠 Home (Admin Dashboard)
   ├─ [View All Orders] → 📊 Order Management
   ├─ [Add Menu Item] → 🍕 Manage Menu
   ├─ [View Bills] → 📄 Billing
   └─ [View Menu] → 🍽️ Menu Items
```

---

## 🔧 Keyboard Shortcuts (If Enabled)

```
[Work in Progress for future enhancement]
- Ctrl+K: Search menu
- Escape: Close modals/notifications
- Enter: Submit forms
```

---

## ✅ All Buttons Status - Working

| Feature | Status | Location |
|---------|--------|----------|
| Add to Cart | ✅ Working | Menu Page |
| Place Order | ✅ Working | Cart Page |
| Clear Cart | ✅ Working | Cart Page |
| Login | ✅ Working | Login Page |
| Sign Up | ✅ Working | Signup Page |
| Logout | ✅ Working | Navbar |
| Generate Bill | ✅ Working | All Orders Page |
| View Orders | ✅ Working | Admin Dashboard |
| Search Menu | ✅ Working | Menu Page |
| Filter by Category | ✅ Working | Menu Page |
| View Reviews | ✅ Working | Reviews Page |
| Submit Review | ✅ Working | Reviews Page |
| Add Menu Item | ✅ Working | Manage Menu (Admin) |
| Delete Menu Item | ✅ Working | Menu Page (Admin) |
| View Profile | ✅ Working | Profile Page |
| Generate QR | ✅ Working | QR Code Page |

---

## 📞 Support & Help

**Having issues?**
1. Clear browser cache: Ctrl+Shift+Delete
2. Clear localStorage: Press F12 → Console → localStorage.clear()
3. Refresh page: Ctrl+R
4. Check browser console for errors: F12
5. Verify all dependencies installed

**Need to reset?**
- Clear all carts: localStorage.clear()
- Reset database: Delete db.sqlite3 and run migrations
- Recreate admin: python manage.py createsuperuser

