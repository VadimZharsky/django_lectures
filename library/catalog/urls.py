from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('all_books/', views.all_books, name='all_books'),
    path('get_a_book/', views.get_a_book, name='get_a_book'),
    path('create_book/',views.BookCreate.as_view(),name='create_book'),
    path('book/<int:pk>/',views.BookDetail.as_view(),name='book_detail'),   
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.CheckedOutBooksByUserView.as_view(),name='profile')
    
]