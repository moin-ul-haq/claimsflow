from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer,User,ChangePasswordSerializer
from organization.permissions import IsSuperAdmin
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import update_session_auth_hash

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsSuperAdmin]

class ChangePasswordView(APIView):
    def post(self,request):
        serializer=ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user=request.user
            if user.check_password(serializer.validated_data['old_password']):
                user.set_password(serializer.validated_data['new_password'])
                user.first_login = False
                user.save()
                update_session_auth_hash(request,user)
                return Response({'message':'Password Changed Successfully!'},status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'message':'Incorrect Password!'},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)