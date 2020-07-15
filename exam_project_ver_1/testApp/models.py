from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self,email,first_name,username,password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have an username')
        user=self.model(email=self.normalize_email(email),username=username,first_name=first_name)
        user.set_password(password)
        user.is_active=True
        user.save(using=self._db)
        return user

    def create_superuser(self,email,first_name,username,password):
        user=self.create_user(email=self.normalize_email(email),first_name=first_name,username=username,password=password)
        user.is_active=True
        user.is_admin=True
        user.is_speruser=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email=          models.EmailField(verbose_name='Email Address',max_length=60,unique=True)
    username=       models.CharField(verbose_name='Username',max_length=30,unique=True)
    first_name=     models.CharField(max_length=30)
    last_name=      models.CharField(max_length=30,blank=True)
    contact_number= models.CharField(max_length=30,blank=True)
    profile_pic=    models.ImageField(upload_to='pics',null=True,blank=True)
    course=         models.CharField(max_length=100,blank=True)
    date_joined=    models.DateTimeField(verbose_name='date_joined',auto_now_add=True)
    last_login=     models.DateTimeField(verbose_name='last_login',auto_now=True)
    is_admin=       models.BooleanField(default=False)
    is_active=      models.BooleanField(default=False)
    is_staff=       models.BooleanField(default=False)
    is_speruser=    models.BooleanField(default=False)
    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name',]

    objects=MyAccountManager()

    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True