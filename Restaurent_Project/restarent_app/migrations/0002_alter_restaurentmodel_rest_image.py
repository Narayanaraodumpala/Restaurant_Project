# Generated by Django 3.2 on 2021-06-11 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restarent_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurentmodel',
            name='rest_image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]