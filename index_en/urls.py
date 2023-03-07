from django.urls import path
from index_en import views

urlpatterns = [
    path('', views.index_en),
]