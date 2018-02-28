# Generated by Django 2.0.2 on 2018-02-28 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crypto_symbol', models.CharField(max_length=5)),
                ('crypto_name', models.CharField(max_length=50)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('purchase_date', models.DateField()),
                ('quantity_owned', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address_line_1', models.CharField(max_length=50)),
                ('address_line_2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=6)),
                ('email', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_symbol', models.CharField(max_length=5)),
                ('stock_name', models.CharField(max_length=50)),
                ('stock_purchase_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock_purchase_date', models.DateField()),
                ('stock_quantity_owned', models.IntegerField()),
                ('stock_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='crypto',
            name='crypto_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.Customer'),
        ),
    ]
