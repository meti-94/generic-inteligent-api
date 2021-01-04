from django.urls import path

from . import views

urlpatterns = [
    path('detect/', views.main, name='simple'),
    path('detect_batch/', views.main_batch, name='batched'),
]