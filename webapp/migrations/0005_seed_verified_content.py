"""Seed verified, factual content.

Every milestone, team bio and publication below is sourced from public,
verifiable records:
- Wikipedia: https://en.wikipedia.org/wiki/Muni_Sakya
- CAN Federation ICT Award citation: https://www.can.org.np/page/12
- The Record (2021): https://www.recordnepal.com/meet-muni-bahadur-shakya-a-pioneering-nepali-computer-scientist
- The Zerone interview (2016): https://medium.com/zerone-magazine/in-pursuit-of-knowledge-and-excellence-the-inspiring-life-of-muni-bahadur-sakya-e6a4d32e05c0
- WACV 2026 Workshop (GeoCV) Open Access proceedings
"""
from datetime import date

from django.db import migrations

MILESTONES = [
    {
        'year': '1962', 'sort_order': 1, 'exact_date': date(1962, 1, 1),
        'title': 'Radio engineering, Calcutta',
        'body': (
            'Muni Bahadur Sakya completes a diploma in radio engineering in Calcutta, '
            'India, and joins Radio Nepal as a technician on his return — repairing and '
            'running the country\'s broadcasting hardware.'
        ),
    },
    {
        'year': '1970', 'sort_order': 2, 'exact_date': date(1970, 1, 1),
        'title': 'Computer engineering, United Kingdom',
        'body': (
            'Awarded a British Council scholarship, Sakya studies electronics and computer '
            'engineering in England. He is offered engineering work there — and turns it '
            'down to return home.'
        ),
    },
    {
        'year': '1973–79', 'sort_order': 3, 'exact_date': date(1973, 1, 1),
        'title': 'Mainframes and microprocessors, France',
        'body': (
            'On French government training he works with mainframe computers, building '
            'microprocessor-based controllers and video cards — the exact skills that will '
            'soon be carried back to Kathmandu.'
        ),
    },
    {
        'year': '1979', 'sort_order': 4, 'exact_date': date(1979, 1, 1),
        'title': "Nepal's first microcomputer",
        'body': (
            'From parts gathered across three countries — a US keyboard, a Russian '
            'television for a monitor, a hand-built power supply and video card — Sakya '
            'assembles Nepal\'s first microcomputer. It is demonstrated at the South Asian '
            'Regional Conference on Computers in Kathmandu; The Rising Nepal and Xinhua '
            'cover the build. Parts sourced from around the world earn it a nickname: the '
            '"UN computer".'
        ),
    },
    {
        'year': '1981', 'sort_order': 5, 'exact_date': date(1981, 1, 1),
        'title': 'Floppy-disk controllers, Minnesota',
        'body': (
            'Sakya works at MTS Systems Corporation in the USA on floppy disk controller '
            'development — pushing toward 900 KB disks when 80 KB was standard — and '
            'visits Silicon Valley to see IBM\'s first hard-drive PC in production.'
        ),
    },
    {
        'year': 'Dec 1983', 'sort_order': 6, 'exact_date': date(1983, 12, 1),
        'title': 'The computer learns Nepali',
        'body': (
            'Returning home with sixteen boxes of components, Sakya demonstrates the first '
            'computer able to read and display Devanagari script on a CP/M machine — the '
            'national anthem, श्रीमान् गम्भीर, rendered in Nepali. A seven-day exhibition at '
            'Tri-Chandra College follows, Gorkhapatra prints the story, and he receives a '
            'national Science Award for the achievement.'
        ),
    },
    {
        'year': '1984', 'sort_order': 7, 'exact_date': date(1984, 1, 1),
        'title': 'High Tech Pioneer Pvt. Ltd. founded',
        'body': (
            'Sakya establishes High Tech Pioneer Pvt. Ltd. in Dillibazar, Kathmandu — '
            'Nepal\'s first commercial computer hardware company, registered while the '
            'country was still the Kingdom of Nepal under the Panchayat system.'
        ),
    },
    {
        'year': '1985', 'sort_order': 8, 'exact_date': date(1985, 1, 1),
        'title': 'Agriculture Development Bank goes Devanagari',
        'body': (
            'The Agriculture Development Bank commissions nineteen computers — one per '
            'branch — running Sakya\'s Devanagari system, entering customer names in '
            'Nepali. Government offices follow.'
        ),
    },
    {
        'year': '1995', 'sort_order': 9, 'exact_date': date(1995, 1, 1),
        'title': 'Sun Moon Computer Industry',
        'body': (
            'Sakya opens Sun Moon Computer Industry, the first Nepalese company to '
            'manufacture computer cards commercially — an early bid at hardware sovereignty '
            'against full import dependency.'
        ),
    },
    {
        'year': '2004–05', 'sort_order': 10, 'exact_date': date(2004, 1, 1),
        'title': 'The Munis Robot speaks Nepali',
        'body': (
            'A home-grown robot that speaks Nepali and senses obstacles through ultrasonic, '
            'infrared and mechanical whisker sensors — years before robotics was a topic in '
            'the domestic press.'
        ),
    },
    {
        'year': '2005', 'sort_order': 11, 'exact_date': date(2005, 1, 1),
        'title': 'RONAST science award',
        'body': (
            'The Royal Nepal Academy of Science and Technology felicitates Sakya as an '
            'A-class scientist in information technology for sustained contribution to '
            'Nepali science.'
        ),
    },
    {
        'year': '17 May 2006', 'sort_order': 12, 'exact_date': date(2006, 5, 17),
        'title': "Nepal's first supercomputer",
        'body': (
            'A sixteen-node cluster running open-source software (OpenMosix and OSCAR) is '
            'publicly demonstrated in Kathmandu — the country\'s first supercomputer, built '
            'from commodity machines for weather, financial and research computing.'
        ),
    },
    {
        'year': '2012', 'sort_order': 13, 'exact_date': date(2012, 1, 1),
        'title': 'ICT Business Excellence Award',
        'body': (
            'The Computer Association of Nepal (CAN) Federation honours Muni Bahadur Sakya '
            'with its ICT Business Excellence Award for ushering information technology '
            'into Nepal.'
        ),
    },
    {
        'year': '2016', 'sort_order': 14, 'exact_date': date(2016, 1, 1),
        'title': 'ICT Pioneer Award',
        'body': (
            'Lifetime-contribution honour: the ICT Award committee recognises Sakya as the '
            'pioneer who "set a new precedent by demonstrating to everyone that it was '
            'possible for computers to be built in Nepal".'
        ),
    },
    {
        'year': '2020s', 'sort_order': 15, 'exact_date': date(2020, 1, 1),
        'title': 'Humanoid robotics and applied AI',
        'body': (
            'The lab enters its fifth decade building an InMoov humanoid robot and an AI '
            'wheeled robot on embedded edge-AI hardware — speech recognition, vision and '
            'language models engineered around Nepali users — carrying four decades of '
            'Devanagari computing into the age of machine learning.'
        ),
    },
]

