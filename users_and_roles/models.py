from django.db import models

class Role(models.Model):
    role_type = models.CharField(max_length=20)

class User(models.Model):
    name = models.CharField(max_length=50) 
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)