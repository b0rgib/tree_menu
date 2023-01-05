from django.db import models

# Create your models here.
class Menu(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return str(self.name)


class Item(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return str(self.name)
