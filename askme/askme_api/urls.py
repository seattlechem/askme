from django.urls import path
from .views import AskViewApi


urlpatterns = [
    path('ask/', AskViewApi.as_view(), name='ask_api')
]
