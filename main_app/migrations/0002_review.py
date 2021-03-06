# Generated by Django 3.1.7 on 2021-03-31 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.IntegerField()),
                ('stars', models.CharField(choices=[('1', 'Boring'), ('2', 'Okay'), ('3', 'Fun'), ('4', 'Great'), ('5', 'Awesome')], default='1', max_length=1)),
                ('boardgame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.boardgame')),
            ],
        ),
    ]
