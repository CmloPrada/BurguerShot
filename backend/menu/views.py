from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Product, Order
from .serializers import (
    CategorySerializer, ProductSerializer, 
    OrderSerializer, OrderCreateSerializer
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        categories = Category.objects.prefetch_related('products').all()
        result = []
        
        for category in categories:
            products = category.products.filter(available=True)
            if products.exists():
                result.append({
                    'id': category.id,
                    'name': category.name,
                    'description': category.description,
                    'products': ProductSerializer(products, many=True).data
                })
        
        return Response(result)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        return OrderSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        
        # Retornar la orden completa con todos los detalles
        output_serializer = OrderSerializer(order)
        return Response(
            output_serializer.data,
            status=status.HTTP_201_CREATED
        )
    
    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        order = self.get_object()
        new_status = request.data.get('status')
        
        if new_status not in dict(Order.STATUS_CHOICES):
            return Response(
                {'error': 'Estado inválido'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        order.status = new_status
        order.save()
        
        serializer = OrderSerializer(order)
        return Response(serializer.data)
