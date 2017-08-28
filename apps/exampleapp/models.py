from django.db import models

class teste(models.Model):
	id = models.AutoField(primary_key=True)
	texto = models.CharField(max_length=100)
# Create your models here.
