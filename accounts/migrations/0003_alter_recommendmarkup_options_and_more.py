# Generated by Django 4.2 on 2024-01-13 01:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_recommendmarkup_reservationuser"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="recommendmarkup",
            options={"verbose_name": "화장품추천", "verbose_name_plural": "화장품추천"},
        ),
        migrations.AlterField(
            model_name="reservationuser",
            name="consultResult",
            field=models.CharField(
                blank=True,
                choices=[
                    ("SPRINGBRIGHT", "봄 브라이트"),
                    ("SPRINGTRUE", "봄 트루"),
                    ("SUMMERBRIGHT", "여름 브라이트"),
                    ("SUMMERMUTE", "여름 트루"),
                    ("FALLBRIGHT", "가을 브라이트"),
                    ("FALLTRUE", "가을 트루"),
                    ("FALLDEEP", "가을 딥"),
                    ("WINTERBRIGHT", "겨울 브라이트"),
                    ("WINTERDEEP", "겨울 딥"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="reservationuser",
            name="consultResult02",
            field=models.CharField(
                blank=True,
                choices=[
                    ("SPRINGBRIGHT", "봄 브라이트"),
                    ("SPRINGTRUE", "봄 트루"),
                    ("SUMMERBRIGHT", "여름 브라이트"),
                    ("SUMMERMUTE", "여름 트루"),
                    ("FALLBRIGHT", "가을 브라이트"),
                    ("FALLTRUE", "가을 트루"),
                    ("FALLDEEP", "가을 딥"),
                    ("WINTERBRIGHT", "겨울 브라이트"),
                    ("WINTERDEEP", "겨울 딥"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
