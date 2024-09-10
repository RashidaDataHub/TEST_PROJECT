from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('insert-example/', views.insert_example_data, name='insert_example_data'),
]