from django.db import models


class CoffeeMachine(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('COFFEE_MACHINE_SMALL', 'COFFEE MACHINE SMALL'),
        ('COFFEE_MACHINE_LARGE', 'COFFEE MACHINE LARGE'),
        ('ESPRESSO_MACHINE', 'ESPRESSO MACHINE'),

    ]
    MODEL_CHOICES = [
        ('BASE_MODEL', 'BASE MODEL'),
        ('PREMIUM_MODEL', 'PREMIUM MODEL'),
        ('DELUXE_MODEL', 'DELUXE MODEL'),

    ]
    product_type = models.CharField(
        max_length=250,
        choices=PRODUCT_TYPE_CHOICES,
        default='COFFEE_MACHINE_SMALL',
    )

    water_line_compatible = models.BooleanField(default=False)

    model_type = models.CharField(
        max_length=250,
        choices=MODEL_CHOICES,
        default='BASE_MODEL',
    )

    @property
    def sku_number(self):
        sku_number = ''
        if self.product_type == 'COFFEE_MACHINE_SMALL':
            sku_number += 'CM00'
        if self.product_type == 'COFFEE_MACHINE_LARGE':
            sku_number += 'CM10'
        if self.product_type == 'ESPRESSO_MACHINE':
            sku_number += 'EM00'
        if self.model_type == 'BASE_MODEL':
            sku_number += '1'
        if self.product_type == 'COFFEE_MACHINE_LARGE' and self.model_type == 'PREMIUM_MODEL' and self.water_line_compatible is True:
            sku_number += '2'
        if self.product_type in ['COFFEE_MACHINE_SMALL', 'ESPRESSO_MACHINE'] and self.model_type == 'PREMIUM_MODEL':
            sku_number += '2'
        if self.model_type == 'DELUXE_MODEL' and self.water_line_compatible is True:
            sku_number += '3'

        return sku_number

    def __str__(self):
        return self.sku_number


class CoffeePod(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('COFFEE_POD_SMALL', 'COFFEE POD SMALL'),
        ('COFFEE_POD_LARGE', 'COFFEE POD LARGE'),
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

    @property
    def sku_number(self):
        sku_number = ''
        if self.product_type == 'COFFEE_POD_SMALL':
            sku_number += 'CP0'
        if self.product_type == 'COFFEE_POD_LARGE':
            sku_number += 'CP1'
        if self.product_type == 'ESPRESSO_POD':
            sku_number += 'EP0'
        if self.coffee_flavor == 'COFFEE_FLAVOR_VANILLA':
            sku_number += '0'
        if self.coffee_flavor == 'COFFEE_FLAVOR_CARAMEL':
            sku_number += '1'
        if self.coffee_flavor == 'COFFEE_FLAVOR_PSL':
            sku_number += '2'
        if self.coffee_flavor == 'COFFEE_FLAVOR_MOCHA':
            sku_number += '3'
        if self.coffee_flavor == 'COFFEE_FLAVOR_HAZELNUT':
            sku_number += '4'
        if self.pack_size == 'DOZEN':
            sku_number += '1'
        if self.pack_size == '3_DOZEN':
            sku_number += '3'
        if self.pack_size == '5_DOZEN':
            sku_number += '5'
        if self.pack_size == '7_DOZEN':
            sku_number += '7'
        return sku_number

    def __str__(self):
        return self.sku_number
