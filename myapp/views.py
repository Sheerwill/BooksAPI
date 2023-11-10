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

'''class GroupRequiredMixin(permissions.BasePermission):
    group_required = None

    def has_permission(self, request, view):
        if self.group_required is None:
            return False
        return request.user.groups.filter(name=self.storekeepers).exists()'''

class StorekeeperBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = StorekeeperBookSerializer   
    permission_classes = [IsStorekeeper]

    '''def test_func(self):
        return self.request.user.groups.filter(name=self.group_required).exists()'''
    

class LibrarianBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = LibrarianBookSerializer
    permission_classes = [IsLibrarian]
