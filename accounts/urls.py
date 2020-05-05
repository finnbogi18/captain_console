from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='accounts-index'),
    path('login', LoginView.as_view(template_name='accounts/login.html'), name='accounts-login'),
    path('register', views.register, name='accounts-register'),
    path('logout', LogoutView.as_view(next_page='accounts-login'), name='accounts-logout'),
]