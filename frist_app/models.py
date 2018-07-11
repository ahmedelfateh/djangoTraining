from django.db import models
#
# Create your models hereself.

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField()
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()
    def __str__(self):
        return str(self.date)

class user(models.Model):
    frist_Name = models.CharField(max_length=20, default='SOME STRING')
    last_Name = models.CharField(max_length=20, default='SOME STRING')
    email = models.EmailField(max_length=50, unique=True, default='SOME STRING')
    def __str__(self):
        return self.frist_Name
