from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_students, name='list_students'),
    path('add/', views.details_form, name='add_student'),
    path('edit/<int:details_id>/', views.details_form, name='edit_student'),
    ]
