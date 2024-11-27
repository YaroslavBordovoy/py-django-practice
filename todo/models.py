from django.db import models


class Task(models.Model):
    TASK_COMPLETE = [
        (False, "Not done"),
        (True, "Done"),
    ]

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(choices=TASK_COMPLETE, default=False)
    tags = models.ManyToManyField(to="Tag", related_name="tasks")

    class Meta:
        ordering = ("is_done", "-created_at",)

    def __str__(self) -> str:
        return (
            f"Task: {self.content[:50]} "
            f"(created at: {self.created_at}, completed: {self.is_done})"
        )


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ("name", )

    def __str__(self) -> str:
        return self.name
