from django.db import models
import re
import bcrypt


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
        if postData['password']!=postData['confirm']:
            errors["confirm"]="Password and confirmation Password don't match"
        return errors
    
    def login_validator(self,postData):
        check_e=User.objects.filter(email=postData['email'])
        errors = {}
        if not len(check_e):
            errors['email']="email doesn't exist"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['password']) <8:
            errors["password"]="User password should be at least 8 characters"
        if len(check_e) and not bcrypt.checkpw(postData['password'].encode(),check_e[0].password.encode()):
            errors["password"]="Wrong Password!"
        return errors


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
    this_user=User.objects.get(id=user_id)
    return this_user

def log_in_u(uemail):
    user0=User.objects.filter(email=uemail)
    return user0[0]

def get_all_users():
    all_users=User.objects.all()
    return all_users