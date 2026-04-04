# 🍍 Home of Flavours - Complete Feature Documentation

## 🌟 System Features

### 1. Authentication & Authorization

#### User Registration
- **Phone-based signup**: Unique phone numbers as primary identifier
- **Name fields**: First name and last name
- **Password protection**: Secure password handling
- **Duplicate prevention**: Phone number uniqueness enforced

**Signup Page**: `/signup`

#### User Login
- **Phone authentication**: Use phone number to login
- **Session management**: Persistent login session
- **Remember user**: Session persists across browser restart
- **Logout functionality**: Clear session and redirect

**Login Page**: `/login`

#### Admin/Manager Role
- **Superuser access**: Full system control
- **Special privileges**:
  - Add/Delete menu items
  - View all orders
  - Generate bills
  - Access admin dashboard
  - Generate QR codes

---

### 2. Menu Management

#### Browse Menu
- **Categorized view**: Items organized by category
  - Papad
  - Starter
  - Gravy
  - Bread
  - Dal
  - Rice
  - Dessert
  - Beverage
- **Item details**: Name, price, description, image
- **Add to cart**: Direct from menu page
- **Real-time count**: Cart counter updates

**Menu Page**: `/menu`

#### Manage Menu (Admin Only)
- **Add items**: Upload new dishes
- **Upload images**: Support for food photography
- **Set pricing**: Dynamic pricing
- **Write descriptions**: Detailed item info
- **Delete items**: Remove from menu
- **Organize**: List order by category

**Management Page**: `/manage_menu`

#### MenuItem Model
```python
- Item ID (auto-generated)
- Name (max 50 chars)
- Category (papad, starter, etc.)
- Description (max 250 chars)
- Image (uploaded to media/)
- Price (string, convertible to int)
- List Order (for sorting)
```

---

### 3. Shopping Cart

#### Cart Features
- **Local storage**: Browser-based cart persistence
- **Add items**: Click "Add to cart" button
- **Adjust quantity**: 
  - Increase: Click "+" button
  - Decrease: Click "-" button
  - Remove: Decrease to 0
- **Real-time total**: Automatic calculation
- **Clear cart**: Remove all items
- **Persistent cart**: Survives page refresh

#### Cart Data Structure
```javascript
{
  "pr1": [quantity, name, price],
  "pr2": [quantity, name, price],
  // pr = product ID
}
```

**Cart Page**: `/cart`

#### Cart Workflow
1. Browse menu
2. Click "Add to cart" on items
3. Go to cart page
4. Review items and quantities
5. Adjust if needed
6. Click "Place Order"

---

### 4. Order Management

#### Place Order
- **Required info**:
  - Items in cart (minimum 1)
  - Customer name (auto-filled if logged in)
  - Phone number (auto-filled if logged in)
  - Table number or "Takeaway"
  - Total price (auto-calculated)

- **Guest ordering**: Can order without login
- **Logged-in ordering**: Auto-fills customer info
- **Table selection**: Number or takeaway option

#### Order Model
```python
- Order ID (primary key)
- Items JSON (stored as string)
- Customer Name
- Customer Phone
- Table/Takeaway status
- Total Price
- Order Time
- Bill Clear Status (boolean)
```

**Place Order**: `/cart` → POST request

---

### 5. Order Tracking

#### Customer Order History
- **My Orders page**: View personal orders
- **Filter by table**: Orders grouped by table
- **Order details**:
  - Order time
  - Items ordered
  - Quantities
  - Total amount
  - Bill status

- **Logged-in feature only**

**My Orders Page**: `/my_orders`

#### Admin Order Monitoring
- **All Orders page**: View every order placed
- **Organized by table**: Grid view grouped by table
- **Real-time updates**: See orders as they come in
- **Quick actions**: Generate bill directly from order

- **Admin-only access**

**All Orders Page**: `/all_orders`

---

### 6. Billing System

