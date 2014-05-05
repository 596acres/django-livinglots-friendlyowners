from django.db import models
from django.utils.translation import ugettext_lazy as _

from livinglots import get_lot_model_name, get_parcel_model_name


class BaseFriendlyOwner(models.Model):

    name = models.CharField(_('name'), max_length=50)
    email = models.EmailField(_('email'), blank=True, null=True)
    phone = models.CharField(_('phone'), blank=True, null=True, max_length=20)
    notes = models.TextField(_('notes'), blank=True, null=True)

    parcels = models.ManyToManyField(get_parcel_model_name())
    lot = models.ForeignKey(get_lot_model_name(), blank=True, null=True)

    added = models.DateTimeField(_('date added'),
        auto_now_add=True,
        editable=False,
        help_text=('When this record was added'),
    )

    def _content_object(self):
        """
        Fake content_object for the benefit of packages that expect one (such
        as livinglots_notify).
        """
        try:
            return self.parcels.all()[0]
        except Exception:
            return None
    content_object = property(_content_object)

    class Meta:
        abstract = True
