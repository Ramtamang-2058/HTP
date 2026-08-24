from django.db import migrations
from datetime import date


def forwards(apps, schema_editor):
    Story = apps.get_model('webapp', 'Story')
    Milestone = apps.get_model('webapp', 'Milestone')

    # Videos remuxed .mov -> .mp4 (browsers refuse the MOV container).
    for story in Story.objects.filter(media_type='video'):
        if story.media_url.endswith('.mov'):
            story.media_url = story.media_url[:-4] + '.mp4'
            story.save(update_fields=['media_url'])

    # 1979: SC/MP detail + worldwide press reach (Zerone Magazine interview).
    m = Milestone.objects.filter(sort_order=4).first()
    if m:
        m.body = (
            "From parts gathered across three countries — an SC/MP microprocessor, "
            "a Russian television for a monitor, a hand-built power supply and video "
            "card — Sakya assembles Nepal's first microcomputer. Demonstrated at the "
            "South Asian Regional Conference on Computers in Kathmandu, it is covered "
            "by The Rising Nepal and Xinhua; the wire story is republished across 88 "
            "countries. Parts sourced from around the world earn it a nickname: the "
            "\"UN computer\"."
        )
        m.save(update_fields=['body'])

    # 1985: use the bank's Nepali name alongside the official one.
    m = Milestone.objects.filter(sort_order=8).first()
    if m:
        m.title = 'Krishi Bikas Bank goes Devanagari'
        m.body = (
            "Krishi Bikas Bank — the Agriculture Development Bank — commissions "
            "nineteen computers, one per branch, running Sakya's Devanagari system "
            "and entering customer names in Nepali. Government offices follow."
        )
        m.save(update_fields=['title', 'body'])

    # Make room for two entries between the supercomputer (12) and the awards.
    for old, new in ((15, 17), (14, 16), (13, 15)):
        Milestone.objects.filter(sort_order=old).update(sort_order=new)

    Milestone.objects.get_or_create(
        sort_order=13,
        defaults=dict(
            year='2010s',
            exact_date=date(2010, 1, 1),
            title='Green computers for telemedicine',
            body=(
                "Low-power \"green computers\" drawing roughly 35 watts — a fraction "
                "of a desktop — are built with doctors for telemedicine clinics in "
                "Jajarkot, Kalikot, Bajura and Dhading, bringing specialist care to "
                "districts far from Kathmandu."
            ),
            is_active=True,
        ),
    )
    Milestone.objects.get_or_create(
        sort_order=14,
        defaults=dict(
            year='2000s–today',
            exact_date=date(2005, 1, 1),
            title='Networking hardware for ISPs',
            body=(
                "Alongside the lab work, the company becomes a supplier of Buffalo "
                "routers and other core networking equipment to internet service "
                "providers across Nepal — keeping the country's connections running "
                "has quietly funded four decades of experimentation."
            ),
            is_active=True,
        ),
    )


def backwards(apps, schema_editor):
    Story = apps.get_model('webapp', 'Story')
    Milestone = apps.get_model('webapp', 'Milestone')

    for story in Story.objects.filter(media_type='video'):
        if story.media_url.endswith('.mp4'):
            story.media_url = story.media_url[:-4] + '.mov'
            story.save(update_fields=['media_url'])

    Milestone.objects.filter(sort_order=13, year='2010s').delete()
    Milestone.objects.filter(sort_order=14, year='2000s–today').delete()

    for old, new in ((17, 15), (16, 14), (15, 13)):
        Milestone.objects.filter(sort_order=old).update(sort_order=new)

    m = Milestone.objects.filter(sort_order=4).first()
    if m:
        m.body = (
            "From parts gathered across three countries — a US keyboard, a Russian "
            "television for a monitor, a hand-built power supply and video card — Sakya "
            "assembles Nepal's first microcomputer. It is demonstrated at the South Asian "
            "Regional Conference on Computers in Kathmandu; The Rising Nepal and Xinhua "
            "cover the build. Parts sourced from around the world earn it a nickname: the "
            "\"UN computer\"."
        )
        m.save(update_fields=['body'])

    m = Milestone.objects.filter(sort_order=8).first()
    if m:
        m.title = 'Agriculture Development Bank goes Devanagari'
        m.body = (
            "The Agriculture Development Bank commissions nineteen computers — one per "
            "branch — running Sakya's Devanagari system, entering customer names in "
            "Nepali. Government offices follow."
        )
        m.save(update_fields=['title', 'body'])


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_team_photo_optimized'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
