# Generated by Django 3.2 on 2022-08-11 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='nip',
            field=models.CharField(db_index=True, max_length=8, verbose_name='NIP'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nip',
            field=models.CharField(max_length=8, unique=True, verbose_name='NIP'),
        ),
    ]
