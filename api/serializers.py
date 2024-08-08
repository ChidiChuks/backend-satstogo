from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from .models import SatsUser, Organizer
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
class OrganizerTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        self.user = authenticate(
            username=attrs['email'], 
            password=attrs['password']
        )

        if self.user is None or not self.user.is_active:
            raise serializers.ValidationError(
                'No active account found with the given credentials'
            )

        data = super().validate(attrs)
        data['user'] = self.user
        return data

class SatsUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = SatsUser
    fields = ['magic_string', 'first_name', 'last_name','created_at', 'last_login']


class BaseOrganizerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Organizer
    fields = ['email', 'password', 'name']

class OrganizerSignUpSerializer(BaseOrganizerSerializer):
    class Meta:
      model = Organizer
      fields = '__all__'
      extra_kwargs = {'password': {'write_only': True}, 'logo': {'required':False} }

    def create(self, validated_data):
      organizer = Organizer(
        email=validated_data['email'],
        name=validated_data['name']
      )
      organizer.set_password(validated_data['password'])  # This method will hash the password
      organizer.save()

      return organizer
    

      organizer = Organizer(
          email=validated_data['email'],
          name=validated_data['name']
      )
      organizer.set_password(validated_data['password'])  # This method will hash the password
      organizer.save()
      auth = get_tokens_for_user(organizer)      
      return {'user':organizer, 'auth': auth }