# Generated by Django 5.1.2 on 2024-11-30 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackinghistory',
            name='amount',
            field=models.FloatField(editable=False),
        ),
    ]
