# Generated by Django 4.0.1 on 2022-08-21 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0009_alter_ad_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='address',
        ),
    ]
