from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status, viewsets


# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f'Returned {len(books)} books',
            'data': serializer_data
        }
        return Response(data)


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApiView(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data = {
                'status': f'Kitob nomi: {book.title}',
                'book': serializer_data,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response({"status": "Does not exists", "message": "Bunday kitob mavjud emas"},
                            status=status.HTTP_404_NOT_FOUND)



# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response({"status": True, "message": "Successuly deleted"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"status": False, "message": "Book not found"}, status=status.HTTP_400_BAD_REQUEST)


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {
                "status": True,
                "message": f"Book {book_saved} Successfully updated",
            }
        )



# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'status': f'Book created',
                'books': data,
            }
            return Response(data)
        else:
            return Response(data={"status": False, "message": "serializer is not found"}, status=status.HTTP_400_BAD_REQUEST)

class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet): # Birgina shu view set orqali barcha viewlarni ishlatish mumkin
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# Function based view in DRF
@api_view(['GET'])              # Funksiya yordamida qilish hozirda deyarli ishlatilinmaydi
def book_list_view(request, *args, **kwargs):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)