# Generated by Django 3.2 on 2021-06-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restarent_app', '0003_auto_20210611_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurentmodel',
            name='rest_type',
            field=models.CharField(max_length=16, null=True),
        ),
    ]