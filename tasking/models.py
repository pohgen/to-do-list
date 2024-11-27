from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ["is_completed", "-date_time"]

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=27)

    def __str__(self):
        return self.name
