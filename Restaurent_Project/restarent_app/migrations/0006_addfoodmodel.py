# Generated by Django 3.2 on 2021-06-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restarent_app', '0005_auto_20210612_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddFoodModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rname', models.CharField(max_length=30)),
                ('dname', models.CharField(max_length=40)),
                ('dtype', models.CharField(max_length=19)),
                ('dcat', models.CharField(max_length=20, null=True)),
                ('dprice', models.IntegerField()),
                ('image1', models.FileField(upload_to='')),
                ('image2', models.FileField(upload_to='')),
                ('image3', models.FileField(null=True, upload_to='')),
                ('image4', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]