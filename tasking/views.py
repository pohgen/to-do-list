from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView
)

from tasking.forms import TaskCreateForm
from tasking.models import Task, Tag


class TaskListView(ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("tasking:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("tasking:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("tasking:task-list")


class TagListView(ListView):
    model = Tag


class TagCreateView(CreateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("tasking:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("tasking:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tasking:tag-list")


def task_complete(request, pk):
    task = Task.objects.get(id=pk)
    task.is_completed = not task.is_completed
    task.save()
    return HttpResponseRedirect(reverse_lazy("tasking:task-list"))
