# Generated by Django 4.0.4 on 2022-05-16 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('company_cnpj', models.IntegerField()),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('pending_payments', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('received_payments', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClientPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=90)),
                ('cpf', models.IntegerField()),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('pending_payments', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('received_payments', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('person_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.clientcompany')),
            ],
        ),
        migrations.CreateModel(
            name='ClientDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='clients_files')),
                ('client_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.clientcompany')),
                ('client_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.clientperson')),
            ],
        ),
    ]
