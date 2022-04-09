import imp
from django.shortcuts import render, redirect
from wall_app import models
# from wall_app import urls


def wall(request):
    if 'id' in request.session:
        users_all=models.get_all_users()
        messages_all=models.all_messages()
        comments_all=models.all_comments()
        context={
            'users_a': users_all,
            'messages_a': messages_all,
            'comments_a': comments_all,
        }
        return render(request,'wall.html',context)
    return redirect('/')

def add_message(request):
    u_id=request.session['id']
    message_user=models.get_user(u_id) #brought the user object
    text=request.POST['newm']
    models.create_message(message_user,text)
    return redirect('/wall') #localhos:8000/wall

def add_comment(request):
    u_id=request.session['id']
    comment_user=models.get_user(u_id)
    comment_text=request.POST['new_comment']
    comment_message=request.POST['message_id']
    this_message=models.get_message(comment_message)
    models.create_comment(comment_user,comment_text,this_message)
    return redirect('/wall')

def delete_this(request):
    comment_to_delete = request.POST['commentid']
    models.delete_this_comment(comment_to_delete)
    return redirect('/wall')