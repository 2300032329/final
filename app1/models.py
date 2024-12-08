from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    meal_type = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/', default='recipes/default.jpg')  # Add a default image here

    def __str__(self):
        return self.name