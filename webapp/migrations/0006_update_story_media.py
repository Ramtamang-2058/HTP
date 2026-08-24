from django.db import migrations

STORY_UPDATES = [
    ('Muni Sakya', {
        'media_url': '/static/img/opt/muni_sakya_portrait_900.jpg',
        'thumbnail_url': '/static/img/opt/muni_sakya_portrait_900.jpg',
        'caption': "Founder Muni Bahadur Sakya, whose 1983 demonstration taught Nepal's first computer to read Devanagari.",
    }),
    ('3D Robot Print', {
        'media_url': '/static/img/opt/robot_after_3d_print_1400.jpg',
        'thumbnail_url': '/static/img/opt/robot_after_3d_print_1400.jpg',
        'caption': 'InMoov humanoid frame, assembled straight off the 3D printers.',
    }),
    ('Hand Assembly', {
        'media_url': '/static/img/opt/hand_assembling_1400.jpg',
        'thumbnail_url': '/static/img/opt/hand_assembling_1400.jpg',
        'caption': 'Calibrating the mechanical hand — one degree of freedom at a time.',
    }),
    ('Base Assembly', {
        'thumbnail_url': '/static/img/opt/assembling_upper_body_1400.jpg',
        'caption': 'Assembly of the mobile base, filmed in the Dillibazar workshop.',
    }),
    ('Handshake Demo', {
        'thumbnail_url': '/static/img/opt/left_hand_break_900.jpg',
        'caption': 'Live handshake test — the moment the arm finally grips right.',
    }),
]


def update_stories(apps, schema_editor):
    Story = apps.get_model('webapp', 'Story')
    for title, fields in STORY_UPDATES:
        Story.objects.filter(title=title).update(**fields)


def revert_stories(apps, schema_editor):
    Story = apps.get_model('webapp', 'Story')
    reverts = {
        'Muni Sakya': {
            'media_url': '/static/img/profiles/muni_bahadur_sakya.png',
            'thumbnail_url': '/static/img/profiles/muni_bahadur_sakya.png',
            'caption': "Founder Muni Bahadur Sakya demonstrating Nepal's first Devanagari computing (1983).",
        },
        '3D Robot Print': {
            'media_url': '/static/img/robots/robot_after_3d_print.jpeg',
            'thumbnail_url': '/static/img/robots/robot_after_3d_print.jpeg',
            'caption': 'InMoov humanoid robot frame assembled after 3D printing in the HTP lab.',
        },
        'Hand Assembly': {
            'media_url': '/static/img/robots/robots_hand_assembling.png',
            'thumbnail_url': '/static/img/robots/robots_hand_assembling.png',
            'caption': 'Calibrating and assembling the mechanical hand degrees of freedom.',
        },
        'Base Assembly': {
            'thumbnail_url': '/static/img/robots/assembling_after_print_upper_body.jpeg',
            'caption': 'Video: Assembly of the mobile base robot in Dillibazar.',
        },
        'Handshake Demo': {
            'thumbnail_url': '/static/img/robots/left_hand_break.png',
            'caption': 'Video: Live humanoid robot handshake demonstration.',
        },
    }
    for title, fields in reverts.items():
        Story.objects.filter(title=title).update(**fields)


class Migration(migrations.Migration):
    dependencies = [
        ('webapp', '0005_seed_verified_content'),
    ]

    operations = [
        migrations.RunPython(update_stories, revert_stories),
    ]
