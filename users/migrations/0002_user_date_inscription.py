# Generated by Django 5.1.2 on 2024-10-28 14:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_inscription',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
