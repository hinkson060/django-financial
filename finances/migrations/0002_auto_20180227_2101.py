# Generated by Django 2.0.2 on 2018-02-28 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crypto',
            old_name='crypto_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='crypto',
            old_name='crypto_owner',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='crypto',
            old_name='crypto_symbol',
            new_name='symbol',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='stock_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='stock_owner',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='stock_purchase_date',
            new_name='purchase_date',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='stock_purchase_price',
            new_name='purchase_price',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='stock_quantity_owned',
            new_name='quantity_owned',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='stock_symbol',
            new_name='symbol',
        ),
    ]
