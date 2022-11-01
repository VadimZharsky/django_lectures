from datetime import date
from django.urls import path
from . import views

#domain.com/first_app/
urlpatterns = [
    path("<str:topic>/", views.device_view, name = "topic-page"),
    path("<int:num_page>", views.num_page_view)
]