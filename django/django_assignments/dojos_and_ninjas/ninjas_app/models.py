from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=45)
    desc = models.TextField(default="old dojo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def all_dojos():
    return Dojo.objects.all()

def create_dojo(dname,dcity,dstate):
    Dojo.objects.create(name=dname,city=dcity, state=dstate)
    print("------",dname,dcity,dstate)

def getDojo(ninjaname,ninjalast,did):
    print(type(did))
    dojo_from_selection = Dojo.objects.get(id=did)	
    new_ninja = Ninja.objects.create(first_name=ninjaname, last_name=ninjalast, dojo=dojo_from_selection)