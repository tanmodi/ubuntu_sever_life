# Generated by Django 2.2.5 on 2019-09-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=250)),
                ('email', models.CharField(blank=True, max_length=500)),
                ('phone', models.CharField(blank=True, max_length=250)),
                ('map', models.CharField(blank=True, max_length=250)),
                ('city', models.CharField(blank=True, max_length=250)),
            ],
        ),
    ]
