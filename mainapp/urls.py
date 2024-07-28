from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import HomePage

app_name = MainappConfig.name

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
]
