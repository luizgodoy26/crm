# Generated by Django 4.0.4 on 2022-05-10 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_alter_clientdocuments_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientcompany',
            name='files',
            field=models.ManyToManyField(blank=True, null=True, to='clients.clientdocuments'),
        ),
    ]
