# Generated by Django 4.1.6 on 2023-03-02 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Тип'),
        ),
    ]