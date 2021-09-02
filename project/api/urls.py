from django.urls import path
from .views import taskListView

urlpatterns = [
    path('all-tasks/', taskListView.as_view()),
]