from django.shortcuts import redirect
from django.urls import reverse

class OnboardingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If user is not authenticated, let them continue (login/registration will handle)
        if not request.user.is_authenticated:
            return self.get_response(request)

        # Get profile safely
        profile = getattr(request.user, "studentprofile", None)

        # Skip middleware if profile missing (like for admins/staff)
        if not profile:
            return self.get_response(request)

        # Define exempt URLs → these routes should always be allowed
        exempt_paths = [
            reverse("onboarding"),  # wizard view
            reverse("logout"),
            reverse("admin:index"),
        ]

        if not profile.onboarding_complete:
            if request.path not in exempt_paths and not request.path.startswith("/admin/"):
                # Redirect to onboarding if not finished
                return redirect("onboarding")

        return self.get_response(request)
