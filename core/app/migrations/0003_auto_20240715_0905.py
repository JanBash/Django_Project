# Generated by Django 3.2.12 on 2024-07-15 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20240715_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='file',
            field=models.FileField(upload_to='asd/'),
        ),
        migrations.AlterField(
            model_name='film',
            name='picture',
            field=models.ImageField(upload_to='asd/'),
        ),
    ]
