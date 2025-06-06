from django.db import models
from cloudinary.models import CloudinaryField

class AboutMe(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    urls = models.URLField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Certificate(models.Model): 
    name = models.CharField(max_length=255)
    description = models.TextField()
    file_url = models.URLField(max_length=500, blank=True, null=True)
    date_issued = models.DateField()

    def __str__(self):
        return self.name if self.name else "Unnamed Certificate"