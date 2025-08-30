from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    STREAM_CHOICES = [
        ('Science', 'Science'),
        ('Commerce', 'Commerce'),
        ('Arts', 'Arts'),
        ('All', 'All'),
    ]

    CLASS_CHOICES = [
        ('11', '11'),
        ('12', '12'),
    ]

    name = models.CharField(max_length=100)
    stream = models.CharField(max_length=50, choices=STREAM_CHOICES)
    class_level = models.CharField(max_length=20, choices=CLASS_CHOICES)
    description = models.TextField(blank=True, null=True) 
    is_active = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"{self.name} ({self.stream}, Class {self.class_level})"


class SubjectEnrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'subject')


class Resources(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="documents")
    subjects_type = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="documents")
    file = models.FileField(upload_to="user_uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.subjects_type.name} - {self.file.name}"