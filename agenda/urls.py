from django.urls import path
from . import views
from .views import new_task, task_list

urlpatterns = [
    path('calendar', views.CalendarView.as_view(), name='calendar'),

    # Add a todo
    path('newtask/', new_task, name='new_task'),

    # List todos
    path('listtask/', task_list, name='task_list'),

]
