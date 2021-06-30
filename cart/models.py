from django.db import models


class Coupon(models.Model):
    # Discount coupons code to validate amount for manage the discount
    code = models.CharField(max_length=10)
    amount = models.DecimalField(decimal_places=2, max_digits=6)
    

    def __str__(self):
        return self.code