TEAM = [
    {
        'name': 'Muni Bahadur Sakya',
        'role': 'Founder & CEO',
        'role_type': 'founder',
        'sort_order': 1,
        'photo': '/static/img/profiles/muni_bahadur_sakya.png',
        'linkedin_url': 'https://www.linkedin.com/in/muni-sakya-6a530574/',
        'bio': (
            'Born 1942 in Patan. Built Nepal\'s first microcomputer (1979), taught computers '
            'to read Nepali (1983), founded the country\'s first commercial computer hardware '
            'company (1984) and its first computer-card manufacturer (1995), and demonstrated '
            'Nepal\'s first supercomputer (2006). Honoured by RONAST (2005), the CAN Federation '
            '(2012) and the ICT Pioneer Award (2016). Still at the bench, five decades on.'
        ),
    },
    {
        'name': 'Ram Kumar Tamang',
        'role': 'Software Lead — Robotics',
        'role_type': 'engineer',
        'sort_order': 2,
        'photo': '/static/img/profiles/ram_tamang.jpeg',
        'github_url': 'https://github.com/Ramtamang-2058',
        'linkedin_url': 'https://www.linkedin.com/in/ram-tamang-a73241198',
        'portfolio_url': 'https://ram-tamang.com.np',
        'bio': (
            'Backend engineer specialising in Python, Django and FastAPI. Leads software for '
            'the HTP humanoid robot — Whisper speech recognition, vision-language scene '
            'understanding, face recognition and the master control pipeline on embedded '
            'hardware. By day he builds Nepal\'s national weather forecast and flood '
            'early-warning platforms at NAXA Pvt. Ltd.'
        ),
    },
    {
        'name': 'Subash Sigdel',
        'role': 'Robotics & AI Researcher',
        'role_type': 'researcher',
        'sort_order': 3,
        'photo': '/static/img/profiles/subash_sigdel.png',
        'github_url': 'https://github.com/subashsigdel',
        'linkedin_url': 'https://www.linkedin.com/in/subash5/',
        'scholar_url': 'https://scholar.google.com/citations?user=rph8zrYAAAAJ&hl=en',
        'portfolio_url': 'https://subashsigdel.com.np',
        'bio': (
            'Researcher in reinforcement learning and computer vision at NAAMII\'s A² Lab. '
            'Co-author of "Segment Anything but Farms" (WACV 2026 Workshop on Geospatial '
            'Computer Vision). At HTP he works on grounding vision-language models in '
            'physical robot action — teaching the machine to point at what it sees — alongside '
            'the 3D-printing pipeline and mechanical assembly.'
        ),
    },
    {
        'name': 'Bikash Tamang',
        'role': 'Lab Assistant',
        'role_type': 'staff',
        'sort_order': 4,
        'photo': '/static/img/profiles/bikash_tamang.png',
        'bio': (
            'Keeps the lab running day to day: 3D-print part finishing, servo wiring and '
            'calibration, sensor mounting and test support across the humanoid and wheeled '
            'robot builds.'
        ),
    },
]

