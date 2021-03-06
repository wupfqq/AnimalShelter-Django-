# Generated by Django 3.0.7 on 2021-08-18 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('gender', models.CharField(max_length=6)),
                ('age', models.DecimalField(decimal_places=1, max_digits=10)),
                ('appearence', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photo/')),
                ('available', models.BooleanField(default=False)),
            ],
        ),
    ]
