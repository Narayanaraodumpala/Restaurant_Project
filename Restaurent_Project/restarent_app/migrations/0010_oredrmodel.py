# Generated by Django 3.2 on 2021-06-28 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restarent_app', '0009_addtocartmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OredrModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('fullname', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=50)),
                ('payment_status', models.CharField(default='Not Done', max_length=500)),
                ('amount', models.FloatField(null=True)),
                ('order_status', models.CharField(max_length=50, null=True)),
                ('pro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restarent_app.addfoodmodel')),
                ('usr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
