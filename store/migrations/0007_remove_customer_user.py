# Generated by Django 5.0.1 on 2024-01-18 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
