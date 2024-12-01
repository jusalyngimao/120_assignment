from django.contrib import admin
from django.urls import path, include
from sms import views  # Import the view to handle the root path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_sms/', views.send_sms_view, name='send_sms'),  # Path for sending SMS
    path('', views.welcome_view, name='home'),  # Root path now points to the welcome page
]
