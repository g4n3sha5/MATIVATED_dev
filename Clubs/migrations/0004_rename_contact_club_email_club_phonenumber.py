# Generated by Django 4.1.2 on 2023-01-10 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clubs', '0003_alter_club_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='contact',
            new_name='email',
        ),
        migrations.AddField(
            model_name='club',
            name='phoneNumber',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
