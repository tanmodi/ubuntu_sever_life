# Generated by Django 4.1.5 on 2023-01-18 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_register_mobile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register',
        ),
    ]