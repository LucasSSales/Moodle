from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class Classroom(models.Model):

    def generateUniqueCode():
        return str(uuid4())
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    uniqueCode = models.CharField(max_length=50, default=generateUniqueCode)
    name = models.CharField(max_length=50, default='class', unique=True)
    
    

class UserClassRoomRelation(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
