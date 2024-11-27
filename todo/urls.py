from django.urls import path

from todo.views import IndexView, TagView

app_name = "todo"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tags/", TagView.as_view(), name="tag"),
]
