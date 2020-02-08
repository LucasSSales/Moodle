from rest_framework import permissions
from classroom.models import Classroom

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.method in ('GET'):
            return True
        data = request.data.dict()

        if 'classroom' in data.keys():
            try:
                classroom = Classroom.objects.get(pk=data['classroom'])
                return classroom.owner.id == request.user.id
            except: 
                return True

        return True
