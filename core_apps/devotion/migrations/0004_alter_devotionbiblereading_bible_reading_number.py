# Generated by Django 4.2.5 on 2023-11-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("devotion", "0003_alter_devotionbiblereading_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="devotionbiblereading",
            name="bible_reading_number",
            field=models.PositiveIntegerField(
                blank=True, verbose_name="Bible Reading Number"
            ),
        ),
    ]