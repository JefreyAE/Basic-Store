# Generated by Django 3.0.5 on 2023-04-20 21:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20230419_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(default=12345, unique=True),
            preserve_default=False,
        ),
    ]
