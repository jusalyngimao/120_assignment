from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),  # Welcome page
    path('send_sms/', views.send_sms_view, name='send_sms'),  # Render send_sms page when clicking link
]