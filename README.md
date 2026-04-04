# Home of Flavours - Food Ordering System Using QR Code

A complete food ordering website for restaurants and cafes with support for dine-in, takeaway, and QR code-based ordering.

## Features

### For Customers:
- ✅ Browse menu organized by categories
- ✅ Add items to cart with quantity management
- ✅ Place orders for dine-in or takeaway
- ✅ View order history and status
- ✅ Leave reviews and ratings
- ✅ User authentication with phone number

### For Admin/Manager:
- ✅ Dashboard with sales analytics
- ✅ Add new menu items with images
- ✅ Delete menu items
- ✅ View all orders by table
- ✅ Generate bills for each table
- ✅ Generate QR codes for tables
- ✅ View billing history

## Tech Stack

- **Backend**: Django 6.0.3
- **Frontend**: Bootstrap 5, jQuery
- **Database**: SQLite3
- **Image Processing**: Pillow
- **QR Code Generation**: qrcode

## Installation & Setup

### Prerequisites
- Python 3.14+
- pip
- Virtual Environment (venv)

### Step 1: Clone the Repository
```bash
cd Order-food-using-QR_code-main
```

### Step 2: Create & Activate Virtual Environment
```bash
python -m venv .venv
.\.venv\Scripts\activate  # On Windows
source .venv/bin/activate # On Mac/Linux
```

### Step 3: Install Dependencies
```bash
pip install django pillow qrcode
```

### Step 4: Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Admin)
```bash
python manage.py createsuperuser
# Enter phone number as USERNAME_FIELD
# Example: 9876543210
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

Server will run at: **http://127.0.0.1:8000/**

## Usage

### For Admin:
1. Go to http://127.0.0.1:8000/admin
2. Login with your credentials
3. Add menu items via "Manage Menu"
4. Monitor orders from "All Orders"
5. Generate bills when service is complete
6. View analytics on the dashboard

### For Customers:
1. Visit http://127.0.0.1:8000/
2. Browse menu items by category
3. Add items to cart
4. Click "Go to Cart" and review order
5. Login or continue as guest
6. Place order
7. View order history in "My Orders"

### QR Code Ordering:
1. Admin generates QR codes for each table
2. QR code links to: `http://site.com/menu?table=1`
3. Customers scan and order
4. Orders appear in "All Orders" by table

## Project Structure

```
Order-food-using-QR_code-main/
├── cafe/                    # Main app
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── urls.py            # URL routing
│   ├── manager.py         # Custom user manager
│   └── migrations/        # Database migrations
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── menu.html         # Menu page
│   ├── cart.html         # Shopping cart
│   ├── login.html        # Login page
│   ├── my_orders.html    # Customer orders
│   ├── all_orders.html   # Admin orders
│   └── ...
├── static/               # CSS, JS, images
├── pr1/                 # Project settings
│   ├── settings.py     # Django settings
│   ├── urls.py        # Project URLs
│   └── wsgi.py        # WSGI config
├── manage.py          # Django management
└── db.sqlite3        # Database file
```

## Models

### User Model
- Extends AbstractUser
- Phone-based authentication
- Tracks order count
- Admin/Manager role support

### MenuItem Model
- Name, category, description
- Image upload
- Price
- Display order

### Order Model
- Items JSON (stored as string)
- Customer details
- Table number
- Total price
- Bill status

### Rating Model
- Customer reviews
- Comments
- Timestamps

### Bill Model
- Invoice tracking
- Bill details
- Total amount
- Customer info

## Admin Credentials

Default admin account (if created):
- **Phone**: (Your entered phone number)
- **Password**: (Your entered password)

## Features In Detail

### 1. Menu Management
- Add items with image upload
- Organize by categories
- Set pricing
- Delete items

### 2. Order Management
- View orders by table
- Real-time tracking
- Quantity updates
- Order time tracking

### 3. Billing System
- Generate bills by table
- Calculate totals
- Print invoice
- Store billing history

### 4. QR Code Feature
- Generate table-specific QR codes
- Direct customers to menu
- Track orders by table
- Simplifies ordering process

### 5. Customer Features
- Browse categorized menu
- Add to cart
- Order history
- Write reviews
- Profile management

## Notes

- Uses SQLite for simplicity (can be upgraded to PostgreSQL)
- Images stored in `/media/fimage/` directory
- Local storage used for cart management
- Phone-based authentication for unique identification
- Bootstrap 5 for responsive design

## Future Enhancements

- Payment integration (Stripe/Razorpay)
- Order status push notifications
- Email/SMS notifications
- Table reservation system
- Multi-language support
- Mobile app development
- Analytics dashboard improvements
- API development (REST/GraphQL)

## Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

### Migration Errors
```bash
python manage.py migrate --fake
python manage.py makemigrations
python manage.py migrate
```

## Support

For issues or questions, please check the existing code or create an issue in the repository.

---

**Happy Ordering! 🍔🍕🍜**
