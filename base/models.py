from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

CATAGORY = (
    ('Home', 'Home'),
    ('Apartment', 'Apartment'),
    ('ROOMS', 'ROOMS'),
    ('Office', 'Office'),
    ('Farmhouse', 'Farmhouse')
)

class Room(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    catagory = models.CharField(max_length=255, choices=CATAGORY, null=True)  # Ensure this is not unique
    beds = models.IntegerField(null=True)  # Allow null values
    baths = models.IntegerField(null=True)
    city = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    phone = models.PositiveIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Add this line
    created = models.DateTimeField(auto_now_add=True,null=False)  # No need for a default since auto_now_add handles it
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self):
        return self.title

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.body[:50]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.user.username
