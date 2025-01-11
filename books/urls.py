from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookListApiView, BookDetailApiView, BookDeleteApiView, BookUpdateApiView, \
    BookCreateApiView, BookListCreateApiView, BookUpdateDeleteView, \
    BookViewSet

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
#     path('books/', BookListApiView.as_view(), name='book-list'),
#     path('book-list-create/', BookListCreateApiView.as_view(), name='book-list-create'),
#     path('book-update-delete/<int:pk>/', BookUpdateDeleteView.as_view(), name='book-update-delete'),
#     path('books/create/', BookCreateApiView.as_view(), name='book-create'),
#     path('books/<int:pk>/', BookDetailApiView.as_view(), name='book-detail'),
#     path('books/<int:pk>/update/', BookUpdateApiView.as_view(), name='book-update'),
#     path('books/<int:pk>/delete/', BookDeleteApiView.as_view(), name='book-delete'),
]

urlpatterns += router.urls