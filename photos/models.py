from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name

class photos(models.Model):
    description = models.TextField()
    img = models.ImageField(null=False, blank= False)
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null= True )

    def __str__(self):
        return self.description