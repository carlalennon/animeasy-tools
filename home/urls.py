"""
URLS for home, install guide, about and FAQ pages
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('install-guide/', views.install_guide, name='install_guide'),
    path('faq/', views.faq, name='faq'),
]
