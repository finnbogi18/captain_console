# Generated by Django 3.0.6 on 2020-05-11 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20200511_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercontactinfo',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cart.Order'),
        ),
    ]
