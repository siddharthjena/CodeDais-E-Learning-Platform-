# Generated by Django 5.0.2 on 2024-07-07 13:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeDaisApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='link',
            field=models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]
