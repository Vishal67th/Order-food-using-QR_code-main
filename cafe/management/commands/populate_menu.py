from django.core.management.base import BaseCommand
from cafe.models import MenuItem

class Command(BaseCommand):
    help = 'Populate menu items in the database'

    def handle(self, *args, **options):
        items = [
            ('Hyderabadi Chicken Biryani', 'Authentic Hyderabadi biryani with tender chicken', 'Biryani', 250),
            ('Mutton Biryani', 'Slow-cooked mutton biryani with aromatic spices', 'Biryani', 300),
            ('Vegetable Biryani', 'Colorful vegetable biryani with seasonal vegetables', 'Biryani', 180),
            ('Butter Chicken', 'Creamy butter chicken with tomato-based gravy', 'Curry', 220),
            ('Paneer Tikka Masala', 'Soft paneer in premium masala sauce', 'Curry', 210),
            ('Chicken Tikka Masala', 'Succulent chicken in creamy tomato sauce', 'Curry', 230),
            ('Dal Makhni', 'Black lentils cooked with butter and cream', 'Curry', 150),
            ('Chole Bhature', 'Fluffy bhature with spiced chickpeas', 'Curry', 140),
            ('Butter Naan', 'Soft naan bread brushed with butter', 'Bread', 50),
            ('Garlic Naan', 'Aromatic garlic naan with fresh garlic', 'Bread', 60),
            ('Tandoori Roti', 'Traditional Indian roti', 'Bread', 30),
            ('Paratha', 'Flaky layered Indian bread', 'Bread', 80),
            ('Mango Lassi', 'Refreshing yogurt-based mango drink', 'Beverage', 70),
            ('Sweet Lassi', 'Chilled yogurt drink with honey', 'Beverage', 60),
            ('Iced Tea', 'Cold brewed tea with lemon', 'Beverage', 40),
            ('Fresh Lime Soda', 'Refreshing lime juice with soda', 'Beverage', 50),
            ('Gulab Jamun', 'Sweet fried dough balls in sugar syrup', 'Dessert', 90),
            ('Kheer', 'Rice pudding with milk and nuts', 'Dessert', 80),
            ('Rasgulla', 'Soft cottage cheese balls in sugar syrup', 'Dessert', 100),
            ('Samosa', 'Crispy pastry filled with spiced potatoes', 'Curry', 35),
        ]

        count = 0
        for name, desc, category, price in items:
            if not MenuItem.objects.filter(name=name).exists():
                MenuItem.objects.create(name=name, desc=desc, category=category, price=price)
                self.stdout.write(self.style.SUCCESS(f'✓ Added: {name}'))
                count += 1
            else:
                self.stdout.write(f'- Skipped: {name} (already exists)')

        self.stdout.write(self.style.SUCCESS(f'\n✓ Total items added: {count}'))
        self.stdout.write(self.style.SUCCESS(f'✓ Total menu items in database: {MenuItem.objects.count()}'))
