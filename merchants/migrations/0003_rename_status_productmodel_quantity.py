# Generated by Django 4.1.7 on 2023-04-01 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0002_alter_productmodel_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='status',
            new_name='quantity',
        ),
    ]