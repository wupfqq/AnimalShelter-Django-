# Generated by Django 3.0.7 on 2021-08-20 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0010_auto_20210820_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='photo',
            field=models.ImageField(upload_to='static/photo'),
        ),
    ]