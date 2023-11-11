from rest_framework import generics, permissions
from .models import Book
from .serializers import ReadOnlyBookSerializer, StorekeeperBookSerializer, LibrarianBookSerializer
from .permissions import IsStorekeeper, IsLibrarian

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = ReadOnlyBookSerializer
    permission_classes = [permissions.IsAuthenticated] 

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = ReadOnlyBookSerializer
    permission_classes = [permissions.IsAuthenticated] 

class StorekeeperBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = StorekeeperBookSerializer   
    permission_classes = [IsStorekeeper]    

class LibrarianBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = LibrarianBookSerializer
    permission_classes = [IsLibrarian]
