from django.urls import path
from my_app.views import home

urlpatterns = [
    path('', home, name='home'),
]
