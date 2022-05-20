# Generated by Django 4.0.4 on 2022-05-18 02:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0006_clientdocuments_user_clientperson_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_name', models.CharField(max_length=90)),
                ('starting_date', models.DateField(blank=True)),
                ('ending_date', models.DateField(blank=True)),
                ('payment_date', models.DateField(blank=True)),
                ('payment_method', models.CharField(choices=[('IC', 'In cash'), ('IS', 'Installments'), ('EX', 'Exchange')], default='IC', max_length=20)),
                ('status', models.CharField(choices=[('PD', 'Payd'), ('PN', 'Pending'), ('CC', 'Cancelled')], default='PN', max_length=20)),
                ('value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('invoice', models.CharField(blank=True, max_length=90)),
                ('description', models.TextField(blank=True, null=True)),
                ('company_client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.clientcompany')),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.clientdocuments')),
                ('person_client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.clientperson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]