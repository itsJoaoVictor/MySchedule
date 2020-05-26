from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
  title = models.CharField(max_length=100)
  desc = models.TextField(blank=True, null=True)
  event_date = models.DateTimeField()
  datetimestamp = models.DateTimeField(auto_now=True, verbose_name="Created")
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    db_table = 'event'

  def __str__(self):
    return self.title

  def get_event_date(self):
    hrs = "Horas"
    return self.event_date.strftime('%d/%m/%Y %H:%M Hours')