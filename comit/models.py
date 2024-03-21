from django.db import models

# Create your models here.
class apps(models.Model):
    id = models.IntegerField(primary_key=True,auto_created = True)
    name = models.CharField(max_length=200, unique = True)
    icon_link = models.CharField(max_length=200, unique = True)
    link = models.CharField(max_length=200, unique = True)
    category = models.CharField(max_length=200, null=True)

