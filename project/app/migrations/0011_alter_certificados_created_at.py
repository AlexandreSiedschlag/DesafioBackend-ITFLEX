# Generated by Django 4.0.3 on 2022-04-05 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_certificados_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificados',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 4, 5, 15, 41, 8, 783177)),
        ),
    ]
