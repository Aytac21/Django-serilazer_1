# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

# serailzer list create detail
@api_view(["GET"])
def list_View(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset,many=True)
    return Response(serializer.data)

@api_view(["POST"])
def create_View(request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["GET"])
def detail_View(request,id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)