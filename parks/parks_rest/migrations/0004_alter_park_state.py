# Generated by Django 4.0.3 on 2022-07-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parks_rest', '0003_alter_park_state 2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='state',
            field=models.CharField(max_length=250),
        ),
    ]
