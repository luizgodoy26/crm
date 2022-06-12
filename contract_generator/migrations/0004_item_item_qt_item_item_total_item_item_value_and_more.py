# Generated by Django 4.0.4 on 2022-06-10 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract_generator', '0003_remove_clientcontract_company_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_qt',
            field=models.FloatField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='item_total',
            field=models.FloatField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='item_value',
            field=models.FloatField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='total',
            field=models.FloatField(blank=True, max_length=12, null=True),
        ),
    ]