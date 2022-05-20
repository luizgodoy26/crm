from django.urls import path
from . import views

urlpatterns = [
    path('calendar', views.CalendarView.as_view(), name='calendar'),
    path('newev', views.event, name='new_event'),
    path('editev/<int:id>', views.event, name='edit_event'),
]
