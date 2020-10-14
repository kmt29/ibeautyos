# Generated by Django 3.1 on 2020-10-14 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Webcontent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_1', models.TextField(blank=True)),
                ('lead_2', models.TextField(blank=True)),
                ('topic_1', models.TextField(blank=True)),
                ('topic_2', models.TextField(blank=True)),
                ('topic_3', models.TextField(blank=True)),
                ('content_1', models.TextField(blank=True)),
                ('content_2', models.TextField(blank=True)),
                ('content_3', models.TextField(blank=True)),
                ('lead_1_mm', models.TextField(blank=True)),
                ('lead_2_mm', models.TextField(blank=True)),
                ('topic_1_mm', models.TextField(blank=True)),
                ('topic_2_mm', models.TextField(blank=True)),
                ('topic_3_mm', models.TextField(blank=True)),
                ('content_1_mm', models.TextField(blank=True)),
                ('content_2_mm', models.TextField(blank=True)),
                ('content_3_mm', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('is_stock', models.BooleanField(default=True)),
                ('is_feature', models.BooleanField(default=False)),
                ('price', models.IntegerField(default=0)),
                ('tag', models.ManyToManyField(blank=True, to='shop.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
            ],
        ),
    ]
