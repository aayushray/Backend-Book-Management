from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework import viewsets, status, generics

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def books(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            book = Book.objects.get(id=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        else:
            queryset = Book.objects.all()
            serializer = BookSerializer(queryset, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=400)
    
    elif request.method == 'PUT':
        book = Book.objects.all(id=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=400)
    
    elif request.method == 'DELETE':
        book = Book.objects.get(id=pk)
        book.delete()
        return Response(status=204)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def authors(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            author = Author.objects.get(id=pk)
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        else:
            queryset = Author.objects.all()
            serializer = AuthorSerializer(queryset, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=400)
    
    elif request.method == 'PUT':
        author = Author.objects.all(id=pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=400)
    
    elif request.method == 'DELETE':
        author = Author.objects.get(id=pk)
        author.delete()
        return Response(status=204)
    
@api_view(['GET', 'POST'])
def create_order(request):
    if request.method == 'GET':
        book_ids = request.query_params.getlist('book_ids', [])
        customer_name = request.query_params.get('customer_name', '')
        return Response({"book_ids": book_ids, "customer_name": customer_name})

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            book_ids = request.data['book_id']
            customer_name = request.data['customer_name']

            total_cost = 0
            for book_id in book_ids:
                book = Book.objects.get(id=book_id)
                if book.quantity_in_stock == 0:
                    return Response({'error': f'Book with ID {book_id} is out of stock.'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    book.quantity_in_stock -= 1
                    book.save()
                    customer_order = Order.objects.create(book=book, customer_name=customer_name)
                total_cost += book.price

            order = serializer.save(total_cost=total_cost, customer_name=customer_name)
            return Response(order, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def customerOrders(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            order = Order.objects.get(id=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        orders = Order.objects.all()
        serializer = CustomerSerializer(orders, many=True)
        return Response(serializer.data)