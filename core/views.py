from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm, CustomRegisterForm
from students.models import StudentProfile

# Create your views here.
@login_required(login_url='/login/')
def Dashboard(req):
    return render(req, 'core/Dashboard.html')

def Login_View(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # form = AuthenticationForm(data=request.POST)
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "core/login.html", {"form": form})


def Logout_View(request):
    logout(request)
    return redirect("login")


def Register_View(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            StudentProfile.objects.create(user=user)
            login(request, user)
            return redirect('/onboarding')
    else:
        form = CustomRegisterForm()
    return render(request, "core/register.html", {'form': form})

def Profile_Icon(request):
    profile = get_object_or_404(StudentProfile, user=request.user)

    return render(request, "core/components/Navbar.html", {"profile": profile})