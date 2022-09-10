from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
        extra_kwargs = {'password' : {'write_only' : True}}
        
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )
    class Meta:
        model = User
        fields = ['email','username','password','password2']
        extra_kwargs = {'password' : {'write_only' : True}}
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError('Passwords did not match')
        attrs.pop('password2')
        return attrs
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)