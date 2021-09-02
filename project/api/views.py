from api.serializers import TaskSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Task


class taskListView(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
