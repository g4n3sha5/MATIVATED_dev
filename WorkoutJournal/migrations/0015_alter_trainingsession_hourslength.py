# Generated by Django 4.1.2 on 2023-05-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkoutJournal', '0014_trainingsession_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingsession',
            name='hoursLength',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
