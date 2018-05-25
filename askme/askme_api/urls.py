from django.urls import path
from .views import AskViewApi, AudioViewApi


urlpatterns = [
    path('ask/', AskViewApi.as_view(), name='ask_api'),
    path('audio/', AudioViewApi.as_view(), name='ask_api'),
]