PUBLICATIONS = [
    {
        'title': 'Segment Anything but Farms: Comparing Segmentation Paradigms for Rural UAV Captured Ultra-High-Resolution Imagery',
        'authors': 'Snehalraj Chugh, Dharmendra Singh Chaudhary, Subash Sigdel, Shubham Thapa, Lalit BC, Nishan Ghimire, Bipendra Basnyat, Nirmalya Roy',
        'venue': 'WACV 2026 Workshop on Geospatial Computer Vision (GeoCV)',
        'abstract': (
            'Evaluates promptable segmentation paradigms — including the Segment Anything Model '
            'family — against fine-tuned baselines on ultra-high-resolution UAV imagery of rural '
            'farmland, where small objects, heavy class imbalance and massive image sizes break '
            'assumptions designed for natural photos.'
        ),
        'category': 'ai',
        'tags': 'Computer Vision, Segmentation, SAM, UAV Imagery, Remote Sensing',
        'external_url': 'https://openaccess.thecvf.com/content/WACV2026W/GeoCV/papers/Chugh_Segment_Anything_but_Farms_Comparing_Segmentation_Paradigms_for_Rural_UAV_WACVW_2026_paper.pdf',
        'published_date': date(2026, 2, 1),
        'is_published': True,
    },
    {
        'title': 'Classification in Machine Learning',
        'authors': 'Subash Sigdel',
        'venue': 'Independent research note',
        'abstract': (
            'A technical overview of classification — learning a function that maps feature sets '
            'to predefined class labels — surveying core algorithms and evaluation practice for '
            'pattern-recognition tasks.'
        ),
        'category': 'ai',
        'tags': 'Machine Learning, Classification',
        'external_url': 'https://subashsigdel.com.np/Re/research.html',
        'published_date': date(2022, 4, 5),
        'is_published': True,
    },
]


def seed(apps, schema_editor):
    Milestone = apps.get_model('webapp', 'Milestone')
    TeamMember = apps.get_model('webapp', 'TeamMember')
    Publication = apps.get_model('webapp', 'ResearchPublication')

    # Remove any placeholder/sample publications from earlier tooling.
    Publication.objects.filter(
        title__in=[
            "InMoov Humanoid Robot: Building Nepal's First Open-Source 3D-Printed Humanoid with Custom Modifications",
            'AI-Powered Wheeled Robot: Integrating Vision Language Models for Semantic Navigation in Unstructured Environments',
            'Devanagari Script Computing in Nepal: From the First Demonstration in 1983 to Modern NLP Systems',
        ]
    ).delete()

    for m in MILESTONES:
        Milestone.objects.get_or_create(sort_order=m['sort_order'], defaults=m)
    for t in TEAM:
        TeamMember.objects.get_or_create(name=t['name'], defaults=t)
    for p in PUBLICATIONS:
        Publication.objects.get_or_create(title=p['title'], defaults=p)


def unseed(apps, schema_editor):
    Milestone = apps.get_model('webapp', 'Milestone')
    TeamMember = apps.get_model('webapp', 'TeamMember')
    Publication = apps.get_model('webapp', 'ResearchPublication')

    for m in MILESTONES:
        Milestone.objects.filter(sort_order=m['sort_order'], year=m['year']).delete()
    for t in TEAM:
        TeamMember.objects.filter(name=t['name']).delete()
    for p in PUBLICATIONS:
        Publication.objects.filter(title=p['title']).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('webapp', '0004_add_venue_milestones_team'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
