# Generated by Django 3.2.8 on 2021-10-15 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_order_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='store.customer'),
        ),
    ]
