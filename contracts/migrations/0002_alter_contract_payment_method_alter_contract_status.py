# Generated by Django 4.0.4 on 2022-07-03 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='payment_method',
            field=models.CharField(choices=[('In cash', 'In cash'), ('Installments', 'Installments'), ('Exchange', 'Exchange')], default='In cash', max_length=20),
        ),
        migrations.AlterField(
            model_name='contract',
            name='status',
            field=models.CharField(choices=[('Payd', 'Payd'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20),
        ),
    ]
