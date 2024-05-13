from django.urls import path
from . import views

urlpatterns = [
    path('', views.posted, name='home'),
    path('<slug:slug>',views.post_detail,name="post_detail"),
]
