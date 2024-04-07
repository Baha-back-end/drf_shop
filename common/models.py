from django.db import models

from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', _('Image')
        VIDEO = 'video', _('Video')
        DOCUMENT = 'document', _('Document')
        GIF = 'gif', _("Gif")
        OTHER = 'other', _("Other")

    file = models.FileField(upload_to='only_medias/',
                            verbose_name=_("File"),
                            validators=[FileExtensionValidator(
                                allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp',
                                                    'mp4', 'mpeg4', 'avi', 'mov', 'mkv',
                                                    'pdf', 'doc', 'docx', 'gif']
                            )])
    file_type = models.CharField(max_length=10,
                                 verbose_name=_("File Type"),
                                 choices=FileType.choices)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")

    def __str__(self):
        return f"Id: {self.id}|Name: {self.file.name.split('/')[-1]}"

    def clean(self):
        if self.file_type not in self.FileType.values:
            raise ValidationError(_("Invalid File Type"))
        elif self.file_type == self.FileType.IMAGE:
            if self.file.name.split('.')[-1] not in ['jpg', 'jpeg', 'png', 'svg', 'webp']:
                raise ValidationError(_("Invalid Image File"))
        elif self.file_type == self.FileType.VIDEO:
            if self.file.name.split('.')[-1] not in ['mp4', 'mpeg4', 'avi', 'mov', 'mkv']:
                raise ValidationError(_("Invalid Video File"))
        elif self.file_type == self.FileType.DOCUMENT:
            if self.file.name.split('.')[-1] not in ['pdf', 'doc', 'docx']:
                raise ValidationError(_("Invalid Document File"))


class Settings(models.Model):
    main_phone_number = models.CharField(max_length=20, verbose_name=_("Main Phone Number"))
    our_clinic_text = models.TextField(verbose_name=_("Our Clinic Text"))

    service_page_image = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_("Service Page Image"),
                                           related_name="service_page_image")
    vacancy_back_image = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_("Vacancy Back Image"),
                                           related_name="vacancy_back_image")
    contacts_back_image = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_("Contacts Back Image"),
                                            related_name="contacts_back_image")

    class Meta:
        verbose_name = _("Settings")
        verbose_name_plural = _("Settings")

    def __str__(self):
        return self.main_phone_number
