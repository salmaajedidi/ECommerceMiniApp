from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
@api_view(['GET','POST'])
def products(request):
    
    #list all products and filter by stock
    if request.method == 'GET':
        in_stock = request.query_params.get('in_stock')
        if in_stock is not None:
            if in_stock.lower() == 'true':
                Products = Product.objects.filter(stock__gt=0)  
            elif in_stock.lower() == 'false':
                Products = Product.objects.filter(stock=0)
            else:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            Products = Product.objects.all()  

        serializer = ProductSerializer(Products, many=True)
        return Response(serializer.data)

    
    #create new product
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def details_Product(request, product_id):
    # Check if the product with the following product_id exists
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

    # Update the product stock
    if request.method == 'PUT':
        stock = request.data.get('stock')
        if stock is not None:
            product.stock = stock
            product.save()  
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        
        return Response({"detail": "The stock field is required."}, status=status.HTTP_400_BAD_REQUEST)

    # Delete the product
    elif request.method == 'DELETE':
        product.delete()
        return Response({"detail": "Product deleted successfully."}, status=status.HTTP_204_NO_CONTENT)