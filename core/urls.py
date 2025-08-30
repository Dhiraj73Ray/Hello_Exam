

from django.urls import path

from .views import Dashboard, Login_View, Logout_View, Register_View


urlpatterns = [
    path('', Dashboard, name="home"),
    path('login/', Login_View, name="login"),
    path('logout/', Logout_View, name="logout"),
    path('register/', Register_View, name="register"),

]
