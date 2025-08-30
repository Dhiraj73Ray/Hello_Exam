from django.core.management.base import BaseCommand
from subjects.models import Subject

class Command(BaseCommand):
    help = "Seed the database with default subjects"

    def handle(self, *args, **options):
        subjects = [
        {'name': 'Physics', 'stream': 'Science', 'class': '11'},
        {'name': 'Biology', 'stream': 'Science', 'class': '11'},
        {'name': 'Mathematics', 'stream': 'Science', 'class': '11'},
        {'name': 'English', 'stream': 'All', 'class': '11'},
        {'name': 'Chemistry', 'stream': 'Science', 'class': '11'},
        {'name': 'Computer Science', 'stream': 'Science', 'class': '11'},
        {'name': 'Environmental Science', 'stream': 'All', 'class': '11'},
        {'name': 'Biotechnology', 'stream': 'Science', 'class': '11'},
        {'name': 'Psychology', 'stream': 'Science', 'class': '11'},
        {'name': 'Home Science', 'stream': 'Science', 'class': '11'},
        {'name': 'Informatics Practices', 'stream': 'Science', 'class': '11'},
        {'name': 'Geology', 'stream': 'Science', 'class': '11'},
        {'name': 'Astronomy', 'stream': 'Science', 'class': '11'},
        {'name': 'Electronics', 'stream': 'Science', 'class': '11'},
        {'name': 'Physics', 'stream': 'Science', 'class': '12'},
        {'name': 'Chemistry', 'stream': 'Science', 'class': '12'},
        {'name': 'Biology', 'stream': 'Science', 'class': '12'},
        {'name': 'Mathematics and Statistics I', 'stream': 'Science', 'class': '12'},
        {'name': 'Mathematics and Statistics II', 'stream': 'Science', 'class': '12'},
        {'name': 'Agriculture Science and Technology', 'stream': 'Science', 'class': '12'},
        {'name': 'Information Technology', 'stream': 'Science', 'class': '12'},
        {'name': 'Book-keeping and Accountancy', 'stream': 'Commerce', 'class': '11'},
        {'name': 'Economics', 'stream': 'Commerce', 'class': '11'},
        {'name': 'Organization of Commerce and Management', 'stream': 'Commerce', 'class': '11'},
        {'name': 'Mathematics and Statistics', 'stream': 'Commerce', 'class': '11'},
        {'name': 'Secretarial Practice (SP)', 'stream': 'Commerce', 'class': '11'},
        {'name': 'Information Technology', 'stream': 'Commerce', 'class': '11'},
        {'name': 'Modern Indian or Foreign Languages', 'stream': 'Commerce', 'class': '11'},
        {'name': 'Book-keeping and Accountancy', 'stream': 'Commerce', 'class': '12'},
        {'name': 'Economics', 'stream': 'Commerce', 'class': '12'},
        {'name': 'Organization of Commerce and Management', 'stream': 'Commerce', 'class': '12'},
        {'name': 'Mathematics and Statistics', 'stream': 'Commerce', 'class': '12'},
        {'name': 'Secretarial Practice (SP)', 'stream': 'Commerce', 'class': '12'},
        {'name': 'Information Technology', 'stream': 'Commerce', 'class': '12'},
        {'name': 'Modern Indian or Foreign Languages', 'stream': 'Commerce', 'class': '12'},
        {'name': 'Economics', 'stream': 'Arts', 'class': '11'},
        {'name': 'Political Science', 'stream': 'Arts', 'class': '11'},
        {'name': 'Sociology', 'stream': 'Arts', 'class': '11'},
        {'name': 'Psychology', 'stream': 'Arts', 'class': '11'},
        {'name': 'Geography', 'stream': 'Arts', 'class': '11'},
        {'name': 'History', 'stream': 'Arts', 'class': '11'},
        {'name': 'Mathematics', 'stream': 'Arts', 'class': '11'},
        {'name': 'Hindi', 'stream': 'Arts', 'class': '11'},
        {'name': 'Marathi', 'stream': 'Arts', 'class': '11'},
        {'name': 'Philosophy', 'stream': 'Arts', 'class': '11'},
        {'name': 'Music', 'stream': 'Arts', 'class': '11'},
        {'name': 'Informatics Practice', 'stream': 'Arts', 'class': '11'},
        {'name': 'Legal Studies', 'stream': 'Arts', 'class': '11'},
        {'name': 'Human Rights and Gender Studies', 'stream': 'Arts', 'class': '11'},
        {'name': 'Mass Media Studies', 'stream': 'Arts', 'class': '11'},
        {'name': 'Public Administration', 'stream': 'Arts', 'class': '11'},
        {'name': 'Entrepreneurship', 'stream': 'Arts', 'class': '11'},
        {'name': 'Fashion Studies', 'stream': 'Arts', 'class': '11'},
        {'name': 'Home Science', 'stream': 'Arts', 'class': '11'},
        {'name': 'Fine Arts', 'stream': 'Arts', 'class': '11'},
        {'name': 'History', 'stream': 'Arts', 'class': '12'},
        {'name': 'Geography', 'stream': 'Arts', 'class': '12'},
        {'name': 'Political Science', 'stream': 'Arts', 'class': '12'},
        {'name': 'Economics', 'stream': 'Arts', 'class': '12'},
        {'name': 'Psychology', 'stream': 'Arts', 'class': '12'},
        {'name': 'Sociology', 'stream': 'Arts', 'class': '12'},
        {'name': 'Information Technology', 'stream': 'Arts', 'class': '12'},
        {'name': 'Mathematics and Statistics', 'stream': 'Arts', 'class': '12'},
        {'name': 'Environment Education (EVS)', 'stream': 'All', 'class': '11'},
        {'name': 'Health and Physical Education', 'stream': 'All', 'class': '11'},
        {'name': 'English', 'stream': 'All', 'class': '12'},
        {'name': 'Environment Education (EVS)', 'stream': 'All', 'class': '12'},
        {'name': 'Health and Physical Education', 'stream': 'All', 'class': '12'},
    ]

        for subj in subjects:
            obj, created = Subject.objects.get_or_create(
                name=subj['name'],
                stream=subj['stream'],
                class_level=subj['class'],
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added {obj}"))
            else:
                self.stdout.write(self.style.WARNING(f"Skipped {obj} (already exists)"))
