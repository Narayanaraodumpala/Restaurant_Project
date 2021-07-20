# Generated by Django 3.2 on 2021-06-23 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restarent_app', '0008_addfoodmodel_fid'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddtocartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restarent_app.addfoodmodel')),
                ('usr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
