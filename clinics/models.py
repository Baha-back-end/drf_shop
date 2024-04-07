import datetime
from ckeditor.fields import RichTextField

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from common.models import Media
from common.utils import validate_phone_number


class Vacancy(models.Model):
    title = models.CharField(_("Title"), max_length=120)
    image = models.ForeignKey(Media,
                              on_delete=models.SET_NULL,
                              null=True, blank=True)
    responsibilities = RichTextField(_("Responsibilities"))
    requirements = RichTextField(_("Requirements"))
    conditions = RichTextField(_("Conditions"))

    class Meta:
        verbose_name = _("vacancy")
        verbose_name_plural = _("vacancies")

    def __str__(self):
        return self.title

