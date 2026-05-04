from django.core.management.base import BaseCommand
from webapp.models import ResearchPublication
from datetime import date


class Command(BaseCommand):
    help = 'Seeds sample research publications'

    def handle(self, *args, **options):
        samples = [
            {
                'title': "InMoov Humanoid Robot: Building Nepal's First Open-Source 3D-Printed Humanoid with Custom Modifications",
                'authors': 'Muni Bahadur Sakya, Ram Kumar Tamang, Subash Sigdel',
                'abstract': (
                    'This paper describes the development and customization of an InMoov humanoid robot at High Tech Pioneer Nepal. '
                    'We present our modifications to the original open-source design, including custom motor replacements, '
                    'a proprietary gear system for improved torque efficiency, and integration of Nepali language AI capabilities '
                    'using OpenAI Whisper and custom Devanagari NLP pipelines. The robot demonstrates real-time speech recognition '
                    'in Nepali, face recognition using DeepFace, and object detection using YOLOv8 on an embedded compute platform.'
                ),
                'category': 'robotics',
                'tags': 'InMoov, Humanoid Robot, 3D Printing, ROS, Devanagari, Nepal',
                'github_url': 'https://github.com/Ramtamang-2058',
                'published_date': date(2024, 6, 1),
                'is_published': True,
            },
            {
                'title': 'AI-Powered Wheeled Robot: Integrating Vision Language Models for Semantic Navigation in Unstructured Environments',
                'authors': 'Subash Sigdel, Ram Kumar Tamang',
                'abstract': (
                    'We present the design and implementation of an AI-powered wheeled robot built on the NVIDIA Jetson Nano platform. '
                    'The system integrates YOLOv8 for real-time object detection, OpenAI VLM for scene understanding, '
                    'OpenAI Whisper for speech commands in both English and Nepali, DeepFace for visitor recognition, '
                    'and ultrasonic sensors for obstacle avoidance. We evaluate the robot\'s performance in indoor navigation '
                    'tasks and demonstrate its ability to understand natural language commands, identify known individuals, '
                    'and respond contextually to its environment without pre-mapped navigation.'
                ),
                'category': 'ai',
                'tags': 'YOLO, Jetson Nano, VLM, Whisper, DeepFace, Computer Vision, Navigation',
                'github_url': 'https://github.com/Ramtamang-2058',
                'published_date': date(2024, 9, 15),
                'is_published': True,
            },
            {
                'title': "Devanagari Script Computing in Nepal: From the First Demonstration in 1983 to Modern NLP Systems",
                'authors': 'Muni Bahadur Sakya, Subash Sigdel',
                'abstract': (
                    'This survey traces the history of Devanagari computing in Nepal from the first demonstration of Nepali script '
                    'on a CP/M microcomputer in 1983 to modern deep learning approaches. We review OCR systems, text-to-speech '
                    'pipelines, machine translation models, and large language model fine-tuning techniques specific to the Nepali '
                    'language. Special attention is given to the challenges of low-resource NLP for Devanagari script and the role '
                    'of open-source tools in advancing Nepali language technology. We outline a roadmap for fully-capable '
                    'Nepali-language AI assistants by 2030.'
                ),
                'category': 'nlp',
                'tags': 'Devanagari, Nepali NLP, OCR, TTS, Low-Resource NLP, LLM, History',
                'published_date': date(2023, 12, 1),
                'is_published': True,
            },
        ]

        for data in samples:
            obj, created = ResearchPublication.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {obj.title[:70]}'))
            else:
                self.stdout.write(f'Already exists: {obj.title[:70]}')

        self.stdout.write(self.style.SUCCESS('Done.'))
