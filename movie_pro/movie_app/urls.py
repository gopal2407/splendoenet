from django.urls import path
from .views import review_form, review_data, review_delete, review_update, search_tile_director
from .views import search_tile_director, filter_genres, filter_status

urlpatterns = [
    path('form/', review_form, name='form_url'),
    path('data/', review_data, name='data_url'),
    path('update/<int:pk>/', review_update, name='update_url'),
    path('delete/<int:pk>/', review_delete, name='delete_url'),
    path('search/', search_tile_director, name='search_url'),
    path('filter-genres/', filter_genres, name='genres_url'),
    path('filter-status/', filter_status, name='status_url'),

]