from django.urls import path
from . import views

app_name='searchengine_app'

urlpatterns = [
    path('', views.getresults, name='getresults'),
]