# Generated by Django 4.0.3 on 2022-03-03 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthappdata', '0002_rename_name_order_medname_alter_meds_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=100),
        ),
    ]
