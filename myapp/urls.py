from django.urls import path
from .views import (
    BookListCreateView,
    BookDetailView,
    StorekeeperBookDetailView,
    LibrarianBookDetailView,
)

urlpatterns = [
    # Book List and Create
    path('books/', BookListCreateView.as_view(), name='book-list-create'),

    # Book Detail
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Storekeeper Book Detail
    path('books/<int:pk>/storekeeper/', StorekeeperBookDetailView.as_view(), name='storekeeper-book-detail'),

    # Librarian Book Detail
    path('books/<int:pk>/librarian/', LibrarianBookDetailView.as_view(), name='librarian-book-detail'),
]