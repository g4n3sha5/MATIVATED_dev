# Generated by Django 4.1.2 on 2023-03-18 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WorkoutJournal', '0010_remove_trainingsession_user_trainingsession_club_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingsession',
            name='user',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='userOwner', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]