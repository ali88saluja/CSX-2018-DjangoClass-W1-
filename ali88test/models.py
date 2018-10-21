from django.db import models
from django.conf import settings
# Create your models here.

class message(models.Model):
	send = models.CharField(max_length=50, blank=False, default="anything")
	message = models.CharField(max_length=50, blank=True, default="anything")
	time = models.DateTimeField(auto_now_add=True, blank=True, default="anything")
	def __str__(self):
		return self.send + " " + self.message + " " + self.time