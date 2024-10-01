from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATAGORY = (
    ('Home', 'Home'),
    ('Apartment', 'Apartment'),
    ('ROOMS', 'ROOMS'),
    ('Office', 'Office'),
    ('Farmhouse', 'Farmhouse')
)

class Room(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    catagory = models.CharField(max_length=255,choices=CATAGORY, null=True)  # Ensure this is not unique
    beds = models.IntegerField()
    baths = models.IntegerField()
    city = models.CharField(max_length=255)
    phone = models.PositiveIntegerField()
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created','-updated']
    def __str__(self):
        return self.title

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =  ["-updated", "-created"]

    def __str__(self):
        return self.body[:50]

