# Generated by Django 3.0 on 2020-09-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0004_auto_20200912_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeemachine',
            name='product_type',
            field=models.CharField(choices=[('COFFEE_MACHINE_SMALL', 'COFFEE MACHINE SMALL'), ('COFFEE_MACHINE_LARGE', 'COFFEE MACHINE LARGE'), ('ESPRESSO_MACHINE', 'ESPRESSO MACHINE')], default='COFFEE_MACHINE_SMALL', max_length=250),
        ),
        migrations.AlterField(
            model_name='coffeepod',
            name='product_type',
            field=models.CharField(choices=[('COFFEE_POD_SMALL', 'COFFEE POD SMALL'), ('COFFEE_POD_LARGE', 'COFFEE POD LARGE'), ('ESPRESSO_POD', 'ESPRESSO POD')], default='COFFEE_POD_LARGE', max_length=250),
        ),
    ]
