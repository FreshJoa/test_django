
from django.urls import path
from .views import movies_list, new_movie, edit_movie, delete_movie



urlpatterns = [
    path('movies/', movies_list, name='movies_list'),
    path('new/', new_movie, name='new_movie'),
    path('edit/<int:id>/', edit_movie, name ='edit_movie'),
    path('delete/<int:id>/', delete_movie, name='delete_movie')

]
