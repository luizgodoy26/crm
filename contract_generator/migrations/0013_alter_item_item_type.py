# Generated by Django 4.0.4 on 2022-07-03 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract_generator', '0012_rename_original_contract_clientcontract_work_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('Equipment', 'Equipment'), ('Labor', 'Labor'), ('Material', 'Material')], default='Material', max_length=20),
        ),
    ]