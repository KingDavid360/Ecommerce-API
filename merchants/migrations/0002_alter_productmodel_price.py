# Generated by Django 4.1.7 on 2023-04-01 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=11),
        ),
    ]
