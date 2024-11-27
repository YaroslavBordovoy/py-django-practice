from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    template_name = "todo/index.html"


class TagView(generic.ListView):
    model = Tag
    queryset = Tag.objects.prefetch_related("tasks")
    template_name = "todo/tag.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = (
        "content",
        "deadline",
        "is_done",
        "tags",
    )
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = (
        "content",
        "deadline",
        "is_done",
        "tags",
    )
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")
