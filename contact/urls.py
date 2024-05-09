
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('success/<int:ticket_id>/', views.contact_success, name='contact_success'),
    path('tickets/', views.contact_tickets, name='contact_tickets'),
    path('<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('privacy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
]
