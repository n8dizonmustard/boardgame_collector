# Generated by Django 3.1.7 on 2021-04-01 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210401_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='price',
        ),
    ]
