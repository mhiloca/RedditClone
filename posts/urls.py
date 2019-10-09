from django.urls import path

from .views import post_list, posted_by, new_post

urlpatterns = [
    path('list', post_list, name='list'),
    path('postedby/<int:id>/', posted_by, name='postedby'),
    path('new/', new_post, name='newpost'),
]