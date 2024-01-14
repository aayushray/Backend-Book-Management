from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
class OrderSerializer(serializers.Serializer):
    book_id = serializers.ListField(child=serializers.IntegerField(), min_length=1,
        error_messages={
            'min_length': 'At least one book_id must be provided.'
        }
    )
    customer_name = serializers.CharField()
    
    def validate_book_id(self, value):
        invalid_book_ids = [book_id for book_id in value if not Book.objects.filter(id=book_id).exists()]
        if invalid_book_ids:
            raise serializers.ValidationError(f"The following book_ids do not exist: {', '.join(map(str, invalid_book_ids))}")
        return value
    
    def create(self, validated_data):
        return {'Total Cost': validated_data['total_cost']}

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
