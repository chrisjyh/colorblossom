# Generated by Django 4.2 on 2024-01-16 01:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_alter_recommendmarkup_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="recommendmarkup",
            name="tool",
            field=models.CharField(
                blank=True,
                choices=[
                    ("BASE", "베이스"),
                    ("SHADOW", "쉐도우"),
                    ("BLUSHER", "블러셔"),
                    ("LIP", "립"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="reservationuser",
            name="memo",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="recommendmarkup",
            name="type",
            field=models.CharField(
                choices=[
                    ("SPRINGBLIGHT", "봄 브라이트"),
                    ("SPRINGLIGHT", "봄 라이트"),
                    ("SUMMERBLIGHT", "여름 브라이트"),
                    ("SUMMERLIGHT", "여름 라이트"),
                    ("SUMMERMUTE", "여름 뮤트"),
                    ("FALLMUTE", "가을 뮤트"),
                    ("FALLDEEP", "가을 딥"),
                    ("WINTERBLIGHT", "겨울 브라이트"),
                    ("WINTERDEEP", "겨울 딥"),
                ],
                default="SPRINGBLIGHT",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="reservationuser",
            name="consultResult",
            field=models.CharField(
                blank=True,
                choices=[
                    ("SPRINGBLIGHT", "봄 브라이트"),
                    ("SPRINGLIGHT", "봄 라이트"),
                    ("SUMMERBLIGHT", "여름 브라이트"),
                    ("SUMMERLIGHT", "여름 라이트"),
                    ("SUMMERMUTE", "여름 뮤트"),
                    ("FALLMUTE", "가을 뮤트"),
                    ("FALLDEEP", "가을 딥"),
                    ("WINTERBLIGHT", "겨울 브라이트"),
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
                    ("SPRINGBLIGHT", "봄 브라이트"),
                    ("SPRINGLIGHT", "봄 라이트"),
                    ("SUMMERBLIGHT", "여름 브라이트"),
                    ("SUMMERLIGHT", "여름 라이트"),
                    ("SUMMERMUTE", "여름 뮤트"),
                    ("FALLMUTE", "가을 뮤트"),
                    ("FALLDEEP", "가을 딥"),
                    ("WINTERBLIGHT", "겨울 브라이트"),
                    ("WINTERDEEP", "겨울 딥"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
