# Generated by Django 3.1 on 2020-11-04 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20201104_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discounted_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='is_discount',
            field=models.BooleanField(default=False),
        ),
    ]