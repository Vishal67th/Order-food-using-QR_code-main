import os
from django.core.management.base import BaseCommand
from django.conf import settings
from cafe.models import menu_item
from difflib import SequenceMatcher


class Command(BaseCommand):
    help = 'Automatically match food items with images in media/fimage/'

    def handle(self, *args, **options):
        media_root = settings.MEDIA_ROOT
        image_folder = os.path.join(media_root, 'fimage')

        # Get all image files
        if not os.path.exists(image_folder):
            self.stdout.write(self.style.ERROR(f'Image folder not found: {image_folder}'))
            return

        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        self.stdout.write(f'Found {len(image_files)} images in {image_folder}')

        # Get all menu items without images
        items_without_images = menu_item.objects.filter(pic='')
        self.stdout.write(f'Found {len(items_without_images)} items without images\n')

        matched_count = 0

        for item in items_without_images:
            best_match = None
            best_score = 0.4  # Minimum 40% similarity

            # Try to find a matching image
            for image_file in image_files:
                filename_without_ext = os.path.splitext(image_file)[0]
                
                # Create comparable names (lowercase, replace underscores/spaces)
                item_name_normalized = item.name.lower().replace(' ', '_')
                image_name_normalized = filename_without_ext.lower().replace(' ', '_')
                
                # Calculate similarity ratio
                similarity = SequenceMatcher(None, item_name_normalized, image_name_normalized).ratio()
                
                if similarity > best_score:
                    best_score = similarity
                    best_match = image_file

            # If match found, update the item
            if best_match:
                image_path = f'fimage/{best_match}'
                item.pic = image_path
                item.save()
                matched_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ {item.name} → {best_match} ({best_score:.1%})')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'✗ No match found for: {item.name}')
                )

        self.stdout.write(f'\n{self.style.SUCCESS(f"Matched {matched_count} items successfully!")}')