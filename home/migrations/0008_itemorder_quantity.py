# Generated by Django 3.0.5 on 2023-04-20 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20230420_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemorder',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
