# students/forms.py

from django import forms
from .models import StudentProfile
from subjects.models import Subject
from django.contrib.auth.models import User


class PersonalDetailsForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    # gender = forms.ChoiceField(choices=[
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    # ])
    gender = forms.ChoiceField(choices=StudentProfile.GENDER_CHOICES)

class AcademicDetailsForm(forms.Form):
    # class_level = forms.ChoiceField(choices=StudentProfile._meta.get_field('class_level').choices)
    class_level = forms.ChoiceField(choices=StudentProfile.CLASS_CHOICES)
    # stream = forms.ChoiceField(choices=StudentProfile._meta.get_field('stream').choices)
    stream = forms.ChoiceField(choices=StudentProfile.STREAM_CHOICES)


class SubjectChoiceForm(forms.Form):
    favourite_subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.filter(is_active=True),
        widget=forms.SelectMultiple(attrs={"id": "id_fav_subjects"}),
        required=False
    )
    def __init__(self, *args, **kwargs):
        class_choice = kwargs.pop("class_choice", None)
        stream_choice = kwargs.pop("stream_choice", None)
        super().__init__(*args, **kwargs)

        qs = Subject.objects.all()
        if class_choice:
            qs = qs.filter(class_level=class_choice)
        if stream_choice:
            qs = qs.filter(stream=stream_choice)

        self.fields["favourite_subjects"].queryset = qs
    def clean_favourite_subjects(self):
        subjects = self.cleaned_data.get("favourite_subjects")
        if not subjects or len(subjects) < 1:
            raise forms.ValidationError("Please select at least one subject.")
        return subjects


class ProfilePictureForm(forms.Form):
    profile_picture = forms.ImageField(required=False)


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['phone', 'dob', 'gender', 'class_level', 'stream', 'address', 'profile_picture']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']