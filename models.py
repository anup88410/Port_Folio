from django.db import models
class blog(models.Model):
    blogtitle=models.CharField(max_length=100)
    datetime=models.DateTimeField()
    blogimage=models.ImageField(upload_to='images/')
    blogsummary=models.TextField()
