from django.conf import settings
from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.http.response import JsonResponse
from rest_framework.response import Response

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        
        # this can be turned on in proj.settings
        # or can be temporarily enabled by creating a new file and running:
        # python manage.py runserver --settings=my_proj.settings_prime
        try: b_check_password = settings.PASSWORD_VALIDATION_ON
        except: b_check_password = False
        
        if b_check_password:
            try: validate_password(validated_data['password'])
            except Exception as e:
                raise serializers.ValidationError(
                    {'password_validation': e.messages}
                    )

        user = User.objects.create_user(
            # email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')