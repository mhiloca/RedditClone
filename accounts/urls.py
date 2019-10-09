from django.urls import path
from django.contrib.auth import views as auth_views

from .views import sign_up, log_in, dashboard

urlpatterns = [
    path('signup/', sign_up, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]
