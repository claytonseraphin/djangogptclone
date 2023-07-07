from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_bot_response, name='get_bot_response'),
]
