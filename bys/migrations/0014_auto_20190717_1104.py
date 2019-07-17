# Generated by Django 2.2.3 on 2019-07-17 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bys', '0013_auto_20190717_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atıf',
            name='tarih',
            field=models.CharField(db_column='Tarih', default=datetime.date.today, max_length=10, null=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='etkinlik',
            name='tarih',
            field=models.CharField(db_column='Tarih', default=datetime.date.today, max_length=10, null=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='faliyet',
            name='tarih',
            field=models.CharField(db_column='Tarih', default=datetime.date.today, max_length=10, null=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='tarih',
            field=models.CharField(db_column='Tarih', default=datetime.date.today, max_length=10, null=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='proje',
            name='tarih',
            field=models.CharField(db_column='Tarih', default=datetime.date.today, max_length=10, null=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='yayın',
            name='tarih',
            field=models.CharField(db_column='Tarih', default=datetime.date.today, max_length=10, null=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='ödül',
            name='tarih',
            field=models.CharField(db_column='Tarih', default=datetime.date.today, max_length=10, null=True, verbose_name='Tarih'),
        ),
    ]
