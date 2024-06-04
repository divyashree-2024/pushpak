# Generated by Django 5.0.6 on 2024-06-04 10:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_useraddress_table"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="useraddress",
            unique_together={("user", "address_name")},
        ),
    ]