#### Generate Bills
- **By table**: Select table and generate bill
- **Calculate totals**: Automatic sum of all items
- **Item breakdown**: List each item with qty and price
- **Customer info**: Name, phone, invoice ID
- **Timestamp**: Creates bill_time

#### Bill Features
- **Invoice numbering**: Auto-generated ID
- **Print support**: "Print Bill" button
- **Bill storage**: Saved to database
- **Tax calculation**: Not included (can be added)
- **Payment status**: Clear bill after payment

**Generate Bill**: `/generate_bill?table=X`

#### Bill View for Admin
- **All bills page**: Complete history
- **Sortable**: By invoice ID or date
- **Details**: Customer, items, amounts
- **Print-friendly**: Format for receipts

**Bills Page**: `/view_bills`

---

### 7. Reviews & Ratings

#### Write Review
- **Customer feedback**: Structured reviews
- **Max 250 characters**: Comment limit
- **Logged-in users**: Can submit reviews
- **Anonymous option**: For guests (future enhancement)

#### Review Display
- **Latest first**: Newest reviews on top
- **Author name**: Customer name displayed
- **Date stamp**: Review date shown
- **Public display**: All reviews visible to everyone

**Reviews Page**: `/reviews`

#### Rating Model
```python
- Review ID (auto)
- Name (customer name)
- Comment (text, max 250 chars)
- Date (review date)
```

---

### 8. User Profile

#### Profile Information
- **Logged-in users only**
- **Displays**:
  - First name
  - Last name
  - Phone number
  - Total orders count
  - Badge for order milestones

#### Profile Data
```python
User {
  - first_name
  - last_name
  - phone (unique)
  - order_count (tracks loyalty)
  - is_superuser (admin status)
}
```

**Profile Page**: `/profile`

---

### 9. QR Code Feature

#### Generate QR Codes
- **Table-specific codes**: Each table has unique code
- **Direct menu access**: Links to menu page
- **Pre-filled table info**: Table number in URL parameter

#### QR Code Implementation
```
URL Format: http://site.com/menu?table=1
QR contains full URL
Scans directly to menu
```

#### Usage Workflow
1. Admin generates QR code for table
2. QR is printed and placed on table
3. Customer scans QR code
4. Directed to menu page
5. Automatically linked to that table
6. Orders tagged with table number

**QR Code Generation**: `/qr_code/table1`

---

### 10. Admin Dashboard

#### Dashboard Features
- **Statistics cards**:
  - Total Orders
  - Total Customers
  - Total Revenue (₹)

- **Quick actions**:
  - View All Orders
  - Add New Menu Item
  - View Bills

- **Instructions section**: System guidance

#### Dashboard Data
```python
context = {
  'total_orders': Order.objects.count(),
  'total_customers': User.objects.filter(cafe_manager=False).count(),
  'total_revenue': sum(o.price for o in Order.objects.all()),
}
```

**Admin Dashboard**: `/` (when logged in as admin)

---

### 11. Navigation & Layout

#### Navigation Bar
- **Logo and branding**: Home of Flavours
- **Dynamic menu**: Changes based on user role
- **Search functionality**: Can be added
- **Cart counter**: Real-time update
- **Mobile responsive**: Hamburger menu for mobile

#### Customer Navigation
- Menu
- Cart
- Reviews
- Profile
- My Orders
- Logout

#### Admin Navigation
- Menu (different view)
- Dashboard
- Add Item
- Orders
- Bills
- Profile
- Logout

---

### 12. Responsive Design

#### Bootstrap 5 Integration
- **Mobile-first approach**
- **Breakpoints**:
  - Mobile: < 576px
  - Tablet: 576px - 992px
  - Desktop: > 992px

#### Features
- Touch-friendly buttons
- Responsive grid layout
- Collapsible navigation
- Readable fonts
- Proper spacing

---

### 13. Messages & Alerts

#### Alert Types
- **Success**: Order placed, item added
- **Error**: Login failed, missing fields
- **Info**: General information
- **Warning**: Confirmations needed

