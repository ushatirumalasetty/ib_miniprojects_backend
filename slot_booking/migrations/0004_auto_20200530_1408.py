# Generated by Django 2.2.1 on 2020-05-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slot_booking', '0003_daysrange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='washingmachineslot',
            name='day',
            field=models.CharField(choices=[('SUNDAY', 'SUNDAY'), ('MONDAY', 'MONDAY'), ('TUESDAY', 'TUESDAY'), ('WEDNESDAY', 'WEDNESDAY'), ('THURSDAY', 'THURSDAY'), ('FRIDAY', 'FRIDAY'), ('SATuERDAY', 'SATuERDAY')], max_length=10),
        ),
    ]
