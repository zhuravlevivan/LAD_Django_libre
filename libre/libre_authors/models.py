from django.db import models


class LibreAuthors(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	country = models.CharField(max_length=255)
	content = models.TextField(blank=True)
	time_create = models.DateTimeField(auto_now_add=True)
	time_update = models.DateTimeField(auto_now=True)
