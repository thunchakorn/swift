# Generated by Django 5.0.4 on 2024-06-28 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apis", "0002_classroom_school"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classroom",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="classrooms",
                to="apis.school",
            ),
        ),
    ]
