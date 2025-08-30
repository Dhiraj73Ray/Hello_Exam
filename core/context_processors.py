from students.models import StudentProfile

def profile_context(request):
    if request.user.is_authenticated:
        try:
            profile = StudentProfile.objects.get(user=request.user)
            return {"profile": profile}
        except StudentProfile.DoesNotExist:
            return {"profile": None}
    return {"profile": None}
