# Generated by Django 5.0.2 on 2024-03-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_rename_datetime_event_date_and_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
