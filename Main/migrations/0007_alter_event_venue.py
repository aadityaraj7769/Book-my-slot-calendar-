# Generated by Django 5.0.2 on 2024-03-17 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_merge_20240317_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
