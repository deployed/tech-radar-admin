# Generated by Django 5.1.4 on 2025-01-14 15:07

import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("radars", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Segment",
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
                ("label", models.CharField(max_length=20)),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True, editable=False, populate_from="label"
                    ),
                ),
                (
                    "radar",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="radars.radar",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Technology",
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
                ("label", models.CharField(max_length=50)),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True, editable=False, populate_from="label"
                    ),
                ),
                ("link", models.URLField(max_length=150)),
                (
                    "ring",
                    models.CharField(
                        choices=[
                            ("adopt", "adopt"),
                            ("hold", "hold"),
                            ("assess", "assess"),
                            ("trial", "trial"),
                        ],
                        default="adopt",
                        max_length=7,
                    ),
                ),
                (
                    "segment",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="radars.segment",
                    ),
                ),
            ],
            options={
                "verbose_name": "Technology",
                "verbose_name_plural": "Technologies",
            },
        ),
    ]
