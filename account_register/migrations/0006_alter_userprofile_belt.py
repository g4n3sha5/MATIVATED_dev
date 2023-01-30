# Generated by Django 4.1.2 on 2023-01-01 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_register', '0005_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='belt',
            field=models.CharField(choices=[('NoInfo', 'No Info'), ('WhiteBelt', 'White Belt'), ('BlueBelt', 'Blue Belt'), ('PurpleBelt', 'Purple Belt'), ('BrownBelt', 'Brown Belt'), ('BlackBelt', 'Black Belt')], default='NoInfo', max_length=16),
        ),
    ]