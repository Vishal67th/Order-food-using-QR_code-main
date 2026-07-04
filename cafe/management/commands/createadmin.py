from django.core.management.base import BaseCommand
from cafe.models import User


class Command(BaseCommand):
    help = "Create default admin user"

    def handle(self, *args, **kwargs):

        phone = "1234567890"
        password = "Admin@123"

        if User.objects.filter(phone=phone).exists():
            self.stdout.write(self.style.SUCCESS("Admin already exists."))
            return

        User.objects.create_superuser(
            phone=phone,
            password=password,
            first_name="Admin",
            last_name="User",
        )

        self.stdout.write(self.style.SUCCESS("Admin created successfully!"))
