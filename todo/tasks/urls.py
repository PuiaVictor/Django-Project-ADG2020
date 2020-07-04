from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
	path('', views.index, name="list"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
=======
    path('', views.index, name="list"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
>>>>>>> 7050fdafe5b8eedc939e765afe4e4e2869ff178b
]