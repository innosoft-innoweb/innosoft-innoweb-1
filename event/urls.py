from django.urls import path
from . import views

urlpatterns = [
   path('<int:id>', views.event_view, name='event'),
]
