# Generated by Django 2.2.5 on 2019-09-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_search_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='map',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
