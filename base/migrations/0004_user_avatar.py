# Generated by Django 4.2.8 on 2024-01-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_alter_user_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(default="avatar.svg", null=True, upload_to=""),
        ),
    ]
