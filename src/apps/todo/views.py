from apps.todo.models import Task
from apps.todo.serializers import TaskSerializer
from apps.utils.views import HTMLViewSet
from rest_framework.decorators import action
from rest_framework.response import Response


class TasksList(HTMLViewSet):
    queryset = Task.objects.all().order_by('done', '-created_at')
    serializer_class = TaskSerializer
    templates_map = {
        'retrieve': 'detial.html',
        'list': 'list.html',
        'create': 'list.html',
        'destroy': 'list.html',
        'new': 'new.html',
    }

    states = {
        'done': 'list',
        'partial_update': 'list',
        'create': 'list',
        'destroy': 'list',
    }

    @action(methods=['GET'], detail=False)
    def new(self, *args, **kwargs):
        return Response()

    @action(methods=['POST'], detail=True)
    def done(self, *args, **kwargs):
        instance = self.get_object()
        instance.done = not instance.done
        instance.save()
        return Response()
