from django.db import models
from timescale.db.models.models import TimescaleModel


class ArcReactor(TimescaleModel):
    voltage = models.FloatField()
