from django.db import models

class coffe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    value = models.FloatField(max_length=5, blank=True, null=True)
    photo = models.ImageField("media/")

    def __str__(self): 
        return self.title
    