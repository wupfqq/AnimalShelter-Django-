# Generated by Django 3.2.6 on 2021-08-20 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0013_auto_20210820_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='photo',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]