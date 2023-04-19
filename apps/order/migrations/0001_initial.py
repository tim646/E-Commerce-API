# Generated by Django 4.2 on 2023-04-20 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('payment_method', models.CharField(choices=[('PP', 'PayPal'), ('GP', 'Google Pay'), ('AP', 'Apple Pay'), ('BT', 'Bank Transfer'), ('COD', 'Cash on Delivery'), ('CA', 'Cash')], max_length=24, verbose_name='Payment Method')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('C', 'Confirmed'), ('S', 'Shipped'), ('D', 'Delivered'), ('X', 'Cancelled')], default='P', verbose_name='Status')),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cart.cart', verbose_name='Cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Order')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('state', models.CharField(max_length=255, verbose_name='State')),
                ('zip_code', models.CharField(max_length=10, verbose_name='Zip Code')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'shipping',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Order')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
    ]
