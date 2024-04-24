from django.urls import path
from . import views

urlpatterns = [
    path('', views.posted, name='home'),
    path('<str:slug_url>',views.post_detail,name="post_detail")
]
