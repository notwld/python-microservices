from rest_framework import viewsets

from .models import Product

from .serializer import ProductSerializer
from rest_framework.response import Response


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        product = Product.objects.create(
            title=request.data['title'],
            price=request.data['price'],
            likes=0,
            img=request.data['img']
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.title = request.data['title']
        product.price = request.data['price']
        product.likes = request.data['likes']
        product.img = request.data['img']

        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response('Item deleted')
