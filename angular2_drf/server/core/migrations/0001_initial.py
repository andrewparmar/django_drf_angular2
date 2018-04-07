# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-03 05:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(help_text='Enter Family Reference', max_length=13)),
                ('title', models.CharField(help_text='Enter Family Title', max_length=200)),
                ('description', models.TextField(help_text='Enter Family Description')),
                ('unit', models.CharField(help_text='Enter Family Unit ', max_length=10)),
                ('minQuantity', models.FloatField(help_text='Enter Family Min Quantity')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(help_text='Enter Location Reference', max_length=20)),
                ('title', models.CharField(help_text='Enter Location Title', max_length=200)),
                ('description', models.TextField(help_text='Enter Location Description')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(help_text='Enter Product Stock Keeping Unit', max_length=13)),
                ('barcode', models.CharField(help_text='Enter Product Barcode (ISBN, UPC ...)', max_length=13)),
                ('title', models.CharField(help_text='Enter Product Title', max_length=200)),
                ('description', models.TextField(help_text='Enter Product Description')),
                ('unitCost', models.FloatField(help_text='Enter Product Unit Cost')),
                ('unit', models.CharField(help_text='Enter Product Unit ', max_length=10)),
                ('quantity', models.FloatField(help_text='Enter Product Quantity')),
                ('minQuantity', models.FloatField(help_text='Enter Product Min Quantity')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Family')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(help_text='Enter Product Stock Keeping Unit', max_length=13)),
                ('barcode', models.CharField(help_text='Enter Product Barcode (ISBN, UPC ...)', max_length=13)),
                ('comment', models.TextField(help_text='Enter Product Stock Keeping Unit')),
                ('unitCost', models.FloatField(help_text='Enter Product Unit Cost')),
                ('quantity', models.FloatField(help_text='Enter Product Quantity')),
                ('date', models.DateField(blank=True, null=True)),
                ('reason', models.CharField(blank=True, choices=[('ns', 'New Stock'), ('ur', 'Usable Return'), ('nr', 'Unusable Return')], default='ns', help_text='Reason for transaction', max_length=2)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product')),
            ],
        ),
    ]
