from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import LoginFormWithCaptcha
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html', next_page='profiles'), name='login'),
    path('profiles/', views.profile_list_view, name='profiles'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', LoginView.as_view(
    template_name='users/login.html', 
    authentication_form=LoginFormWithCaptcha,
    next_page='profiles'
), name='login'),
]