# Generated by Django 4.0.6 on 2022-07-21 21:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userpreferences', '0002_auto_20220721_2115'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserPreferences',
            new_name='UserPreference',
        ),
    ]