from django.urls import path, re_path
from . import views
from users.views import ResetPasswordView

urlpatterns = [
    path('', views.home_page , name='home_page'),
    path('society_guidelines/', views.society_guidelines, name="society_guidelines"),
    path('user_profile/', views.user_profile, name="user_profile"),
]