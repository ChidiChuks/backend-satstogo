# Generated by Django 4.2.11 on 2024-08-26 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_attendance_locked'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsession',
            name='deadline_string',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]