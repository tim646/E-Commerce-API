# Generated by Django 4.2 on 2023-04-19 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_payment_table_alter_shippingaddress_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Confirmed'), ('S', 'Shipped'), ('D', 'Delivered'), ('X', 'Cancelled')], default='P'),
        ),
    ]