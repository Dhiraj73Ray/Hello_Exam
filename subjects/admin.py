from django.contrib import admin
from .models import Subject, SubjectEnrollment, Resources
# Register your models here.
admin.site.register(Subject)
admin.site.register(SubjectEnrollment)
admin.site.register(Resources)