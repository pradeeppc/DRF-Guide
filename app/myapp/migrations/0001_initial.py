# Generated by Django 2.1.15 on 2022-01-06 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('sku_id', models.PositiveIntegerField(blank=True, null=True)),
                ('product_id', models.PositiveIntegerField(blank=True, null=True)),
                ('sku_name', models.CharField(max_length=512)),
                ('price', models.DecimalField(decimal_places=10, default=0, max_digits=20)),
                ('manufacturer', models.CharField(max_length=512)),
                ('salt_name', models.CharField(max_length=512)),
                ('drug_form', models.CharField(max_length=256)),
                ('pack_size', models.CharField(max_length=256)),
                ('strength', models.CharField(max_length=256)),
                ('is_banned', models.BooleanField(default=False)),
                ('unit', models.CharField(blank=True, max_length=256, null=True)),
                ('price_per_unit', models.DecimalField(decimal_places=10, default=0, max_digits=20)),
            ],
            options={
                'db_table': 'drug',
            },
        ),
    ]