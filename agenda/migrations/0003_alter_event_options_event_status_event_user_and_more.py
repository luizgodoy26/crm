# Generated by Django 4.0.4 on 2022-05-21 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0002_alter_event_end_time_alter_event_start_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['status']},
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
