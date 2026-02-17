from rest_framework import serializers
from .models import Category, Product, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    """Serializador para categorías"""
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'order']


class ProductSerializer(serializers.ModelSerializer):
    """Serializador para productos"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 
            'category', 'category_name', 'image', 
            'available', 'created_at', 'updated_at'
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializador para ítems de pedido"""
    product_name = serializers.CharField(source='product.name', read_only=True)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'unit_price', 'subtotal']


class OrderSerializer(serializers.ModelSerializer):
    """Serializador para pedidos"""
    items = OrderItemSerializer(many=True)
    payment_method_display = serializers.CharField(source='get_payment_method_display', read_only=True)
    delivery_type_display = serializers.CharField(source='get_delivery_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id', 'customer_name', 'customer_phone', 'customer_email',
            'delivery_type', 'delivery_type_display', 'address', 'address_notes',
            'payment_method', 'payment_method_display', 'status', 'status_display',
            'total', 'notes', 'items', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        """Crear pedido con sus ítems"""
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        
        return order
    
    def validate(self, data):
        """Validaciones personalizadas"""
        # Si es delivery, la dirección es obligatoria
        if data.get('delivery_type') == 'delivery' and not data.get('address'):
            raise serializers.ValidationError({
                'address': 'La dirección es obligatoria para pedidos con delivery.'
            })
        
        # Validar que hay ítems en el pedido
        items = data.get('items', [])
        if not items:
            raise serializers.ValidationError({
                'items': 'El pedido debe tener al menos un producto.'
            })
        
        # Calcular total
        total = sum(item['quantity'] * item['unit_price'] for item in items)
        data['total'] = total
        
        return data


class OrderCreateSerializer(serializers.ModelSerializer):
    """Serializador simplificado para crear pedidos desde el frontend"""
    items = OrderItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = [
            'customer_name', 'customer_phone', 'customer_email',
            'delivery_type', 'address', 'address_notes',
            'payment_method', 'notes', 'items'
        ]
    
    def create(self, validated_data):
        """Crear pedido con sus ítems"""
        items_data = validated_data.pop('items')
        
        # Calcular el total
        total = sum(item['quantity'] * item['unit_price'] for item in items_data)
        
        # Crear el pedido
        order = Order.objects.create(total=total, **validated_data)
        
        # Crear los ítems
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        
        return order
    
    def validate(self, data):
        """Validaciones personalizadas"""
        # Si es delivery, la dirección es obligatoria
        if data.get('delivery_type') == 'delivery' and not data.get('address'):
            raise serializers.ValidationError({
                'address': 'La dirección es obligatoria para pedidos con delivery.'
            })
        
        # Validar que hay ítems en el pedido
        items = data.get('items', [])
        if not items:
            raise serializers.ValidationError({
                'items': 'El pedido debe tener al menos un producto.'
            })
        
        return data
