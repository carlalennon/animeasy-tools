
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='contact'),
    path('success/', views.contact_success, name='contact_success'),
    path('tickets/', views.contact_tickets, name='contact_tickets'),
    path('<int:ticket_id>/', views.product_detail, name='ticket_detail'),
]
