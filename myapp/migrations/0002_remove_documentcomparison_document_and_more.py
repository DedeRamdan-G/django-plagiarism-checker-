# Generated by Django 5.0.6 on 2024-09-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="documentcomparison",
            name="document",
        ),
        migrations.AddField(
            model_name="documentcomparison",
            name="document1",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="documentcomparison",
            name="document2",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name="Document",
        ),
    ]