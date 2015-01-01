from django.db import models
from model_utils.fields import MonitorField, StatusField
from model_utils import Choices
from records.models import Record


class Letter(Record):
    STATUS = Choices('open', 'closed')
    status = StatusField()
    status_changed = MonitorField(monitor='status')
    text = models.TextField()
    comment = models.TextField()


class Attachment(models.Model):
    letter = models.ForeignKey(Letter)
    attachment = models.FileField(upload_to="letters/%Y/%m/%d")
    text = models.CharField(max_length=250)