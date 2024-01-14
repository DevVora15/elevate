from django.db import models

# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self) :
        return 'Message from ' + self.first_name + ' - ' + self.email    