# Generated by Django 2.2.12 on 2020-10-15 13:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ConfMan', '0002_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 10, 15, 13, 18, 25, 997693, tzinfo=utc)),
        ),
    ]