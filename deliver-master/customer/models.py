from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='menu_images/')
    def __str__(self):
        return self.title
    
class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=True)
    reservation = models.CharField(max_length=300, blank=True)
    table_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'Reservation: {self.created_on.strftime("%b %d %I:%M %p")}'