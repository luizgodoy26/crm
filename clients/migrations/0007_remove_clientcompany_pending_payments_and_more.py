# Generated by Django 4.0.4 on 2022-06-24 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_clientdocuments_user_clientperson_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientcompany',
            name='pending_payments',
        ),
        migrations.RemoveField(
            model_name='clientcompany',
            name='received_payments',
        ),
        migrations.RemoveField(
            model_name='clientperson',
            name='pending_payments',
        ),
        migrations.RemoveField(
            model_name='clientperson',
            name='received_payments',
        ),
    ]
