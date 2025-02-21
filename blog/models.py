from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateField()
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title
