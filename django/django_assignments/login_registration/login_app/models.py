from ast import Add
from django.db import models
import re
import bcrypt
from login_registration.settings import PASSWORD_HASHERS

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "User first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "User last name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['password']) <8:
            errors["password"]="User password should be at least 8 characters"
        return errors
    
    def login_validator(self,postData):
        errors1 = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors1['email'] = "Invalid email address!"
        if len(postData['password']) <8:
            errors1["password"]="User password should be at least 8 characters"
        return errors1

class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    objects=UserManager()

def create_u(data):
    upassword=data['password']
    hashed_pass= bcrypt.hashpw(upassword.encode(), bcrypt.gensalt()).decode()
    return User.objects.create(first_name=data['first_name'],last_name=data['last_name'],email=data['email'],password=hashed_pass)

def get_user(user_id):
    return User.objects.get(id=user_id)

def log_in_u(uemail):
    user0=User.objects.filter(email=uemail)
    return user0[0]
