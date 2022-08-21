from django.db import models

from ads.models.category import Category
from users.models import User


class Ad(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    is_published = models.BooleanField(default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="images/", null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["id"]

    def __str__(self):
        return self.name
