# Generated by Django 4.1.2 on 2023-02-03 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_register', '0007_alter_userprofile_belt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='firstName',
            field=models.CharField(blank=True, default='User', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lastName',
            field=models.CharField(blank=True, default='Anonymous', max_length=20, null=True),
        ),
    ]