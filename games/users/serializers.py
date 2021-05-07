from rest_framework import serializers
from .models import Publisher, Customer, BaseUserProfile
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUserProfile
        fields = ['user', 'firstname', 'lastname', 'contact', 'date']
        abstract = True


class PublisherSerializer(BaseUserSerializer):
    class Meta:
        model = Publisher
        fields = ['user', 'firstname', 'lastname', 'contact', 'date']


class CustomerSerializer(BaseUserSerializer):
    class Meta:
        model = Customer
        fields = ['user', 'firstname', 'lastname', 'contact', 'date']


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    firstname = serializers.CharField(max_length=30)
    lastname = serializers.CharField(max_length=30)
    contact = serializers.CharField()
    date = serializers.DateField()

    password = serializers.CharField(max_length=30)
    password2 = serializers.CharField(max_length=30)

    is_customer = serializers.BooleanField(default=False)
    is_publisher = serializers.BooleanField(default=False)

    def save(self, validated_data):
        user = User.objects.create_user(
            username=self.validated_data['username'],
        )
        is_customer = self.validated_data['is_customer']
        is_publisher = self.validated_data['is_publisher']

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializer.ValidationError({'password': 'Password must match'})

        user.set_password(password)
        user.save()

        if (is_customer):
            user_profile = Customer(
                user=user,
                firstname=self.validated_data['firstname'],
                lastname=self.validated_data['lastname'],
                contact=self.validated_data['contact'],
                date=self.validated_data['date'],
            )

        elif (is_publisher):
            user_profile = Publisher(
                user=user,
                firstname=self.validated_data['firstname'],
                lastname=self.validated_data['lastname'],
                contact=self.validated_data['contact'],
                date=self.validated_data['date'],
            )
        user_profile.save()
        return user_profile


class UserSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=50)
    firstname = serializers.CharField(max_length=30)
    lastname = serializers.CharField(max_length=30)
    contact = serializers.CharField()
    date = serializers.DateField()
