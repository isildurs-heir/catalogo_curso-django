from django.urls import path, include
from catalogo import views

urlpatterns = [
    path('',views.index, name='index'),
    path('authors/',views.AuthorListView.as_view(),name='authors'),
    path('author/<pk>',views.AuthorDetail,name='author'),
    path('books/',views.BookListView.as_view(),name='books'),
    path('book/<pk>',views.BookDetail,name='book'),
    path('generos/', views.GenreListView.as_view(),name='generos'),
    path('genero/new/', views.genre_new, name='genero_new'),
    path('genero/update/<pk>',views.genre_update, name='genero_update'),
    path('test-ajax/',views.test_ajax,name='test'),
    path('test-ajax/data',views.getData,name ='xd'),
]  