# Generated by Django 3.2 on 2021-06-11 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restarent_app', '0002_alter_restaurentmodel_rest_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurentmodel',
            name='rest_email',
        ),
        migrations.RemoveField(
            model_name='restaurentmodel',
            name='rest_password',
        ),
    ]
