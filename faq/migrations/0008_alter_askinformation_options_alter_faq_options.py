# Generated by Django 4.2 on 2024-01-12 02:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("faq", "0007_alter_askinformation_reg_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="askinformation",
            options={"verbose_name": "1대1 문의", "verbose_name_plural": "1대1 문의"},
        ),
        migrations.AlterModelOptions(
            name="faq",
            options={"verbose_name": "FAQ", "verbose_name_plural": "FAQ"},
        ),
    ]
