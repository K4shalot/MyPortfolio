from django.db import models

class AboutMe(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    urls = models.URLField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Certificate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='certificates/',null=True,blank=True)
    date_issued = models.DateField()

    def __str__(self):
        return self.name