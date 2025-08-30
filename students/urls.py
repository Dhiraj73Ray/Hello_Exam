
# students/urls.py
from django.urls import path
from .views import StudentOnboardingWizard, Reports
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from .forms import (
    PersonalDetailsForm,
    AcademicDetailsForm,
    SubjectChoiceForm,
    ProfilePictureForm,
)


file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'wizard_uploads'))

urlpatterns = [
    path(
        "onboarding/",
        StudentOnboardingWizard.as_view([
            ("personal", PersonalDetailsForm),
            ("academic", AcademicDetailsForm),
            ("subjects", SubjectChoiceForm),
            ("profile_pic", ProfilePictureForm),
        ],file_storage=file_storage),
        name="onboarding",
    ),
    path('', Reports, name='report'),
]
