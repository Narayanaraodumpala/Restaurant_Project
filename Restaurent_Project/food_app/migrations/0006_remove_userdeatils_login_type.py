# Generated by Django 3.2 on 2021-07-09 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0005_userdeatils_login_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdeatils',
            name='login_type',
        ),
    ]
