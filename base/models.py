from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CATAGORY = (
    ('Home','Home'),
    ('Apartment','Apartment'),
    ('ROOMS','Rooms'),
    ('Office','Office'),
    ('Farmhouse','Farmhouse')
)
class  Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=255)
    catagory =  models.CharField(max_length=255,choices=CATAGORY,null=True)
    description = models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    price = models.PositiveBigIntegerField()
    location = models.CharField(max_length=255)
    phone = models.PositiveBigIntegerField(default=0)
    beds = models.PositiveBigIntegerField()
    baths = models.PositiveBigIntegerField()
    # images  = models.ImageField(null=True,blank=True)


    def __str__(self):
        host_username = self.host.username if self.host else "Unknown"
        return f'{self.title} ordered by "{host_username}"'


        

