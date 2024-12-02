from django.db import models
from login.models import User

class Publicacion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='publicaciones/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    