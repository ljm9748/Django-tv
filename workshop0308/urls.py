from django.urls import path
from . import views

urlpatterns = [
    # DOMAIN/lotto/
    path('lotto/', views.lotto),
    # DOMAIN/lotto/action
]
