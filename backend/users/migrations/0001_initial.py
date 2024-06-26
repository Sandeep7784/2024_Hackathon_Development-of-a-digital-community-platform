# Generated by Django 4.2.3 on 2024-02-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cookie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(max_length=50)),
                ("cookie", models.CharField(max_length=40)),
                ("expiry", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("userId", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("password", models.CharField(max_length=500)),
                ("user_type", models.IntegerField()),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
            ],
        ),
    ]
