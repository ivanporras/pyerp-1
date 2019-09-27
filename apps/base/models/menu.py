# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather


class PyMenu(PyFather):
    name = models.CharField(_("Menu"), max_length=40)
    parent_id = models.ForeignKey('self', null=True, blank=True, default=None, on_delete=models.PROTECT)
    link = models.CharField(_("link"), max_length=100)
    sequence = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('base:menu-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _("PyMenu")
