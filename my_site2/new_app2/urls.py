from django.urls import path
from . import views

app_name = "new_app2"

urlpatterns = [
    path('example/', views.simple_view, name = "simple"),
    path('variable/', views.variable_view, name="variable"),
]
