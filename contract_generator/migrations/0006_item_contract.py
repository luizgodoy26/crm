# Generated by Django 4.0.4 on 2022-06-12 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
        ('contract_generator', '0005_remove_item_total_clientcontract_total_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contracts.contract'),
        ),
    ]
