# Generated by Django 4.0.4 on 2022-04-17 13:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d3app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='age',
            name='age',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]