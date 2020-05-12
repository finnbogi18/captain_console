from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('login', LoginView.as_view(template_name='accounts/login.html'), name='accounts-login'),
    path('register', views.register, name='accounts-register'),
    path('logout', LogoutView.as_view(next_page='accounts-login'), name='accounts-logout'),
    path('profile', views.profile, name='accounts-profile'),
    path('profile/edit', views.edit, name='accounts-edit'),
    path('profile/searchhistory', views.search_history, name='accounts-searchhistory'),
    path('profile/searchhistory/clear', views.clear_search, name='accounts-clearhistory'),
]