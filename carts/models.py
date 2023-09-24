from django.db import models
from django.utils.translation import gettext_lazy as _

from store.models import Product


class Cart(models.Model):
    cart_id = models.CharField(_("cart id"), max_length=250)
    date_added = models.DateTimeField(_("date added"), auto_now_add=True)

    def __str__(self):
        return self.cart_id
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'))
    cart = models.ForeignKey(Cart, verbose_name=_("cart"), on_delete=models.CASCADE)
    quantity = models.IntegerField(_("quatity"))
    is_active = models.BooleanField(_("is active"), default=True)

    def __str__(self):
        return self.product
