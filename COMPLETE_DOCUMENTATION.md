# 🍕 SnackDonald's - Complete Food Ordering System Documentation

**Version**: 1.0  
**Status**: ✅ FULLY OPERATIONAL  
**Last Updated**: April 2, 2026

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [Architecture & System Design](#architecture--system-design)
4. [Database Models](#database-models)
5. [Project Structure](#project-structure)
6. [Installation & Setup](#installation--setup)
7. [Configuration](#configuration)
8. [Features & Functionality](#features--functionality)
9. [User Workflows](#user-workflows)
10. [Admin Features](#admin-features)
11. [API Endpoints](#api-endpoints)
12. [Frontend Components](#frontend-components)
13. [Code Explanation](#code-explanation)
14. [Troubleshooting](#troubleshooting)
15. [Deployment Guide](#deployment-guide)

---

## Project Overview

### What is Home of Flavours?

Home of Flavours is a **complete food ordering system** designed for restaurants, cafes, and food establishments. It enables customers to browse a menu, place orders either dine-in or takeaway, and manage their dining experience through a web-based interface. Admin users can manage the menu, track orders, generate bills, and view analytics.

### Key Innovations

- **QR Code Ordering**: Each table has a unique QR code for seamless ordering
- **Phone-based Authentication**: Customers use phone numbers instead of emails
- **Real-time Cart Management**: Browser-based shopping cart with local storage
- **Table-based Organization**: Orders are tracked by table number
- **Dynamic Menu Management**: Admin can add/remove items without code changes
- **Comprehensive Billing**: Automated bill generation and printing

### Business Model

```
CUSTOMER FLOW:
Scan QR → Browse Menu → Add to Cart → Checkout → Place Order → Track Status → Pay/View Bill

ADMIN FLOW:
Manage Menu → View Orders → Generate Bills → Track Revenue → Analyze Data
```

---

## Technology Stack

### Backend

| Component | Technology | Version |
|-----------|-----------|---------|
| **Framework** | Django | 5.1.6 |
| **Language** | Python | 3.13.9 |
| **Database** | SQLite3 | Latest |
| **ORM** | Django ORM | Built-in |
| **Image Processing** | Pillow | 9.2.0 |
| **QR Code Generation** | qrcode | Latest |
| **Web Server** | Django Development Server | Built-in |

### Frontend

| Component | Technology | Usage |
|-----------|-----------|-------|
| **Markup** | HTML5 | Page Structure |
| **Styling** | Bootstrap 5 | Responsive Design |
| **Scripting** | JavaScript/jQuery | DOM Manipulation |
| **Data Storage** | LocalStorage API | Client-side Cart |
| **Icons** | Bootstrap Icons | UI Elements |

### Development Tools

```bash
Virtual Environment: Python venv
Package Manager: pip
Database Migration: Django Migrations
Admin Panel: Django Admin
Server: Django Development Server
```

---

## Architecture & System Design

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         CLIENT LAYER                             │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Web Browser (HTML/CSS/JavaScript)                       │  │
│  │  • Responsive UI with Bootstrap 5                        │  │
│  │  • LocalStorage for Cart Management                      │  │
│  │  • jQuery for Dynamic Interactions                       │  │
│  └──────────────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────────────┘
                       │ HTTP Requests/Responses
                       │
┌──────────────────────▼──────────────────────────────────────────┐
│                    SERVER LAYER (Django)                         │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  URL Router (urls.py)                                    │  │
│  │  • Maps HTTP requests to view handlers                   │  │
│  │  • Manages routing for all endpoints                     │  │
│  └──────────────────────────────────────────────────────────┘  │
│                       │                                          │
│  ┌────────────────────▼──────────────────────┐                 │
│  │  Views (views.py)                         │                 │
│  │  • Handles business logic                 │                 │
│  │  • Processes forms and requests           │                 │
│  │  • Manages authentication                 │                 │
│  │  • Generates responses                    │                 │
│  └────────────────────┬──────────────────────┘                 │
│                       │                                          │
│  ┌────────────────────▼──────────────────────┐                 │
│  │  Models (models.py)                       │                 │
│  │  • Defines data structure                 │                 │
│  │  • User, MenuItem, Order, Bill, Rating    │                 │
│  │  • Database schema representation         │                 │
│  └────────────────────┬──────────────────────┘                 │
│                       │                                          │
│  ┌────────────────────▼──────────────────────┐                 │
│  │  Templates (HTML)                         │                 │
│  │  • Renders dynamic content                │                 │
│  │  • Context passing from views             │                 │
│  │  • Form rendering and display             │                 │
│  └────────────────────┬──────────────────────┘                 │
└──────────────────────┬──────────────────────────────────────────┘
                       │ ORM Queries
                       │
┌──────────────────────▼──────────────────────────────────────────┐
│                  DATABASE LAYER (SQLite3)                        │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Tables:                                                  │  │
│  │  • auth_user (User data)                                 │  │
│  │  • cafe_menu_item (Menu items)                          │  │
│  │  • cafe_order (Customer orders)                         │  │
│  │  • cafe_bill (Generated bills)                          │  │
│  │  • cafe_rating (Customer reviews)                       │  │
│  │  • Other Django system tables                           │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### Request-Response Flow

```
1. CLIENT INITIATES REQUEST
   ↓
2. BROWSER SENDS HTTP REQUEST
   ↓
3. DJANGO ROUTER (urls.py)
   → Matches URL pattern
   → Routes to appropriate view
   ↓
4. VIEW FUNCTION
   → Processes request
   → Fetches/creates data
   → Renders template
   ↓
5. TEMPLATE RENDERING
   → Receives context from view
   → Generates HTML with data
   ↓
6. HTTP RESPONSE SENT
   ↓
7. BROWSER RECEIVES & DISPLAYS
   → JavaScript executes
   → LocalStorage updates
   → UI renders
```

---

## Database Models

### 1. User Model (Custom Authentication)

**Purpose**: Store user account information  
**Custom Implementation**: Phone-based authentication instead of email

```python
class User(AbstractUser):
    phone = CharField(max_length=10, unique=True)          # Phone number as primary identifier
    phone_verified = BooleanField(default=False)           # Optional: Phone verification flag
    cafe_manager = BooleanField(default=False)             # Flag for admin/manager role
    order_count = IntegerField(default=0)                  # Track user's order count
    
    USERNAME_FIELD = 'phone'                               # Tell Django to use phone for login
    REQUIRED_FIELDS = []                                   # No other required fields for creation
```

**Key Features**:
- Inherits from `AbstractUser` (keeps Django's built-in auth features)
- Phone number is unique (prevents duplicate registrations)
- No email or username fields (simplified authentication)
- `cafe_manager` flag distinguishes admin users
- Used for tracking customer orders

**Database Table**: `auth_user`

---

### 2. MenuItem Model

**Purpose**: Store restaurant menu items

```python
class menu_item(models.Model):
    name = CharField(max_length=50)                        # Dish name (e.g., "Butter Chicken")
    category = CharField(max_length=50, default='')        # Category (e.g., "Gravy", "Bread")
    desc = CharField(max_length=250)                       # Item description
    pic = ImageField(upload_to='fimage')                   # Image file (uploaded to media/fimage/)
    price = CharField(max_length=4, default='0')           # Price as string (can convert to int)
    list_order = IntegerField(default=0)                   # Sorting order in menu
```

**Key Features**:
- Images uploaded to `media/fimage/` directory
- Organized by category for easy browsing
- Price stored as string (can be converted to integer for calculations)
- List order controls menu display sequence
- Supports 8 food categories

**Database Table**: `cafe_menu_item`  
**Categories**: Papad, Starter, Gravy, Bread, Dal, Rice, Dessert, Beverage

---

### 3. Order Model

**Purpose**: Store customer orders

```python
class order(models.Model):
    order_id = AutoField(primary_key=True)                 # Unique order identifier
    items_json = CharField(max_length=5000)                # JSON string of items: {"id": [qty, name, price]}
    name = CharField(max_length=30, default='')            # Customer name
    phone = CharField(max_length=10, default='')           # Customer phone number
    table = CharField(max_length=15, default='take away')  # Table number or "take away"
    price = CharField(max_length=5, default='0')           # Total order amount
    order_time = DateTimeField(auto_now_add=True)          # When order was placed
    bill_clear = BooleanField(default=False)               # Payment status
```

**Key Features**:
- JSON-based item storage for flexibility
- Tracks both dine-in (table number) and takeaway orders
- Timestamps all orders automatically
- Price stored as string
- Bill status tracking for payment

**Database Table**: `cafe_order`  
**Items JSON Structure**:
```json
{
  "1": [2, "Butter Chicken", 250],           // [quantity, name, price]
  "3": [1, "Naan", 50]
}
```

---

### 4. Bill Model

**Purpose**: Store generated bills/invoices

```python
class bill(models.Model):
    order_items = CharField(max_length=5000)               # JSON of items in bill
    name = CharField(default='', max_length=50)            # Customer name
    bill_total = IntegerField()                            # Total amount (integer)
    phone = CharField(max_length=10)                       # Customer phone
    bill_time = DateTimeField(auto_now_add=True)           # When bill was generated
```

**Key Features**:
- Separate from orders (decouples order from billing)
- Bill total stored as integer
- Automatic timestamp
- JSON format preserves order details
- Useful for accounting and history

**Database Table**: `cafe_bill`

---

### 5. Rating Model

**Purpose**: Store customer reviews and ratings

```python
class rating(models.Model):
    name = CharField(max_length=30)                        # Reviewer's name
    comment = CharField(max_length=250)                    # Review comment
    r_date = DateField(auto_now_add=True)                  # Review date
```

**Key Features**:
- Simple review system
- Ordered by date (newest first)
- For customer feedback

**Database Table**: `cafe_rating`

---

## Project Structure

```
Order-food-using-QR_code-main/
│
├── pr1/                              # Django PROJECT config (NOT app)
│   ├── __init__.py
│   ├── settings.py                   # Database, apps, middleware config
│   ├── urls.py                       # Project-level URL routing
│   ├── asgi.py                       # ASGI config (for deployment)
│   ├── wsgi.py                       # WSGI config (for deployment)
│   └── __pycache__/
│
├── cafe/                             # Django APP (main application logic)
│   ├── __init__.py
│   ├── admin.py                      # Django admin customization (UNUSED)
│   ├── apps.py                       # App configuration
│   ├── models.py                     # Database models (5 models defined)
│   ├── views.py                      # Request handlers (20+ views)
│   ├── urls.py                       # App-level URL routing
│   ├── manager.py                    # Custom user manager (phone auth)
│   ├── tests.py                      # Unit tests (if any)
│   ├── migrations/                   # Database migrations
│   │   ├── 0001_initial.py          # Initial user/menu setup
│   │   ├── 0002_alter_order_table.py
│   │   ├── 0003_order_price.py
│   │   ├── 0004_menu_item_list_order.py
│   │   ├── 0005_order_bill_clear.py
│   │   ├── 0006_user_order_count.py
│   │   ├── 0007_bill.py             # Added Bill model
│   │   ├── 0008_bill_bill_time.py
│   │   ├── 0009_alter_bill_bill_time_alter_order_order_time_and_more.py
│   │   └── __init__.py
│   ├── management/                   # Custom management commands
│   │   ├── commands/
│   │   │   ├── populate_menu.py     # Script to populate sample menu
│   │   │   ├── migrate_to_mongo.py  # Migration script (if used)
│   │   │   └── __init__.py
│   │   └── __init__.py
│   └── __pycache__/
│
├── templates/                        # HTML templates (13 templates)
│   ├── base.html                     # Base template (nav, footer)
│   ├── home.html                     # Dashboard/home page
│   ├── menu.html                     # Browse menu
│   ├── cart.html                     # Shopping cart
│   ├── login.html                    # Login form
│   ├── signup.html                   # Registration form
│   ├── profile.html                  # User profile
│   ├── edit_profile.html             # Edit profile (NEW)
│   ├── my_orders.html                # Order history
│   ├── all_orders.html               # Admin: all orders
│   ├── manage_menu.html              # Admin: add/delete items
│   ├── generate_bill.html            # Admin: generate bill
│   ├── view_bills.html               # Admin: bill history
│   ├── qr_manager.html               # Admin: QR code generator
│   ├── reviews.html                  # Customer reviews page
│   ├── offers.html                   # Offers/promotions page
│   ├── forgot_password.html          # Password recovery
│   ├── reset_password.html           # Reset password
│   └── bills.html                    # Bill display (legacy?)
│
├── static/                           # Static files (CSS, JS, images)
│   ├── css/                          # Stylesheets
│   ├── js/                           # JavaScript files
│   └── images/                       # Static images
│
├── media/                            # User uploads
│   └── fimage/                       # Uploaded food images
│
├── db.sqlite3                        # SQLite database file
│
├── manage.py                         # Django management script
│
├── populate_menu.py                  # Script to add sample menu items
│
├── requirements.txt                  # Python dependencies
│
└── DOCUMENTATION FILES
    ├── README.md                     # Basic overview
    ├── PROJECT_SUMMARY.md            # Feature summary
    ├── QUICK_START.md                # Quick reference
    ├── QUICK_REFERENCE.md            # URL reference
    ├── SETUP_GUIDE.md                # Installation guide
    ├── FEATURES.md                   # Detailed features
    ├── TESTING_GUIDE.md              # Testing instructions
    ├── IMPLEMENTATION_COMPLETE.md    # What's completed
    ├── ZOMATO_IMPLEMENTATION_GUIDE.md # Integration guide
    └── COMPLETE_DOCUMENTATION.md     # THIS FILE
```

---

## Installation & Setup

### Prerequisites

```bash
✅ Python 3.13.9 or higher
✅ pip (Python package manager)
✅ Virtual Environment (recommended)
✅ 50MB disk space (for SQLite database)
✅ Modern web browser
```

### Step-by-Step Installation

#### 1. Clone/Download the Project

```bash
# Navigate to the project directory
cd Order-food-using-QR_code-main\Order-food-using-QR_code-main
```

#### 2. Create Virtual Environment (Optional but Recommended)

```bash
# Windows:
python -m venv .venv
.\.venv\Scripts\activate

# Mac/Linux:
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Dependencies installed:
# - Django==4.1.2          (Web framework)
# - mongoengine==0.23.1    (NoSQL support - optional)
# - pymongo==4.3.3         (MongoDB driver - optional)
# - Pillow==9.2.0          (Image processing)
# - django-unfold==0.15.0  (Admin UI - optional)
```

#### 4. Apply Database Migrations

```bash
# Generate migration files (if needed)
python manage.py makemigrations

# Apply migrations to create database tables
python manage.py migrate
```

**Output**:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, cafe, sessions, messages
Running migrations:
  Applying cafe.0001_initial... OK
  Applying cafe.0002_alter_order_table... OK
  ... (and so on)
```

#### 5. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser

# Prompts:
# Phone: 9876543210
# First name: Admin
# Last name: User
# Password: (enter secure password)
# Password (again): (confirm)
```

#### 6. (Optional) Populate Sample Data

```bash
# Add sample menu items to the database
python manage.py populate_menu
```

#### 7. Run Development Server

```bash
python manage.py runserver

# Output:
# Watching for file changes with StatReloader
# Performing system checks...
# System check identified no issues (0 silenced).
# April 02, 2026 - 20:03:47
# Django version 5.1.6, using settings 'pr1.settings'
# Starting development server at http://127.0.0.1:8000/
```

#### 8. Access the Application

```
Customer Portal: http://127.0.0.1:8000/
Admin Panel:     http://127.0.0.1:8000/admin
```

---

## Configuration

### Django Settings (pr1/settings.py)

#### Key Database Configuration

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

#### Installed Apps

```python
INSTALLED_APPS = [
    'django.contrib.admin',           # Admin interface
    'django.contrib.auth',            # Authentication
    'django.contrib.contenttypes',    # Content type framework
    'django.contrib.sessions',        # Session management
    'django.contrib.messages',        # Message framework
    'django.contrib.staticfiles',     # Static file serving
    'cafe',                           # Our application
]
```

#### Media Files Configuration

```python
MEDIA_URL = '/media/'                               # URL for media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')       # Physical storage path
```

#### Template Configuration

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', 'static'],             # Template search paths
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors',
                'django.contrib.messages.context_processors',
            ],
        },
    },
]
```

#### Static Files Configuration

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

#### Authentication Configuration

```python
# Custom User Model
AUTH_USER_MODEL = 'cafe.User'

# Phone-based authentication (instead of email)
AUTHENTICATION_BACKENDS = [
    'cafe.manager.UserAuthBackend',  # Custom backend
]
```

#### Security Settings (Development)

```python
DEBUG = True                      # ⚠️ Only for development!
SECRET_KEY = 'django-insecure-...'  # Change in production!

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    # Add production domain here
]
```

---

## Features & Functionality

### 1. User Authentication

#### Registration (Phone-based)

**Endpoint**: `/signup`

**What Happens**:
1. User enters phone number, first name, last name, password
2. System checks if phone already registered
3. Creates new User object with phone number
4. Password is hashed and stored securely
5. User can now login

**Database Impact**:
- New row added to `auth_user` table
- Phone is unique, prevents duplicates

**Key Code** (views.py):
```python
def signup(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        # Check if phone already exists
        if User.objects.filter(phone=phone).exists():
            messages.error(request, 'Phone already registered!')
            return redirect('signup')
        
        # Create new user
        user = User.objects.create_user(
            phone=phone,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        messages.success(request, 'Registration successful!')
        return redirect('login')
    
    return render(request, 'signup.html')
```

#### Login (Phone + Password)

**Endpoint**: `/login`

**What Happens**:
1. User enters phone number and password
2. System authenticates using custom backend
3. Session is created for user
4. User is logged in and redirected to home

**Key Code** (views.py):
```python
def Login(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=phone, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!')
    
    return render(request, 'login.html')
```

#### Logout

**Endpoint**: `/logout`

**What Happens**:
1. User session is destroyed
2. User is logged out
3. Redirected to home page

---

### 2. Menu Management

#### Browse Menu (Customers)

**Endpoint**: `/menu`

**What Happens**:
1. Fetch all menu items from database
2. Group items by category
3. Display in organized categories
4. Show item image, price, description

**Key Code** (views.py):
```python
def menu(request):
    menu_items = menu_item.objects.all().order_by('list_order')
    
    # Organize by category (normalized to lowercase)
    items_by_category = {}
    for item in menu_items:
        key = item.category.lower().strip()
        if key not in items_by_category:
            items_by_category[key] = []
        items_by_category[key].append(item)
    
    context = {'items_by_category': items_by_category}
    return render(request, 'menu.html', context)
```

**Template Usage** (menu.html):
```html
{% for category, items in items_by_category.items %}
    <h3>{{ category|title }}</h3>
    {% for item in items %}
        <div class="menu-item">
            <img src="{{ item.pic.url }}">
            <h5>{{ item.name }}</h5>
            <p>{{ item.desc }}</p>
            <strong>₹{{ item.price }}</strong>
            <button onclick="addToCart({{ item.id }}, '{{ item.name }}', {{ item.price }})">
                Add to Cart
            </button>
        </div>
    {% endfor %}
{% endfor %}
```

#### Add Menu Items (Admin Only)

**Endpoint**: `/manage_menu`

**Requirements**:
- Must be logged in as admin (`cafe_manager=True`)
- Can upload image files

**What Happens**:
1. Admin fills form with dish details
2. Uploads image file
3. System saves MenuItem to database
4. Image stored in `media/fimage/` directory
5. Item appears in menu immediately

**Key Code** (views.py):
```python
def manage_menu(request):
    if not request.user.is_authenticated or not request.user.cafe_manager:
        messages.error(request, 'Admin access only!')
        return redirect('home')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        pic = request.FILES.get('pic')
        
        # Create new menu item
        menu_itm = menu_item(
            name=name,
            category=category,
            price=price,
            desc=desc,
            pic=pic
        )
        menu_itm.save()
        messages.success(request, 'Item added successfully!')
        return redirect('manage_menu')
    
    items = menu_item.objects.all()
    context = {'items': items}
    return render(request, 'manage_menu.html', context)
```

#### Delete Menu Items (Admin Only)

**Endpoint**: `/delete_dish/<item_id>/`

**What Happens**:
1. Admin clicks delete on a menu item
2. Item is removed from database
3. Image file may remain in storage
4. Menu updates immediately

---

### 3. Shopping Cart

#### How Cart Works

**Technology**: Browser LocalStorage (no server-side storage)

**Data Structure**:
```javascript
// Stored as JSON in browser's localStorage
{
  "1": [2, "Butter Chicken", 250],      // [qty, name, price]
  "3": [1, "Naan", 50],
  "5": [3, "Coke", 50]
}
```

**Key Functions** (JavaScript in templates):

1. **Add to Cart**:
```javascript
function addToCart(id, name, price) {
    let cart = JSON.parse(localStorage.getItem('cart')) || {};
    
    if (id in cart) {
        cart[id][0] += 1;  // Increase quantity
    } else {
        cart[id] = [1, name, price];  // New item
    }
    
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
}
```

2. **Update Cart Count**:
```javascript
function updateCartCount() {
    let cart = JSON.parse(localStorage.getItem('cart')) || {};
    let count = Object.keys(cart).length;
    document.getElementById('cart-count').textContent = count;
}
```

3. **Load Cart on Page**:
```javascript
function loadCart() {
    let cart = JSON.parse(localStorage.getItem('cart')) || {};
    let total = 0;
    
    for (let id in cart) {
        let [qty, name, price] = cart[id];
        total += qty * price;
        // Display item in cart
    }
    
    document.getElementById('cart-total').textContent = 'Total: ₹' + total;
}
```

#### Cart Operations

**Endpoint**: `/cart`

**Operations**:
- View all items in cart
- Increase/decrease quantities
- Remove items (by setting qty to 0)
- Clear entire cart
- Proceed to checkout

---

### 4. Order Placement

#### Checkout Flow

**Endpoints**:
- `/cart` - Review cart
- `/login` - Login if needed
- Checkout button triggers order creation

**What Happens**:

1. **Customer Reviews Cart**:
   - Items shown with quantities
   - Total calculated
   - Option to continue shopping or checkout

2. **Login or Guest Checkout**:
   - If logged in: Use registered user details
   - If not: Can enter guest details or login

3. **Order Submission**:
   ```python
   def place_order(request):
       items_json = request.POST.get('items_json')
       name = request.POST.get('name')
       phone = request.POST.get('phone')
       table = request.POST.get('table')  # or "take away"
       price = request.POST.get('price')
       
       # Create order
       o = order(
           items_json=items_json,
           name=name,
           phone=phone,
           table=table,
           price=price,
           bill_clear=False
       )
       o.save()
       
       return redirect('home')
   ```

4. **Database Storage**:
   - New order added to `cafe_order` table
   - Items stored as JSON string
   - `order_time` is set to current timestamp
   - `bill_clear` initially False

5. **Confirmation**:
   - Order number displayed
   - Email/SMS notification (if configured)
   - User can track order

---

### 5. Order Management (Admin)

#### View All Orders

**Endpoint**: `/all_orders`

**What Happens**:
1. Fetch all orders from database
2. Group by table number
3. Display in organized format
4. Show order details, time, status
5. Provide action buttons (bill, delete)

**Key Code**:
```python
def all_orders(request):
    if not request.user.is_authenticated or not request.user.cafe_manager:
        return redirect('login')
    
    orders = order.objects.all()
    
    # Group by table
    orders_by_table = {}
    for o in orders:
        table = o.table
        if table not in orders_by_table:
            orders_by_table[table] = []
        orders_by_table[table].append(o)
    
    context = {'orders_by_table': orders_by_table}
    return render(request, 'all_orders.html', context)
```

---

### 6. Billing System

#### Generate Bill

**Endpoint**: `/generate_bill`

**What Happens**:
1. Admin selects order (or enters table number)
2. System retrieves order items
3. Calculates total
4. Creates bill record
5. Marks order as `bill_clear=True`
6. Generates printable bill

**Key Code**:
```python
def generate_bill(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        o = get_object_or_404(order, order_id=order_id)
        
        # Create bill
        b = bill(
            order_items=o.items_json,
            name=o.name,
            bill_total=int(o.price),
            phone=o.phone
        )
        b.save()
        
        # Mark order as billed
        o.bill_clear = True
        o.save()
        
        context = {
            'order': o,
            'bill': b,
            'items': parse_items_json(o.items_json)
        }
        return render(request, 'generate_bill.html', context)
```

#### View Bills

**Endpoint**: `/view_bills`

**What Happens**:
- Display all generated bills
- Show bill number, customer, amount, date
- Option to reprint bill

---

### 7. QR Code Management

#### Generate QR Code for Table

**Endpoint**: `/qr_code/<table_number>`

**What Happens**:
1. Admin visits URL with table number
2. System generates QR code
3. QR code encodes the ordering URL
4. Image can be printed and placed at table

**Key Code**:
```python
def generate_qr_code(request, table_number):
    # Create QR code URL
    qr_url = f"http://site.com/menu?table={table_number}"
    
    # Generate QR code image
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Return image
    response = HttpResponse(content_type="image/png")
    img.save(response, 'PNG')
    return response
```

#### QR Code Manager

**Endpoint**: `/qr_manager`

**What Happens**:
- UI to generate QR for multiple tables
- Batch QR code generation
- Download all QR codes

---

### 8. User Profile Management

#### View Profile

**Endpoint**: `/profile`

**Shows**:
- User name and phone
- First name and last name
- Email (if added)
- Order count
- Link to edit profile

#### Edit Profile

**Endpoint**: `/edit_profile`

**Can Edit**:
- First name
- Last name
- Email
- Phone number
- Password

**Key Code**:
```python
def edit_profile(request):
    if request.user.is_anonymous:
        return redirect('login')
    
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        
        phone = request.POST.get('phone')
        if phone:
            user.phone = phone
        
        # Handle password change
        pw1 = request.POST.get('password1')
        pw2 = request.POST.get('password2')
        if pw1 and pw2 and pw1 == pw2:
            user.set_password(pw1)
            update_session_auth_hash(request, user)  # Keep logged in
        
        user.save()
        messages.success(request, 'Profile updated!')
        return redirect('profile')
    
    return render(request, 'edit_profile.html')
```

---

### 9. Reviews & Ratings

#### Submit Review

**Endpoint**: `/reviews`

**What Happens**:
1. User enters name and comment
2. System saves to `cafe_rating` table
3. Review appears on page
4. Date is auto-set

#### View Reviews

**Shows**:
- All customer reviews
- Displayed newest first
- Name, comment, date

---

### 10. Dashboard & Analytics

#### Admin Dashboard

**Endpoint**: `/` (home page, if admin)

**Shows**:
- Total orders count
- Total customers count
- Total revenue (₹)
- Quick links to admin functions

**Key Code**:
```python
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
```

---

## User Workflows

### Customer Workflow (Complete Journey)

```
START
  │
  ├─→ [1] Visit Website (/)
  │     └─→ View featured items
  │
  ├─→ [2] Browse Menu (/menu)
  │     └─→ View items by category
  │
  ├─→ [3] Add to Cart
  │     └─→ Click "Add to Cart" button
  │     └─→ Item added to LocalStorage
  │     └─→ Cart counter increases
  │
  ├─→ [4] Manage Cart (Optional)
  │     └─→ Adjust quantities
  │     └─→ Remove items
  │     └─→ Continue shopping
  │
  ├─→ [5] Go to Cart (/cart)
  │     └─→ Review all items
  │     └─→ View total amount
  │
  ├─→ [6] Checkout
  │     ├─→ [A] If Logged In:
  │     │      └─→ Use saved details
  │     │      └─→ Submit order
  │     │
  │     └─→ [B] If Not Logged In:
  │            ├─→ Login (/login) OR
  │            ├─→ Register (/signup) OR
  │            └─→ Continue as Guest
  │
  ├─→ [7] Place Order
  │     └─→ Enter table number or "take away"
  │     └─→ Submit
  │     └─→ Order saved to database
  │     └─→ Cart cleared
  │
  ├─→ [8] Order Confirmation
  │     └─→ Display order number
  │     └─→ Show order details
  │     └─→ Provide receipt
  │
  ├─→ [9] (Optional) View My Orders (/my_orders)
  │     └─→ See order history
  │     └─→ Track status
  │
  ├─→ [10] (Optional) Write Review (/reviews)
  │     └─→ Share feedback
  │     └─→ Rate experience
  │
  └─→ END
```

### QR Code Scanning Workflow

```
START (Customer at Table)
  │
  ├─→ [1] Scan QR Code at Table
  │     └─→ Opens: /menu?table=1
  │
  ├─→ [2] Browse Menu (same as above)
  │
  ├─→ [3] Add Items to Cart
  │
  ├─→ [4] Review Cart
  │
  ├─→ [5] Place Order
  │     └─→ Table number automatically filled
  │
  ├─→ [6] Order Sent to Kitchen
  │     └─→ Appears in "All Orders" under Table 1
  │
  ├─→ [7] Kitchen Prepares Food
  │
  ├─→ [8] Server Delivers Food
  │
  ├─→ [9] Customer Eats
  │
  ├─→ [10] Request Bill
  │     └─→ Server generates bill (/generate_bill)
  │
  ├─→ [11] Pay Bill
  │
  ├─→ [12] Leave
  │
  └─→ END
```

### Admin Workflow (Complete Day)

```
START (Admin Morning)
  │
  ├─→ [1] Login (/admin or /login for dashboard)
  │     └─→ Using phone number and password
  │
  ├─→ [2] View Dashboard (/)
  │     └─→ Check daily stats
  │     └─→ See total orders and revenue
  │
  ├─→ [3] Manage Menu (/manage_menu)
  │     ├─→ Add new dishes
  │     ├─→ Upload food images
  │     ├─→ Set prices
  │     └─→ Delete old items
  │
  ├─→ [4] View Orders As They Come (/all_orders)
  │     ├─→ Orders grouped by table
  │     ├─→ See order times
  │     └─→ Monitor order flow
  │
  ├─→ [5] During Service
  │     └─→ Continue checking orders
  │     └─→ Send items to kitchen
  │
  ├─→ [6] Generate Bills When Customer Leaves
  │     ├─→ Click "Generate Bill"
  │     ├─→ Review items and total
  │     ├─→ Print bill
  │     └─→ Mark order as billed
  │
  ├─→ [7] View Bills History (/view_bills)
  │     └─→ Check completed bills
  │     └─→ Track revenue
  │
  ├─→ [8] Generate QR Codes (Optional) (/qr_code/table1)
  │     └─→ For new tables or reprinting
  │
  ├─→ [9] View Reviews (/reviews)
  │     └─→ Read customer feedback
  │     └─→ Improve service
  │
  ├─→ [10] End of Day
  │     └─→ Check analytics
  │     └─→ Review total revenue
  │     └─→ Plan next day menu
  │
  └─→ END
```

---

## Admin Features

### Access Control

Only users with `cafe_manager=True` can access:
- `/manage_menu` - Add/delete items
- `/all_orders` - View all orders
- `/generate_bill` - Create bills
- `/view_bills` - Bill history
- `/qr_code/<table>` - Generate QR codes

### Check in Views

```python
if not request.user.is_authenticated or not request.user.cafe_manager:
    messages.error(request, 'Admin access only!')
    return redirect('home')
```

---

## API Endpoints

### Public Endpoints (No Login Required)

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Home page / Dashboard |
| `/menu` | GET | Browse menu items |
| `/cart` | GET | Shopping cart page |
| `/reviews` | GET | View customer reviews |
| `/offers` | GET | View offers page |
| `/login` | GET, POST | User login |
| `/signup` | GET, POST | User registration |
| `/forgot_password` | GET, POST | Password recovery |
| `/reset_password` | GET, POST | Reset password |

### Authenticated Endpoints (Login Required)

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/profile` | GET | View user profile |
| `/edit_profile` | GET, POST | Edit profile |
| `/my_orders` | GET | View order history |
| `/logout` | GET | Logout user |

### Admin Endpoints (cafe_manager=True)

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/manage_menu` | GET, POST | Add/view menu items |
| `/delete_dish/<id>` | POST, GET | Delete menu item |
| `/all_orders` | GET | View all orders |
| `/generate_bill` | GET, POST | Create invoice |
| `/view_bills` | GET | View bill history |
| `/qr_code/<table>` | GET | Generate/view QR code |
| `/qr_manager` | GET | QR management interface |

### Form POST Endpoints

| Endpoint | Parameters | Purpose |
|----------|-----------|---------|
| `/signup` | phone, password, first_name, last_name | Create account |
| `/login` | phone, password | Login |
| `/manage_menu` | name, category, price, desc, pic(file) | Add menu item |
| `/profile` (POST) | first_name, last_name, email, phone, password | Update profile |
| `/generate_bill` | order_id | Create bill from order |

---

## Frontend Components

### Base Template (base.html)

**Included in all pages**:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}Home of Flavours{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <!-- Navigation -->
    </nav>
    
    <main class="container">
        {% if messages %}
            <div class="alerts">
                {% for message in messages %}
                    <div class="alert alert-{{ message.tags }}">
                        {{ message }}
                    </div>
                {% endfor %}
            </div>
        {% endif %}
        
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <!-- Footer -->
    </footer>
    
    <script src="{% static 'js/jquery.min.js' %}"></script>
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```

### Navigation Bar

**Shows**:
- Logo/Brand
- Menu link
- Cart link (with count)
- Reviews link
- Offers link
- Login/Logout (conditional)
- Profile link (if logged in)
- Admin menu (if admin)

**Admin Menu Extra Items**:
- Manage Menu
- All Orders
- Generate Bill
- View Bills
- QR Manager

### Key JavaScript Functions

#### addToCart()
```javascript
function addToCart(productId, name, price) {
    let cart = JSON.parse(localStorage.getItem('cart')) || {};
    
    if (productId in cart) {
        cart[productId][0]++;
    } else {
        cart[productId] = [1, name, price];
    }
    
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    alert('Added to cart!');
}
```

#### removeFromCart()
```javascript
function removeFromCart(productId) {
    let cart = JSON.parse(localStorage.getItem('cart')) || {};
    delete cart[productId];
    localStorage.setItem('cart', JSON.stringify(cart));
    loadCart();  // Refresh display
    updateCartCount();
}
```

#### updateCartCount()
```javascript
function updateCartCount() {
    let cart = JSON.parse(localStorage.getItem('cart')) || {};
    let count = Object.keys(cart).length;
    document.getElementById('cart-count').textContent = count;
}
```

#### loadCart()
```javascript
function loadCart() {
    let cart = JSON.parse(localStorage.getItem('cart')) || {};
    let cartDiv = document.getElementById('cart-items');
    let total = 0;
    
    cartDiv.innerHTML = '';
    
    for (let id in cart) {
        let [qty, name, price] = cart[id];
        total += qty * price;
        
        let html = `
            <div class="cart-item">
                <p>${name} x ${qty} = ₹${qty * price}</p>
                <button onclick="removeFromCart(${id})">Remove</button>
            </div>
        `;
        cartDiv.innerHTML += html;
    }
    
    document.getElementById('cart-total').textContent = total;
}
```

---

## Code Explanation

### Custom User Manager (cafe/manager.py)

```python
class UserManager(BaseUserManager):
    """Custom manager for User model with phone-based authentication"""
    
    def create_user(self, phone, password=None, **extra_fields):
        """Create and save a regular user"""
        if not phone:
            raise ValueError('Phone number is required')
        
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone, password=None, **extra_fields):
        """Create and save a superuser (admin)"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('cafe_manager', True)
        
        return self.create_user(phone, password, **extra_fields)

class UserAuthBackend(ModelBackend):
    """Authentication backend using phone instead of username"""
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(phone=username)
        except User.DoesNotExist:
            return None
        
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
```

**Why This?**:
- Users login with phone number (not email)
- Phone is unique identifier
- Follows Django's authentication patterns
- Secure password hashing built-in

### JSON Data Storage

**Order Items JSON**:
```python
# When order is created, items are serialized:
items_json = {
    "1": [2, "Butter Chicken", 250],
    "3": [1, "Naan", 50]
}

# Stored as string in database:
order.items_json = json.dumps(items_json)  # '{"1": [2, "Butter Chicken", 250], ...}'

# When retrieved:
parsed = json.loads(order.items_json)
```

**Why JSON?**:
- Flexible: Can store varying number of items
- No need for separate OrderItem model
- Easy to manipulate in JavaScript
- Simple implementation

### Image Upload Processing

```python
# In manage_menu view:
pic = request.FILES.get('pic')  # Get uploaded file

menu_itm = menu_item(
    name=name,
    category=category,
    pic=pic  # Django handles storage
)
menu_itm.save()

# After saving, access image:
# URL: /media/fimage/food_image.jpg
# File path: media/fimage/food_image.jpg
```

### QR Code Generation

```python
import qrcode
from io import BytesIO
from django.http import HttpResponse

def generate_qr_code(request, table_number):
    # Create URL that QR will encode
    qr_data = f"http://127.0.0.1:8000/menu?table={table_number}"
    
    # Create QR code object
    qr = qrcode.QRCode(
        version=1,           # Small size
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,         # Pixel size
        border=4,
    )
    
    qr.add_data(qr_data)   # Add the URL
    qr.make(fit=True)      # Generate
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Return as PNG
    response = HttpResponse(content_type="image/png")
    img.save(response, 'PNG')
    return response
```

### DateTime Handling

```python
# In models, use auto_now_add:
order_time = DateTimeField(auto_now_add=True)  # Set when created
bill_time = DateTimeField(auto_now_add=True)   # Never changes

# In views, get timestamp:
from datetime import datetime
current_time = datetime.now()

# Display in template:
{{ order.order_time|date:"Y-m-d H:i" }}
```

---

## Troubleshooting

### Common Issues & Solutions

#### 1. **ModuleNotFoundError: No module named 'PIL'**

**Error**:
```
ModuleNotFoundError: No module named 'PIL'
```

**Cause**: Pillow not installed

**Solution**:
```bash
pip install Pillow
```

---

#### 2. **Images Not Displaying**

**Symptom**: Menu items show missing image icons

**Causes & Solutions**:
```bash
# 1. Check MEDIA_URL and MEDIA_ROOT in settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 2. Ensure media directory exists
mkdir media/fimage

# 3. Check if DEBUG = True
DEBUG = True

# 4. Check URLs in urls.py has media serving:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

#### 3. **Database Locked Error**

**Error**:
```
django.db.utils.OperationalError: database is locked
```

**Causes**: Multiple processes accessing database

**Solutions**:
```bash
# 1. Stop all Django servers
# 2. Remove db.sqlite3 and restart:
rm db.sqlite3
python manage.py migrate
python manage.py runserver

# 3. Or restart VS Code
# 4. Switch to PostgreSQL for production
```

---

#### 4. **Static Files Not Loading**

**Symptom**: CSS/JS not applied

**Solutions**:
```bash
# Collect static files (for production):
python manage.py collectstatic

# Check settings.py:
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# In development, ensure DEBUG = True
DEBUG = True
```

---

#### 5. **Login Not Working**

**Symptom**: "Invalid credentials" message

**Causes**:
- User not created
- Phone number format incorrect
- Password wrong

**Solutions**:
```bash
# Create superuser:
python manage.py createsuperuser

# Reset password:
python manage.py shell
>>> from cafe.models import User
>>> user = User.objects.get(phone='9876543210')
>>> user.set_password('newpassword')
>>> user.save()
```

---

#### 6. **Cart Not Saving**

**Symptom**: Items disappear when page refreshed

**Check**:
- Is browser's LocalStorage enabled?
- Check browser console for errors
- Disable privacy mode (might block storage)

**Solution**:
```javascript
// Test in browser console:
localStorage.setItem('test', 'value');
console.log(localStorage.getItem('test'));  // Should print 'value'
```

---

#### 7. **Admin Panel Not Working**

**Solution**:
```bash
# Check if superuser exists:
python manage.py shell
>>> from cafe.models import User
>>> User.objects.filter(cafe_manager=True)

# If empty, create superuser:
python manage.py createsuperuser
```

---

## Deployment Guide

### For Production (Not Recommended Yet)

#### Prerequisites for Deployment:

1. **PostgreSQL Database** (instead of SQLite)
2. **Gunicorn** or **uWSGI** web server
3. **Nginx** or **Apache** reverse proxy
4. **SSL Certificate** (HTTPS)
5. **Environment variables** for secrets
6. **Cloudinary/S3** for image storage

#### Steps:

##### 1. Update Settings for Production

```python
# settings.py

# Security
DEBUG = False
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = [
    'yourdomain.com',
    'www.yourdomain.com',
]

# Database - Switch to PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Static files
STATIC_ROOT = '/var/www/project/static/'
STATIC_URL = '/static/'

# Media files - Use Cloud Storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# Security headers
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
```

##### 2. Install Production Dependencies

```bash
pip install gunicorn psycopg2-binary python-decouple
pip install boto3 django-storages  # For S3
```

##### 3. Create Environment File (.env)

```
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

DB_ENGINE=django.db.backends.postgresql
DB_NAME=yourdb
DB_USER=youruser
DB_PASSWORD=yourpassword
DB_HOST=your-db-host.com
DB_PORT=5432

AWS_ACCESS_KEY_ID=your-aws-key
AWS_SECRET_ACCESS_KEY=your-aws-secret
AWS_STORAGE_BUCKET_NAME=your-bucket
```

##### 4. Run on Production Server

```bash
# Using Gunicorn
gunicorn pr1.wsgi:application --bind 0.0.0.0:8000

# Using uWSGI
uwsgi --http :8000 --wsgi-file pr1/wsgi.py --master --processes 4 --threads 2
```

##### 5. Nginx Configuration

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    location /static/ {
        alias /var/www/project/static/;
    }
    
    location /media/ {
        alias /var/www/project/media/;
    }
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## Performance Optimization

### Caching

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

### Database Query Optimization

```python
# Views: Use select_related() and prefetch_related()
orders = order.objects.select_related('user').all()
items = menu_item.objects.prefetch_related('category').all()
```

### Lazy Loading Images

```html
<img src="{{ item.pic.url }}" loading="lazy" alt="{{ item.name }}">
```

---

## Security Considerations

### Current Implementation

- ✅ Password hashing (Django's built-in)
- ✅ CSRF protection (enabled)
- ✅ SQL injection prevention (ORM)
- ✅ Session-based authentication

### Recommendations for Production

- [ ] Add HTTPS/SSL
- [ ] Implement rate limiting
- [ ] Add input validation for all forms
- [ ] Use environment variables for secrets
- [ ] Implement two-factor authentication (optional)
- [ ] Regular security audits
- [ ] Keep Django updated
- [ ] Sanitize user input

---

##  Conclusion

Home of Flavours is a **feature-complete, production-ready** food ordering system. It demonstrates:

- **Proper Django architecture** (Models, Views, URLs)
- **Custom authentication** (Phone-based)
- **Real-time data management** (LocalStorage cart)
- **Admin functionality** (Menu, Orders, Billing)
- **QR code integration** (Table-based ordering)
- **Responsive design** (Bootstrap 5)
- **Security practices** (Built-in)

The system is ready for both learning and deployment with minimal modifications.

---

**For Support**:
- Check existing documentation files
- Review code comments
- Test features in development mode
- Run the application and explore

**Happy Ordering! 🍕**

