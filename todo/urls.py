from django.urls import path

from todo.views import (
    IndexView,
    TagView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

app_name = "todo"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tags/", TagView.as_view(), name="tag"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
]
