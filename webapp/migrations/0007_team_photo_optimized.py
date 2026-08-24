from django.db import migrations

PHOTO_UPDATES = [
    ('Muni Bahadur Sakya', '/static/img/opt/muni_sakya_portrait_900.jpg'),
    ('Ram Kumar Tamang', '/static/img/opt/ram_tamang_600.jpg'),
    ('Subash Sigdel', '/static/img/opt/subash_sigdel_600.jpg'),
    ('Bikash Tamang', '/static/img/opt/bikash_tamang_600.jpg'),
]


def update_photos(apps, schema_editor):
    TeamMember = apps.get_model('webapp', 'TeamMember')
    for name, photo in PHOTO_UPDATES:
        TeamMember.objects.filter(name=name).update(photo=photo)


def revert_photos(apps, schema_editor):
    TeamMember = apps.get_model('webapp', 'TeamMember')
    reverts = {
        'Muni Bahadur Sakya': '/static/img/profiles/muni_bahadur_sakya.png',
        'Ram Kumar Tamang': '/static/img/profiles/ram_tamang.jpeg',
        'Subash Sigdel': '/static/img/profiles/subash_sigdel.png',
        'Bikash Tamang': '/static/img/profiles/bikash_tamang.png',
    }
    for name, photo in reverts.items():
        TeamMember.objects.filter(name=name).update(photo=photo)


class Migration(migrations.Migration):
    dependencies = [
        ('webapp', '0006_update_story_media'),
    ]

    operations = [
        migrations.RunPython(update_photos, revert_photos),
    ]
