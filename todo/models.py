from django.db import models


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(to="Tag", related_name="tasks")

    class Meta:
        ordering = ("is_done", "-created_at",)

    def __str__(self) -> str:
        return f"Task: {self.content[:50]} ()"


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
