from django.urls import path, include
from .views import ProcessImage

urlpatterns = [
    path('process-image', ProcessImage.as_view()),
]