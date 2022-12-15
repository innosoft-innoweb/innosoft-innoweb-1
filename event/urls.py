from django.urls import path
from . import views

urlpatterns = [
   path('<int:id>', views.event_view, name='event'),
   path('join/<int:id>', views.join_event, name='join_event'),
]
