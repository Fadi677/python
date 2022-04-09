from django.db import models
from login_app.models import *


class Message(models.Model):
    message=models.TextField()
    user = models.ForeignKey(User, related_name="usersM", on_delete = models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment=models.TextField()
    user = models.ForeignKey(User, related_name="usersC", on_delete = models.CASCADE)
    message= models.ForeignKey(Message, related_name="messagesC", on_delete = models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


def all_comments():
    comments_list=Comment.objects.all().order_by("created_at")
    return comments_list

def all_messages():
    messages_list=Message.objects.all().order_by("created_at")
    return messages_list

def get_message(msg_id):
    this_message=Message.objects.get(id=msg_id)
    return this_message

def create_message(user,text):
    msg = Message.objects.create(message = text, user = user)
    return msg

def create_comment(comment_user,comment_text,comment_message):
    Comment.objects.create(comment=comment_text ,user= comment_user,message= comment_message)

def delete_this_comment(comment_id):
    comment_del=Comment.objects.get(id=comment_id)
    comment_del.delete()