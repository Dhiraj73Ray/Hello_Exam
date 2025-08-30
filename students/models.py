from django.contrib.auth.models import User
from django.db import models
from subjects.models import Subject

class StudentProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    CLASS_CHOICES = [
        ('11', '11'),
        ('12', '12'),
    ]
    STREAM_CHOICES = [
        ('Science', 'Science'),
        ('Commerce', 'Commerce'),
        ('Arts', 'Arts'),
        ('All', 'All'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    class_level = models.CharField(max_length=2, choices=CLASS_CHOICES, blank=True)
    stream = models.CharField(max_length=20, choices=STREAM_CHOICES, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    level = models.PositiveIntegerField(default=1)        # you can compute later
    enrolled_subjects = models.ManyToManyField(
        'subjects.Subject', related_name="enrolled_students", blank=True
    )
    onboarding_complete = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

