# Generated by Django 3.1.7 on 2021-03-17 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingapp', '0002_lot_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='nickname',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
