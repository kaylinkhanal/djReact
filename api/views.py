from rest_framework import viewsets
from .models import Assignment
from .serializers import AssignmentSerializer

#
class AssignmentViewset(viewsets.ModelViewSet):
    serializer_class= AssignmentSerializer
    queryset= Assignment.objects.all()
#now we can use this userviewset inside our own urls.py
