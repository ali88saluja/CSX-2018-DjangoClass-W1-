from django.db import models
from django.conf import settings
# Create your models here.

class message(models.Model):
	send = models.CharField(max_length=50, blank=False)
	message = models.CharField(max_length=50, blank=True)
	time = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.send + " " + self.message + " " + self.time