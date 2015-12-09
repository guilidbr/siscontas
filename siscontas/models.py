from django.db import models
from django.utils import timezone

class Bank(models.Model):
	description = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	edited_date = models.DateTimeField(default=timezone.now)

class Card(models.Model):
	bank = models.ForeignKey('Bank')
	last_four_digits = models.IntegerField()
	card_type = models.TextField()
	day_close_account = models.IntegerField()
	limit = models.DecimalField
	created_date = models.DateTimeField(default = timezone.now())
	edited_date = models.DateTimeField(default=timezone.now)