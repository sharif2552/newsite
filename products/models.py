from django.db import models

# Create your models here.
class paymentmaking(models.Model):
    name = models.CharField(max_length=100)
   
    age = models.IntegerField()
    phone_number =models.IntegerField()
    def __str__(self):
        return self.name + ' '


class info(models.Model):
    fullname = models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    
    def __str__(self):
        return self.fullname  # এইটার কাজ হইতাছে এডমিন প্যানেল এ যাইয়া এই নাম show করাইবো