# Generated by Django 4.1.7 on 2023-04-01 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0004_rename_descriptiom_productmodel_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='quantity',
            field=models.CharField(blank=True, default=0, max_length=100),
        ),
    ]
