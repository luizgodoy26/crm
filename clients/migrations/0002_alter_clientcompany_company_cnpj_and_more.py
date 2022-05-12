# Generated by Django 4.0.4 on 2022-05-10 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcompany',
            name='company_cnpj',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clientcompany',
            name='company_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='clientcompany',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='clientcompany',
            name='pending_payments',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='clientcompany',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='clientcompany',
            name='received_payments',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='clientperson',
            name='cpf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clientperson',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='clientperson',
            name='pending_payments',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='clientperson',
            name='person_company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.clientcompany'),
        ),
        migrations.AlterField(
            model_name='clientperson',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='clientperson',
            name='received_payments',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
    ]
