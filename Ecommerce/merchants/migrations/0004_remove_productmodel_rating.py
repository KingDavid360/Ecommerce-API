# Generated by Django 4.1.7 on 2023-04-11 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0003_productmodel_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='rating',
        ),
    ]
