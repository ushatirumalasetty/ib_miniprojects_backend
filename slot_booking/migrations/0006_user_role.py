# Generated by Django 2.2.1 on 2020-06-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slot_booking', '0005_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'ADMIN'), ('USER', 'USER')], default='USER', max_length=50),
            preserve_default=False,
        ),
    ]
