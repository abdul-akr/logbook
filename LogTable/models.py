from django.db import models
from django.contrib.auth.models import AbstractUser
class Roles(models.Model):
   
    # MANAGER=1
    # EMPLOYEE=2
    # ADMIN=3
    # SUPERVISOR=4

    # ROLES_CHOICES=(
    #     (MANAGER,'manager'),
    #     (EMPLOYEE,'employee'),
    #     (ADMIN,'admin'),
    #     (SUPERVISOR,'supervisor')
    # )
    role=models.CharField(max_length=50,unique=True)
    

class User(models.Model):
    uniqueid=models.CharField(max_length=20,unique=True,unique=True)
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length=10)
    role=models.ManyToManyField(Roles)
    # class Role(models.TextChoices):
        
    #     ADMIN="ADMIN",'Admin'
    #     MANAGER="MANAGER",'Manager'
    #     EMPLOYEE ="EMPLOYEE",'Employee'
    # base_role=Role.EMPLOYEE

    # roles=models.ForeignKey(Roles)
    

    # def save(self)
    # logs=models.ForeignKey()
    # def __str__(self):
    #     return self.uniqueid



class LogsTable(models.Model):
    
    user= models.ForeignKey(User,on_delete=models.CASCADE,related_name='logs',default=None,null=True,blank=True)
    day=models.DateField(auto_now_add = True)
    time_in=models.TimeField(auto_now_add = True)
    time_out=models.TimeField(default='00:00:00')
    uniqueid=models.CharField(max_length=20)

    # def __str__(self):
    #     return self.day,self.time_in,self.time_out


    #     MANAGER="MANAGER",'Manager'
    #     EMPLOYEE ="EMPLOYEE",'Employee'
    # base_role=Role.EMPLOYEE

    # role=models.CharField(max_length=50)
    

# role=models.CharField(max_length=50,choices=ROLES_CHOICES)
    # uniqueid=models.CharField(max_length=20)
    # user= models.ForeignKey(User,on_delete=models.CASCADE,choices=ROLES_CHOICES,related_name='role_names',default=None,null=True,blank=True)
    # user=models.ManyToManyField(User)