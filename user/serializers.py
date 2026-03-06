from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','organization','practice','role']

class ChangePasswordSerializer(serializers.Serializer):
    old_password=serializers.CharField()
    new_password=serializers.CharField()
    class Meta:
        fields=['old_password','new_password','Confirm_new_password']