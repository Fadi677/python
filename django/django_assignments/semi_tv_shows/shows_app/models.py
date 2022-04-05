from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["title"] = "Network should be at least 3 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Show description should be at least 10 characters"
        return errors

class Show(models.Model):
    title=models.CharField(max_length=45)
    network=models.CharField(max_length=45)
    release_date=models.DateField()
    description=models.TextField(default="description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager() 

def all_shows():
    return Show.objects.all()

def create_show(data):
    return Show.objects.create(title=data['title'],network=data['network'],release_date=data['release_date'],description=data['description'])

def get_show(showid):
    return Show.objects.get(id=showid)

def update_me(data,show_id):
    show_to_update=Show.objects.get(id=show_id)
    show_to_update.title=data['title']
    show_to_update.network=data['network']
    show_to_update.release_date=data['release_date']
    show_to_update.description=data['description']
    show_to_update.save()
    return show_to_update

def delete_this(showid):
    D_show=Show.objects.get(id=showid)
    D_show.delete()