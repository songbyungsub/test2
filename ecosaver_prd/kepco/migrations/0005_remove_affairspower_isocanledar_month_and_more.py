# Generated by Django 4.1.7 on 2024-01-29 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kepco', '0004_affairspower_isocanledar_month_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='affairspower',
            name='isocanledar_month',
        ),
        migrations.RemoveField(
            model_name='affairspower',
            name='isocanledar_week',
        ),
        migrations.RemoveField(
            model_name='affairspower',
            name='isocanledar_year',
        ),
    ]
