from django.db import models

class CoffeeMachine(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('COFFEE_MACHINE_LARGE', 'COFFEE MACHINE LARGE'),
        ('COFFEE_MACHINE_SMALL', 'COFFEE MACHINE SMALL'),
        ('ESPRESSO_MACHINE', 'ESPRESSO MACHINE'),

    ]
    product_type = models.CharField(
        max_length=250,
        choices=PRODUCT_TYPE_CHOICES,
        default='COFFEE_MACHINE_LARGE',
    )

    water_line_compatible = models.BooleanField(default=False)


class CoffeePod(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('COFFEE_POD_LARGE', 'COFFEE POD LARGE'),
        ('COFFEE_POD_SMALL', 'COFFEE POD SMALL'),
        ('ESPRESSO_POD', 'ESPRESSO POD'),
    ]
    FLAVOR_CHOICES = [
        ('COFFEE_FLAVOR_VANILLA', 'COFFEE FLAVOR VANILLA'),
        ('COFFEE_FLAVOR_CARAMEL', 'COFFEE FLAVOR CARAMEL'),
        ('COFFEE_FLAVOR_PSL', 'COFFEE FLAVOR PSL'),
        ('COFFEE_FLAVOR_MOCHA', 'COFFEE FLAVOR MOCHA'),
        ('COFFEE_FLAVOR_HAZELNUT', 'COFFEE FLAVOR HAZELNUT'),
    ]
    PACK_SIZE_CHOICES = [
        ('DOZEN', '1 dozen (12)'),
        ('3_DOZEN', '3 dozen (36)'),
        ('5_DOZEN', '5 dozen (60)'),
        ('7_DOZEN', '7 dozen (84)'),
    ]
    product_type = models.CharField(
        max_length=250,
        choices=PRODUCT_TYPE_CHOICES,
        default='COFFEE_POD_LARGE',
    )

    coffee_flavor = models.CharField(
        max_length=250,
        choices=FLAVOR_CHOICES,
        default='COFFEE_FLAVOR_VANILLA',
    )

    pack_size = models.CharField(
        max_length=250,
        choices=PACK_SIZE_CHOICES,
        default='DOZEN',
    )