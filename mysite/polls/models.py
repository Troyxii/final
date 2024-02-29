from django.db import models

# Create your models here.






class Event(models.Model):
    event_name = models.CharField(max_length=255)
    description = models.TextField() 
    start_date = models.CharField(max_length=255)
    location = models.CharField(max_length= 255)

    def __str__(self):
        return self.event_name