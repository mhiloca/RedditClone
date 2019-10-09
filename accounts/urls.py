from django.urls import path

from .views import sign_up, log_in, log_out, dashboard

urlpatterns = [
    path('signup/', sign_up, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('dashboard/', dashboard, name='dashboard')
]
