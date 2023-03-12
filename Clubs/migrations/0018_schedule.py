# Generated by Django 4.1.2 on 2023-02-18 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clubs', '0017_alter_usermembership_authorized'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownerClub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clubs.club')),
            ],
        ),
    ]