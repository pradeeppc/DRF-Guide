# Generated by Django 2.1.15 on 2022-01-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='product_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='drug',
            name='sku_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
