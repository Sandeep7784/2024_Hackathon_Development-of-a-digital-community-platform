# Generated by Django 5.0.2 on 2024-02-29 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cookie',
            name='expiry',
        ),
    ]
