from django.db import models

# Create your models here.
from django.urls import reverse
class Category(models.Model):
    name = models.CharField(max_length=200)
     
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    rasm = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('body',args=[str(self.id)]) 


