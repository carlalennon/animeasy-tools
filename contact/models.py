from django.db import models

class Ticket(models.Model):
    email = models.EmailField(null=True, max_length=254)
    date_received = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

