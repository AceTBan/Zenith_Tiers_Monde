from unicodedata import name
from django.urls import path
from . import views

app_name = 'event'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_id>/detail/', views.detail, name='detail'),
]