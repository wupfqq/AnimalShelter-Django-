# Generated by Django 3.0.7 on 2021-08-20 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0009_auto_20210820_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='photo',
            field=models.ImageField(upload_to='photo/'),
        ),
    ]
