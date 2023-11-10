from django.db import models

'''class CustomUser(AbstractUser):
    # Add any additional fields you need
    role = models.CharField(max_length=255, blank=True, null=True)'''

# Create your models here.
class Book(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('First Approval', 'First Approval'),        
        ('Verified', 'Verified'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year_of_release = models.IntegerField()
    genre = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    class Meta:
        unique_together = ('isbn', 'title')

    def __str__(self):
        return self.title