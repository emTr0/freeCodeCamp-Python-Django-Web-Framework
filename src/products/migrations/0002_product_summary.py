# Generated by Django 4.1.4 on 2022-12-08 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="summary",
            field=models.TextField(default="This is cool!"),
        ),
    ]
