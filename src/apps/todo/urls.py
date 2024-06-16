from apps.todo.views import TasksList
from rest_framework import routers

router = routers.SimpleRouter()

app_name = 'todo'

router.register(r'tasks', TasksList)

urlpatterns = router.urls
