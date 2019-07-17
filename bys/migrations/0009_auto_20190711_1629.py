# Generated by Django 2.2.3 on 2019-07-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bys', '0008_auto_20190711_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atıf',
            name='tarih',
            field=models.CharField(blank=True, db_column='Tarih', default='gg/aa/yyyy', max_length=10, null=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='etkinlik',
            name='tarih',
            field=models.CharField(blank=True, db_column='Tarih', default='gg/aa/yyyy', max_length=10, null=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='faliyet',
            name='tarih',
            field=models.CharField(blank=True, db_column='Tarih', default='gg/aa/yyyy', max_length=10, null=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='tarih',
            field=models.CharField(blank=True, db_column='Tarih', default='gg/aa/yyyy', max_length=10, null=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='proje',
            name='tarih',
            field=models.CharField(blank=True, db_column='Tarih', default='gg/aa/yyyy', max_length=10, null=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='yayın',
            name='tarih',
            field=models.CharField(blank=True, db_column='Tarih', default='gg/aa/yyyy', max_length=10, null=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='ödül',
            name='tarih',
            field=models.CharField(blank=True, db_column='Tarih', default='gg/aa/yyyy', max_length=10, null=True, verbose_name='Tarih'),
        ),
    ]