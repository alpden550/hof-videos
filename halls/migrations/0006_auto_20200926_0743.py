# Generated by Django 3.0.7 on 2020-09-26 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('halls', '0005_auto_20200926_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='halls', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
