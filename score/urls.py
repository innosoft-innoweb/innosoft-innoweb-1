from django.urls import path

from . import views


urlpatterns = [
    path('<int:participant_id>/<int:event_id>', views.score_view, name='score'),

]