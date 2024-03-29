# Generated by Django 2.2.3 on 2019-07-20 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bys', '0017_auto_20190721_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atıf',
            name='akademisyen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bys.NewUserModel'),
        ),
        migrations.AlterField(
            model_name='etkinlik',
            name='akademisyen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bys.NewUserModel'),
        ),
        migrations.AlterField(
            model_name='faliyet',
            name='akademisyen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bys.NewUserModel'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='akademisyen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bys.NewUserModel'),
        ),
        migrations.AlterField(
            model_name='proje',
            name='akademisyen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bys.NewUserModel'),
        ),
        migrations.AlterField(
            model_name='yayın',
            name='akademisyen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bys.NewUserModel'),
        ),
        migrations.AlterField(
            model_name='ödül',
            name='akademisyen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bys.NewUserModel'),
        ),
    ]
