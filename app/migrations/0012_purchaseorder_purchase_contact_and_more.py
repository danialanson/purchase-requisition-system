# Generated by Django 4.1.4 on 2023-01-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_purchaseorder_purchase_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='purchase_contact',
            field=models.TextField(default=None, max_length=11),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='purchase_email',
            field=models.TextField(default=None),
        ),
    ]
