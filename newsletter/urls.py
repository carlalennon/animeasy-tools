from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.newsletter_create, name='create_newsletter'),
    path('success/', views.newsletter_success, name='newsletter_success'),
    path('archive/', views.newsletter_archive, name='newsletter_archive'),
]
