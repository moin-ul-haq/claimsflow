from django.db import models
from django.contrib.auth.models import AbstractUser
from organization.models import Organization,Practice


class User(AbstractUser):
    permission_choices =[
        ('superadmin','SuperAdmin'),
        ('orgadmin','OrgAdmin'),
        ('pracadmin','PracAdmin')
    ]

    role = models.CharField(max_length=20,choices=permission_choices)
    organization = models.ForeignKey(Organization,related_name='user',on_delete=models.CASCADE,null=True,blank=True)
    practice = models.ForeignKey(Practice,on_delete=models.CASCADE,related_name='user',null=True,blank=True)
    first_login=models.BooleanField(default=True)

    def __str__(self):
            return f"{self.username} - {self.get_role_display()}"
    def save(self,*args, **kwargs): 
        if not self.pk:
            self.set_password('moin')
        super().save(*args,**kwargs)
