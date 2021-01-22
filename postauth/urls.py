from django.urls import path
from .views import LoginTokenAuth


urlpatterns = [
    path('login/', LoginTokenAuth.as_view())
]
