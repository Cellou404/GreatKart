from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("Category name"), max_length=50, unique=True)
    description = models.TextField(_("Description"), max_length=500, blank=True)
    image = models.ImageField(upload_to="photos/categories/", blank=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(_("slug"), unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("products_by_category", args=[self.slug])

    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == "":
            self.slug = slugify(f"{self.name}")

        if self.created_at == None:
            self.created_at = timezone.localtime(timezone.now())

        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