#### Message Display
- Toast-like alerts
- Dismissible with close button
- Auto-dismiss after timeout (optional)
- Color-coded by type

---

## 🔄 Complete User Journeys

### Journey 1: Guest Ordering (Takeaway)
```
1. Visit http://127.0.0.1:8000/
2. Browse menu (anonymous)
3. Add items to cart
4. Go to cart page
5. Click "Place Order"
6. Enter name and phone (not logged in)
7. Select "Take Away"
8. Confirm order
9. See success message
10. Redirect to home
```

### Journey 2: Registered User Dine-In
```
1. Visit website
2. Click Login
3. Enter phone and password
4. Go to profile to confirm details
5. Click Menu
6. Browse items by category
7. Add to cart
8. Go to cart
9. Click "Place Order"
10. Auto-filled name and phone
11. Select table number (let's say table1)
12. Confirm order
13. Go to "My Orders"
14. See order with table info
15. Admin generates bill when done
```

### Journey 3: Admin Managing Service
```
1. Login as admin (superuser)
2. Go to Dashboard
3. See statistics
4. Add menu items via "Add Item"
5. Generate QR codes for each table
6. Print and place QR codes
7. Customers scan and order
8. Monitor "All Orders"
9. See orders by table
10. Click "Generate Bill" when service ends
11. Review bill and print
12. View all bills in "View Bills"
13. Analyze revenue in dashboard
```

---

## 📊 Data Flow Diagram

```
Customer Input
    ↓
Menu Page (Browse Items)
    ↓
Shopping Cart (LocalStorage)
    ↓
Place Order (POST /cart)
    ↓
Order Model (Saved to DB)
    ↓
Admin Monitoring (All Orders)
    ↓
Bill Generation (/generate_bill)
    ↓
Bill Model (Saved to DB)
    ↓
View Bills (History)
```

---

## 🔐 Security Features

- **Phone-based authentication**: Unique identifier
- **Password hashing**: Django built-in security
- **CSRF protection**: All POST requests protected
- **Admin-only views**: Permission checks on all admin features
- **Session management**: Secure user sessions
- **Input validation**: Form validation
- **Error handling**: Graceful error messages

---

## 📱 Mobile Optimization

- **Responsive layout**: Works on all devices
- **Touch-friendly**: Larger tap targets
- **Mobile navigation**: Hamburger menu
- **Optimized images**: Fast loading
- **Viewport settings**: Proper scaling

---

## ⚡ Performance Features

- **Local storage**: Fast cart management
- **Minimal database queries**: Optimized views
- **Image optimization**: Pillow compression (can be added)
- **Caching**: Django caching (can be implemented)
- **CDN ready**: Bootstrap from CDN

---

## 🚀 Future Enhancement Ideas

1. **Payment Integration**: Stripe, Razorpay, SonyPay
2. **Email/SMS Notifications**: Order updates
3. **Estimated delivery time**: Dynamic calculation
4. **Staff messaging**: Kitchen communication
5. **Ratings by item**: Individual item ratings
6. **Combo deals**: Bundle offerings
7. **Loyalty program**: Points and rewards
8. **Real-time notifications**: WebSocket or push
9. **Mobile app**: Native iOS/Android
10. **Analytics dashboard**: Advanced reporting

---

## 📞 API Endpoints Summary

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | / | Menu (Home) |
| GET | /menu | View Menu |
| GET | /cart | Shopping Cart |
| POST | /cart | Place Order |
| GET | /my_orders | Customer Orders |
| GET | /all_orders | Admin Orders |
| POST | /manage_menu | Add Menu Item |
| GET | /generate_bill | Generate Bill |
| GET | /view_bills | View Bills |
| GET | /reviews | View/Write Reviews |
| POST | /reviews | Submit Review |
| GET | /profile | User Profile |
| GET/POST | /login | User Login |
| GET/POST | /signup | User Registration |
| GET | /logout | User Logout |
| GET | /qr_code/<table> | Generate QR |

---

**System is fully functional and ready for use! 🎉**
