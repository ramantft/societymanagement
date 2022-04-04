from django.urls import path, re_path
from . import views
from users.views import ResetPasswordView

urlpatterns = [
    path('', views.home_page , name='home_page'),
]