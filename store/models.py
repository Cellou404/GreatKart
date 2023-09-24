import uuid
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify

from category.models import Category


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Product name"), max_length=200, unique=True)
    description = models.TextField(_("description"), max_length=500)
    price = models.IntegerField(_("price"))
    images = models.ImageField(_("images"), upload_to="photos/products")
    stock = models.IntegerField(_("stock"))
    is_available = models.BooleanField(_("is available ?"), default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(_("slug"), unique=True, blank=True)
    created_date = models.DateTimeField(
        _("created date"), auto_now_add=True, blank=True
    )
    modified_date = models.DateTimeField(_("modified date"), auto_now=True, blank=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Product")
        ordering = ("-created_date",)

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == "":
            self.slug = slugify(f"{self.name}")

        if self.created_date == None:
            self.created_date = timezone.localtime(timezone.now())

        if self.modified_date == None:
            self.modified_date = timezone.localtime(timezone.now())

        super(Product, self).save(*args, **kwargs)
