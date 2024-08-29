from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)

class ClassAssignment(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    class1File = models.FileField(name="Class 1 File", blank=True)
    class2File = models.FileField(name="Class 2 File", blank=True)
    class3File = models.FileField(name="Class 3 File", blank=True)
    class4File = models.FileField(name="Class 4 File", blank=True)
    class6File = models.FileField(name="Class 6 File", blank=True)
    class7File = models.FileField(name="Class 7 File", blank=True)
    class8File = models.FileField(name="Class 8 File", blank=True)