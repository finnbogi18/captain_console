from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="accounts-index"),
    path('login',views.login,name="accounts-login"),
]