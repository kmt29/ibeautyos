# Generated by Django 3.1 on 2020-10-14 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201015_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='test',
        ),
    ]
