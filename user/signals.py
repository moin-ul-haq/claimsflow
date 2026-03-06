# from .models import User
# from django.contrib.auth.signals import user_logged_in
# from django.dispatch import receiver
# from django.shortcuts import redirect


# @receiver(user_logged_in,sender=User)
# def password_change_redirect(sender,request,user,**kwargs):
#     if user.first_login == True:
#         return redirect('change_password')