from django.db import models

# Create your models here.
class LongTask(models.Model):
  created_on = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=128, help_text='Enter a unique name for the task',)
  progress = models.PositiveIntegerField(default=0)
  result = models.CharField(max_length=128, blank=True, null=True)
