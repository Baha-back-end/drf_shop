import datetime
from mptt.models import MPTTModel, TreeForeignKey

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class ServiceCategory(MPTTModel):
    title = models.CharField(max_length=100,
                             verbose_name=_("Title"),
                             unique=True)
    order = models.IntegerField(_("Order"), default=0)

    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name="children")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Service Category")
        verbose_name_plural = _("Service Categories")
        ordering = ['order']

    class MPTTMeta:
        order_insertion_by = ['title']


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name=_("Category Title"),
                                 related_name="services")
    title = models.CharField(_("Title"), max_length=100)
    subtitle = models.CharField(_("Subtitle"), max_length=100)
    image = models.ForeignKey('common.Media',
                              on_delete=models.CASCADE,
                              verbose_name=_("Image"))
    short_desc = models.TextField(_("Short Description"))
    desc = models.TextField(_("Description"))
    price = models.IntegerField(_("price"))
    is_home_page = models.BooleanField(_("is home page"),
                                       default=False,
                                       unique=True)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.title


class ServiceImage(models.Model):
    image = models.ForeignKey('common.Media', on_delete=models.CASCADE,
                              verbose_name=_("Image"))
    service = models.ForeignKey(Service, on_delete=models.CASCADE,
                                verbose_name=_("Service"))

    class Meta:
        verbose_name = _("Service Image")
        verbose_name_plural = _("Service Images")

    def __str__(self):
        return f"Id: {self.id}| Service: {self.service.title}"


class Characteristics(models.Model):
    title = models.CharField(_("title"), max_length=100)
    value = models.CharField(_("value"), max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE,
                                verbose_name=_("Characteristics"),
                                related_name="characteristics")

    class Meta:
        verbose_name = _("Characteristic")
        verbose_name_plural = _("Characteristics")

    def __str__(self):
        return self.title


class ProcedureCost(models.Model):
    title = models.CharField(_("title"), max_length=100)
    price = models.CharField(_("price"), max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE,
                                verbose_name=_("service"),
                                related_name='procedure_costs')

    class Meta:
        verbose_name = _("procedure cost")
        verbose_name_plural = _("procedure costs")
