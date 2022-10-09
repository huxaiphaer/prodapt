import uuid as uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class WeatherForecast(TimeStampedModel, models.Model):

    """Weather forecast model."""

    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    city = models.CharField(_('City'), max_length=100, null=True, blank=True)
    description = models.TextField(_('Description'), null=True, blank=True)
    date_time_forecasted = models.DateTimeField(
        _('Date Time Forecasted'), null=True, blank=True)

    def __str__(self):
        """Model Representation."""
        return self.city
