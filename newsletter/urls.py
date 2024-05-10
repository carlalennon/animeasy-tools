from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.newsletter_create, name='create_newsletter'),
    path('success/', views.newsletter_success, name='newsletter_success'),
    path('archive/', views.newsletter_archive, name='newsletter_archive'),
    path('unsubscribe/', views.newsletter_unsubscribe, name='newsletter_unsubscribe'),
    path('<int:newsletter_id>/', views.newsletter_detail, name='newsletter_detail'),
]
