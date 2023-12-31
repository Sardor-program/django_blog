from django.urls import path
from windows.views import home, about, window

urlpatterns = [
    path('', home),
    path('about/', about),
    path('window/', window)
]

