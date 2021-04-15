from django.urls import path

from .views import homeView


app_name = "store"
urlpatterns = [
    path("", homeView, name="home"),
]
