# Generated by Django 4.1.2 on 2023-01-24 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Clubs', '0008_rename_location_club_address_club_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('memberType', models.CharField(choices=[('Authorized', 'authorized'), ('Instructor', 'instructor'), ('Student', 'student')], max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='club',
            name='authorizedUser',
        ),
        migrations.RemoveField(
            model_name='club',
            name='instructors',
        ),
        migrations.CreateModel(
            name='UserMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membershipType', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userMembershipType', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userMembership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='Clubs.club')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userRequest', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]