from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    userscontact = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
    dob = models.DateField()
    Language = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CommingMessages(models.Model):
    frommesg = models.CharField(max_length=500)
    sentby = models.ForeignKey(User, on_delete=models.CASCADE)
    recivedfrom = models.ForeignKey('Contact',on_delete=models.CASCADE)

    def __str__(self):
        return self.sentby
class GoingMessages(models.Model):
    tomsg = models.CharField(max_length=500)
    sentby = models.ForeignKey(User, on_delete=models.CASCADE)
    recivedfrom = models.ForeignKey('Contact',on_delete=models.CASCADE)


class CustomUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    Language = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.nickname


    


