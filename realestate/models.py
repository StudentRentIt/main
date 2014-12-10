from django.db import models

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=60)