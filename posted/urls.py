from django.urls import path
from .views import posted

urlpatterns = [
    path('', posted, name='home')
]