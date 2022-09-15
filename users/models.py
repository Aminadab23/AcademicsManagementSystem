from email.policy import default
from hashlib import md5
import imp
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from PIL import Image
from AcademicManager.models import Academy
# Create your models here.


class userManager(BaseUserManager):
    def create_user(self,email,FullName, password=None):
        if not email:
            raise ValueError('Users must have an email adress.')
        if not FullName:
            raise ValueError('Users must have an FullName adress.')
        if not password:
            raise ValueError('Users must have an password adress.')
        user = self.model(
            email= self.normalize_email(email),
            FullName = FullName,
        )
        user.set_password(password)
        user.save(using= self.db)
        return user
    def create_superuser(self,email,FullName,password):
        user = self.create_user(
            email= self.normalize_email(email),
            FullName= FullName,
            password=password,
        )
        user.is_admin= True
        user.is_staff= True
        user.is_superuser= True
        user.save(using= self.db)
        return user



def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'
def get_default_profile_image():
    return 'default.jpg'
class user(AbstractBaseUser):
    email= models.EmailField(max_length=60, unique=True)
    FullName= models.CharField(max_length=100)
    Profilepic= models.ImageField(upload_to=get_profile_image_filepath, default= get_default_profile_image, null= True)
    # password= models.CharField(max_length=255, )
    Roll = models.CharField(max_length=50,default='user')
    Academy = models.CharField(max_length=200, default='staff')
    course= models.CharField(max_length=120, default='N/A')
    date_joined= models.DateTimeField(auto_now_add= True)
    last_login= models.DateTimeField(auto_now=True)
    is_admin= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    
   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['FullName']


    objects= userManager()


    def __str__(self):
        return self.FullName
    def has_perm(self, perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
    def has_change_permission(self,request, obj=None):
        return True
    def has_delete_permission(self,request, obj=None):
        return True
    


    def get_profile_image_filename(self):
        return str(self.Profilepic)[str(self.Profilepic).index(f'profile_images/{self.pk}'):]
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img= Image.open(self.Profilepic.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.Profilepic.path)

class UploadRecite(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    academy= models.CharField(max_length=254)
    course = models.CharField(max_length=255)
    recite = models.ImageField( upload_to='recite')
class UserMessage(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=255)
    message= models.TextField()
    def __str__(self):
        return self.name

