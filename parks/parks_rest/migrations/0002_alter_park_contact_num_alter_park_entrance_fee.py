# Generated by Django 4.0.3 on 2022-07-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parks_rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='contact_num',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='park',
            name='entrance_fee',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
