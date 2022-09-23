from django.db import models


class PostModel(models.Model):
    TYPES_OF_POST = [
        ('FE', 'Front-end'),
        ('BK', 'Back-end'),
        ('VJ', 'Video DJ'),
        ('MG', 'Motion graphics'),
        ('VE', 'Video edit'),
        ('3D', '3D modeling'),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    dt_create = models.DateTimeField(auto_now=False, auto_now_add=True)
    dt_change = models.DateTimeField(auto_now=True)

