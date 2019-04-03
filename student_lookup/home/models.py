from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_img')
    reg_no = models.CharField(max_length=10)
    dep = models.CharField(max_length=10)
    room = models.CharField(max_length=8)
    batch = models.CharField(max_length=5,null=True,blank=True)
    parent_no = models.CharField(max_length=10)
    student_no = models.CharField(max_length=10)
    batch = models.CharField(max_length=5)    
