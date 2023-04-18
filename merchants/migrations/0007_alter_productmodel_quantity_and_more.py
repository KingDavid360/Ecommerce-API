# Generated by Django 4.1.7 on 2023-04-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0006_alter_productmodel_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='quantity',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='ratings',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=5),
        ),
    ]
