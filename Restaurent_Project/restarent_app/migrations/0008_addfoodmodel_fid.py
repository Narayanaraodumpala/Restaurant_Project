# Generated by Django 3.2 on 2021-06-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restarent_app', '0007_restaurentmodel_rest_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='addfoodmodel',
            name='fid',
            field=models.IntegerField(default=False),
        ),
    ]
