# Generated by Django 4.1.2 on 2023-03-30 12:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WorkoutJournal', '0013_trainingsession_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingsession',
            name='participants',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]