from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('halls/delete/', views.delete_hall, name='hall_delete'),
    path('halls/update/', views.update_hall, name='hall_update'),
]
