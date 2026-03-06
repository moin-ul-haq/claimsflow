from django.shortcuts import redirect
from django.urls import reverse

class FirstLoginMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        if request.user.is_authenticated:
            if request.user.first_login:
                allowed_urls=[
                    reverse('change_password'),
                reverse('rest_framework:logout'),
                reverse('rest_framework:login')
                ]
                if request.path not in allowed_urls:
                    return redirect('change_password')
        
        response=self.get_response(request)
        return response