from rest_framework import serializers
from .models import Book

class ReadOnlyBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['status']

    
class StorekeeperBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class LibrarianBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

