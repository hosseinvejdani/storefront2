# Generated by Django 3.2.8 on 2021-10-08 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20211008_1646'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': {('cancel_order', 'Can Cancel Order')}},
        ),
    ]
