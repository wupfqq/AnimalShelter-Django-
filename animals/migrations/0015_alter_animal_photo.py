# Generated by Django 3.2.6 on 2021-08-20 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0014_alter_animal_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='photo',
            field=models.ImageField(upload_to='photo/'),
        ),
    ]
