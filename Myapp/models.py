from django.db import models
# Create your models here.
STATE_CHOICES = (
    ('Province 1', 'Province 1'),
    ('Province 2', 'Province 2'),
    ('Bagmati Province', 'Bagmati Province'),
    ('Gandaki Province', 'Gandaki Province'),
    ('Lumbini Province', 'Lumbini Province'),
    ('Karnali Province', 'Karnali Province'),
    ('Sudurpashchim Province', 'Sudurpashchim Province'),
)

class Signup(models.Model):
    First_Name= models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    Email= models.CharField(max_length=100)
    Password = models.CharField(max_length= 100)

class User(models.Model):
    Username= models.CharField(max_length=100)
    Password = models.CharField(max_length= 100)


   # _________------Image UPLOADER______---------
class Imageupload(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = models.DateField(auto_now_add=True)

       # _________------RESUME UPLOADER______---------

    STATE_CHOICES = (
    ('Province 1', 'Province 1'),
    ('Province 2', 'Province 2'),
    ('Bagmati Province', 'Bagmati Province'),
    ('Gandaki Province', 'Gandaki Province'),
    ('Lumbini Province', 'Lumbini Province'),
    ('Karnali Province', 'Karnali Province'),
    ('Sudurpashchim Province', 'Sudurpashchim Province'),
)


class Resume_Uploader(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length= 100)
    locality = models.CharField(max_length= 100)
    city = models.CharField(max_length= 100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices= STATE_CHOICES, max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='pro', blank= True)
    my_file = models.FileField(upload_to = 'document', blank = True)

    
 