from django.db import migrations


DEFAULT_SLOTS = [
    {'slot': 'video', 'label': 'Product video', 'media_type': 'video',
     'fallback_path': '/video/handshke_robot.mp4',
     'caption': 'Kancha in action — hear, think, see, move.', 'sort_order': 0},
    {'slot': 'image_1', 'label': 'Kancha, upper front view', 'media_type': 'image',
     'fallback_path': '/static/img/robots/kancha_upper_front_view.jpeg',
     'caption': 'Upper front view.', 'sort_order': 1},
    {'slot': 'image_2', 'label': 'Base unit', 'media_type': 'image',
     'fallback_path': '/static/img/robots/kancha_base_unit.jpeg',
     'caption': 'The ESP32-S3 drive base.', 'sort_order': 2},
    {'slot': 'image_3', 'label': 'Palm and fingers', 'media_type': 'image',
     'fallback_path': '/static/img/robots/kancha_palm.jpeg',
     'caption': 'The palm and finger servos.', 'sort_order': 3},
    {'slot': 'image_4', 'label': 'Head and camera', 'media_type': 'image',
     'fallback_path': '/static/img/robots/kancha_head_camera_view.jpeg',
     'caption': 'The head that feeds the vision system.', 'sort_order': 4},
    {'slot': 'image_5', 'label': 'Upper back wiring', 'media_type': 'image',
     'fallback_path': '/static/img/robots/kancha_upper_back_wiring.jpeg',
     'caption': 'Two drivers on 26 servos.', 'sort_order': 5},
    {'slot': 'image_6', 'label': 'Left leg', 'media_type': 'image',
     'fallback_path': '/static/img/robots/kancha_left_leg.jpeg',
     'caption': 'Left leg, assembled.', 'sort_order': 6},
]


def seed_slots(apps, schema_editor):
    ProductMedia = apps.get_model('webapp', 'ProductMedia')
    for item in DEFAULT_SLOTS:
        ProductMedia.objects.get_or_create(slot=item['slot'], defaults=item)


def remove_slots(apps, schema_editor):
    ProductMedia = apps.get_model('webapp', 'ProductMedia')
    ProductMedia.objects.filter(slot__in=[s['slot'] for s in DEFAULT_SLOTS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_productmedia'),
    ]

    operations = [
        migrations.RunPython(seed_slots, remove_slots),
    ]
