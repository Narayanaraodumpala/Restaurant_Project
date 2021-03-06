# Generated by Django 3.2 on 2021-06-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restarent_app', '0011_auto_20210628_0535'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo_id', models.CharField(max_length=10)),
                ('promo_code', models.CharField(max_length=10)),
                ('prome_name', models.CharField(default=True, max_length=20, null=True)),
                ('promo_discription', models.CharField(default=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(null=True)),
                ('valid_upto', models.DateTimeField(null=True)),
            ],
        ),
    ]
