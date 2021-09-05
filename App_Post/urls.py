from django.urls import path

from App_Post import views

urlpatterns = [
    path("", views.home, name="home")
]
