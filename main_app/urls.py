from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # All routes will be added here
    path('', views.home, name='home'),
    path("about/", views.about, name="about"),

]
