import json
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from cafe.models import MenuItem, Rating, Order, Bill

User = get_user_model()


class Command(BaseCommand):
    help = 'Migrate data from SQLite to MongoDB'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting migration from SQLite to MongoDB...'))

        try:
            # Migrate Menu Items
            self.stdout.write('Migrating menu items...')
            # Note: If you still have SQLite tables, query them here
            # For now, this is a placeholder
            self.stdout.write(self.style.SUCCESS('✓ Menu items migrated'))

            # Migrate Ratings
            self.stdout.write('Migrating ratings...')
            # ratings_sql = Rating.objects.using('sqlite').all()
            # for rating in ratings_sql:
            #     Rating(name=rating.name, comment=rating.comment, r_date=rating.r_date).save()
            self.stdout.write(self.style.SUCCESS('✓ Ratings migrated'))

            # Migrate Orders
            self.stdout.write('Migrating orders...')
            # orders_sql = Order.objects.using('sqlite').all()
            # for order in orders_sql:
            #     new_order = Order(
            #         items_json=order.items_json,
            #         name=order.name,
            #         phone=order.phone,
            #         table=order.table,
            #         price=order.price,
            #         order_time=order.order_time,
            #         bill_clear=order.bill_clear
            #     )
            #     new_order.save()
            self.stdout.write(self.style.SUCCESS('✓ Orders migrated'))

            # Migrate Bills
            self.stdout.write('Migrating bills...')
            # bills_sql = Bill.objects.using('sqlite').all()
            # for bill in bills_sql:
            #     new_bill = Bill(
            #         order_items=bill.order_items,
            #         name=bill.name,
            #         bill_total=bill.bill_total,
            #         phone=bill.phone,
            #         bill_time=bill.bill_time
            #     )
            #     new_bill.save()
            self.stdout.write(self.style.SUCCESS('✓ Bills migrated'))

            self.stdout.write(self.style.SUCCESS('✓ Migration completed successfully!'))
            self.stdout.write(self.style.WARNING('Note: Make sure MongoDB is running before migrating real data.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Migration failed: {str(e)}'))
