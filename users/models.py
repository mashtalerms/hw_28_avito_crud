from django.db import models

from ads.models.location import Location


class User(models.Model):

    ROLE = [("member", "Member"), ("moderator", "Moderator"), ("admin", "Admin")]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=40, unique=True, blank=False, null=False)
    password = models.CharField(max_length=30, unique=True, blank=False, null=False)
    role = models.CharField(choices=ROLE, max_length=9, default='member')
    age = models.PositiveSmallIntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['username']

    def __str__(self):
        return self.first_name
