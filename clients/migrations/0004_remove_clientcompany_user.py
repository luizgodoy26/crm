# Generated by Django 4.0.4 on 2022-05-17 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_clientcompany_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientcompany',
            name='user',
        ),
    ]