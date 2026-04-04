import os
from django.core.management.base import BaseCommand
from django.conf import settings
from cafe.models import menu_item
from difflib import SequenceMatcher


class Command(BaseCommand):
    help = 'Improved image matching with better name normalization'

    def normalize_name(self, name):
        """Normalize names: lowercase, remove spaces, handle common variations"""
        name = name.lower()
        # Remove common words that might differ
        name = name.replace(' ', '_')
        name = name.replace('-', '_')
        return name

    def handle(self, *args, **options):
        media_root = settings.MEDIA_ROOT
        image_folder = os.path.join(media_root, 'fimage')

        if not os.path.exists(image_folder):
            self.stdout.write(self.style.ERROR(f'Image folder not found: {image_folder}'))
            return

        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        
        # Show all paneer, pizza, and beverage items
        paneer_items = menu_item.objects.filter(category__icontains='paneer')
        pizza_items = menu_item.objects.filter(category__icontains='pizza')
        beverage_items = menu_item.objects.filter(category__icontains='beverages')

        self.stdout.write(self.style.WARNING('\n=== PANEER ITEMS ==='))
        for item in paneer_items:
            status = '✓ HAS IMAGE' if item.pic else '✗ MISSING'
            self.stdout.write(f'{status}: {item.name} (pic: {item.pic})')

        self.stdout.write(self.style.WARNING('\n=== PIZZA ITEMS ==='))
        for item in pizza_items:
            status = '✓ HAS IMAGE' if item.pic else '✗ MISSING'
            self.stdout.write(f'{status}: {item.name} (pic: {item.pic})')

        self.stdout.write(self.style.WARNING('\n=== BEVERAGE ITEMS ==='))
        for item in beverage_items:
            status = '✓ HAS IMAGE' if item.pic else '✗ MISSING'
            self.stdout.write(f'{status}: {item.name} (pic: {item.pic})')

        # Now try matching with lower threshold
        self.stdout.write(self.style.WARNING('\n\n=== ATTEMPTING MATCHES (Score >= 30%) ==='))
        
        all_items = menu_item.objects.filter(pic='')
        matched_count = 0

        for item in all_items:
            best_match = None
            best_score = 0.3  # Lower threshold

            item_name_normalized = self.normalize_name(item.name)

            for image_file in image_files:
                filename_without_ext = os.path.splitext(image_file)[0]
                image_name_normalized = self.normalize_name(filename_without_ext)
                
                similarity = SequenceMatcher(None, item_name_normalized, image_name_normalized).ratio()
                
                if similarity > best_score:
                    best_score = similarity
                    best_match = image_file

            if best_match:
                image_path = f'fimage/{best_match}'
                item.pic = image_path
                item.save()
                matched_count += 1
                category = item.category if item.category else 'Unknown'
                self.stdout.write(
                    self.style.SUCCESS(f'✓ [{category}] {item.name} → {best_match} ({best_score:.0%})')
                )

        self.stdout.write(f'\n{self.style.SUCCESS(f"Success: {matched_count} items matched!")}')