from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from formtools.wizard.views import SessionWizardView
from .forms import ( PersonalDetailsForm, AcademicDetailsForm, SubjectChoiceForm, ProfilePictureForm, StudentProfileForm, UserForm)
from .models import StudentProfile
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from subjects.models import Subject

# Create your views here.

# @login_required(login_url='/login/')
# def Profile(req):
#     return render(req, 'students/profile.html')

# We’ll define the sequence of forms for the wizard
FORMS = [
    ("personal", PersonalDetailsForm),
    ("academic", AcademicDetailsForm),
    ("subjects", SubjectChoiceForm),
    ("profile_pic", ProfilePictureForm),
]


# TEMPLATES = {
#     "personal": "students/wizard_personal.html",
#     "academic": "students/wizard_academic.html",
#     "subjects": "students/wizard_subjects.html",
#     "profile_pic": "students/wizard_profile_pic.html",
# }


@login_required(login_url='/login/')
def Profile(request):
    profile = get_object_or_404(StudentProfile, user=request.user)

    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get("first_name", "")
        user.last_name = request.POST.get("last_name", "")
        user.email = request.POST.get("email", "")
        user.save()

        profile.phone = request.POST.get("phone", "")
        dob = request.POST.get("dob", "").strip()
        profile.dob = dob if dob else None
        profile.gender = request.POST.get("gender", "")
        profile.class_level = request.POST.get("class_level", "")
        profile.stream = request.POST.get("stream", "")
        profile.address = request.POST.get("address", "")

        # Remove picture if clicked
        if "remove_picture" in request.POST:
            if profile.profile_picture:
                profile.profile_picture.delete(save=False)
            profile.profile_picture = None
            profile.save()  

        # Otherwise normal update
        else:
            if "profile_picture" in request.FILES:
                profile.profile_picture = request.FILES["profile_picture"]

        profile.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("profile")

    return render(request, "students/profile.html", {"profile": profile})


@method_decorator(login_required, name="dispatch")
class StudentOnboardingWizard(SessionWizardView):
    form_list = FORMS
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'wizard_uploads')
    )

    # def get_template_names(self):
    #     """Pick the template for the current step."""
    #     return [TEMPLATES[self.steps.current]]
    template_name = "core/wizard_form.html"

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)

        step_titles = {
        "personal": "Personal Details",
        "academic": "Academic Details",
        "subjects": "Favourite Subjects",
        "profile_pic": "Profile Picture (Optional)",
        }
        context["step_title"] = step_titles[self.steps.current]

        if self.steps.current == 'subjects':
            context['available_subjects'] = Subject.objects.all()
        # for file upload step
        if self.steps.current == "profile_pic":
            context["form_enctype"] = "multipart/form-data"

        return context

    def get_form_kwargs(self, step=None):
        kwargs = super().get_form_kwargs(step)

        if step == "subjects":
            # get previous step’s cleaned data
            academic_data = self.get_cleaned_data_for_step("academic") or {}
            kwargs["class_choice"] = academic_data.get("class_level")
            kwargs["stream_choice"] = academic_data.get("stream")

        return kwargs

    def done(self, form_list, **kwargs):
        """
        Once all steps are complete, save everything at once.
        """
        user = self.request.user
        profile, created = StudentProfile.objects.get_or_create(user=user)

        # Loop through all forms and update profile
        for form in form_list:
            data = form.cleaned_data

            if isinstance(form, PersonalDetailsForm):
                user.first_name = data["first_name"]
                user.last_name = data["last_name"]
                profile.gender = data["gender"]

            elif isinstance(form, AcademicDetailsForm):
                profile.class_level = data["class_level"]
                profile.stream = data["stream"]

            elif isinstance(form, SubjectChoiceForm):
                profile.enrolled_subjects.set(data["favourite_subjects"])

            elif isinstance(form, ProfilePictureForm):
                if data.get("profile_picture"):
                    profile.profile_picture = data["profile_picture"]

        # Save both User and Profile
        user.save()
        profile.onboarding_complete = True
        profile.save()

        # Redirect to dashboard after onboarding
        return redirect("home")
    
    
@login_required(login_url='/login/')
def Reports(req):
    return render(req, 'students/reports.html')

