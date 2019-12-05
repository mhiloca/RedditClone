from django.urls import path

from .views import post_list, posted_by, new_post, vote_up, vote_down

urlpatterns = [
    path('list', post_list, name='list'),
    path('postedby/<int:id>/', posted_by, name='postedby'),
    path('new/', new_post, name='newpost'),
    path('voteup/<int:id>/', vote_up, name='vote_up'),
    path('votedown/<int:id>/', vote_down, name='vote_down'),
]