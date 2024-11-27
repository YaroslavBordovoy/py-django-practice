from django.shortcuts import render
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
