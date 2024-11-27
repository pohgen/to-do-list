from django.urls import path

from tasking.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskUpdateView,
    TaskDeleteView,
    task_complete,
)

urlpatterns = [
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("", TaskListView.as_view(), name="task-list"),
    path("create-task/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update-task/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete-task/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/complete-task/", task_complete, name="task-complete"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "tasking"
