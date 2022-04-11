# Generated by Django 4.0.3 on 2022-04-05 19:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_certificados_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificados',
            name='groups',
            field=models.CharField(blank=True, choices=[('1', 'ADM'), ('15', 'COMERCIAL'), ('30', 'RH')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='certificados',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 5, 16, 49, 32, 559956)),
        ),
    ]