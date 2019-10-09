from django.urls import path

from .views import post_list, posted_by

urlpatterns = [
    path('list', post_list, name='list'),
    path('postedby/<int:id>/', posted_by, name='postedby'),
]