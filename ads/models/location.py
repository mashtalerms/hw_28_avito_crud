from django.db import models


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    lat = models.CharField(max_length=30, blank=False, null=False)
    lng = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name
