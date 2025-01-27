from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'content', 'title', 'subtitle', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # check title if it conteins only alphabrtical chars
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavhasi harflardan iborat bo'lishi kerak!"
                }
            )

        #check title and author from database existence
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavhasi va muallifi bir xil bo'lgan kitobni saqlay olmaysiz!"
                }
            )
        return data

    def validate_price(self, price):
        if price <=0 or price >= 999999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx notogri kiritilgan!"
                }
            )

