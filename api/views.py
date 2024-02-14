from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializers
from .permissions import IsOwnerOrReadOnly

# 2. API Endpoints [CRUD Operations]
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    permission_classes = [permissions.IsAuthenticated | IsOwnerOrReadOnly]
    
    def update(self, req, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=req.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def delete(self, req, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_No_CONTENT)