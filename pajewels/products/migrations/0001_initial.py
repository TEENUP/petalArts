# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 11:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import durationfield.db.models.fields.duration


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=False, max_digits=100)),
                ('primaryImage', models.ImageField(upload_to='products/images/')),
                ('secondaryImage', models.ImageField(upload_to='products/images/')),
                ('additionalImage', models.ImageField(upload_to='products/images/')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.Product')),
                ('timePeriod', durationfield.db.models.fields.duration.DurationField()),
                ('returnOnInvestment', models.DecimalField(decimal_places=2, default=False, max_digits=100)),
                ('returnOnRefferal', models.DecimalField(decimal_places=2, default=False, max_digits=100)),
            ],
            bases=('products.product',),
        ),
    ]
