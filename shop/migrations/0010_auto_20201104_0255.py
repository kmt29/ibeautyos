# Generated by Django 3.1 on 2020-11-03 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20201104_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogimage',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='BlogImage',
        ),
    ]