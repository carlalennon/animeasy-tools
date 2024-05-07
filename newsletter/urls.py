from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.newsletter_create, name='create_newsletter'),
    path('success/', views.newsletter_success, name='newsletter_success'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
