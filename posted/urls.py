from django.urls import path
from .views import posted, post_detail

urlpatterns = [
    path('', posted, name='home'),
    path('<int:post_id>',post_detail)
]
