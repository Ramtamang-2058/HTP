from django.db import migrations

def populate_stories(apps, schema_editor):
    Story = apps.get_model('webapp', 'Story')
    Story.objects.create(
        title='Muni Sakya',
        media_url='/static/img/profiles/muni_bahadur_sakya.png',
        thumbnail_url='/static/img/profiles/muni_bahadur_sakya.png',
        caption="Founder Muni Bahadur Sakya demonstrating Nepal's first Devanagari computing (1983).",
        media_type='image',
        order=1
    )
    Story.objects.create(
        title='3D Robot Print',
        media_url='/static/img/robots/robot_after_3d_print.jpeg',
        thumbnail_url='/static/img/robots/robot_after_3d_print.jpeg',
        caption="InMoov humanoid robot frame assembled after 3D printing in the HTP lab.",
        media_type='image',
        order=2
    )
    Story.objects.create(
        title='Hand Assembly',
        media_url='/static/img/robots/robots_hand_assembling.png',
        thumbnail_url='/static/img/robots/robots_hand_assembling.png',
        caption="Calibrating and assembling the mechanical hand degrees of freedom.",
        media_type='image',
        order=3
    )
    Story.objects.create(
        title='Base Assembly',
        media_url='/video/building_base_robot.mov',
        thumbnail_url='/static/img/robots/assembling_after_print_upper_body.jpeg',
        caption="Video: Assembly of the mobile base robot in Dillibazar.",
        media_type='video',
        order=4
    )
    Story.objects.create(
        title='Handshake Demo',
        media_url='/video/handshke_robot.mov',
        thumbnail_url='/static/img/robots/left_hand_break.png',
        caption="Video: Live humanoid robot handshake demonstration.",
        media_type='video',
        order=5
    )

def unload_stories(apps, schema_editor):
    Story = apps.get_model('webapp', 'Story')
    Story.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('webapp', '0002_story'),
    ]
    operations = [
        migrations.RunPython(populate_stories, unload_stories),
    ]
