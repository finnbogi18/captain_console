# Generated by Django 3.0.6 on 2020-05-14 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_orderpaymentinfo_expiry_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderpaymentinfo',
            name='expiry_month',
            field=models.CharField(choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12')], default='1', max_length=2),
        ),
    ]