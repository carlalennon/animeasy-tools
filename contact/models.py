from django.db import models
status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('resolved', 'Resolved')])

class Ticket(models.Model):
    email = models.EmailField(null=True, max_length=254)
    date_received = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('resolved', 'Resolved')], default='pending')

    def __str__(self):
        return self.title

