from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Profile(User):
    profile_image = models.CharField(max_length=9999, blank=True)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return User.first_name


class SearchHistory(models.Model):
    search = models.CharField(max_length=999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.search


def add_history(search,user):
    history = SearchHistory()
    history.search = search
    history.user = user
    history.save()