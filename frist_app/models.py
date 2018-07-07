from django.db import models

# Create your models hereself.

class Topic(models.Model):
    top_Name = models.CharField(max_length = 264, unique=True)
    def __str__(self):
        return self.top_Name

class webPage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length = 264, unique=True)
    url = models.URLField(unique=True)
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(webPage)
    date = models.DateField()
    def __str__(self):
        return str(self.date)