from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    template_name = "todo/index.html"

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        task_id = self.request.POST.get("task_id")
        action = self.request.POST.get("action")

        if task_id:
            task = Task.objects.get(id=task_id)
            if action == "complete":
                task.is_done = True
            elif action == "undo":
                task.is_done = False
            task.save()

        return redirect("todo:index")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.prefetch_related("tasks")
    template_name = "todo/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
