from django.contrib import admin
from .models import Category, Product, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Administración de categorías"""
    list_display = ['name', 'order']
    list_editable = ['order']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Administración de productos"""
    list_display = ['name', 'category', 'price', 'available', 'created_at']
    list_filter = ['category', 'available', 'created_at']
    list_editable = ['available']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'description', 'category')
        }),
        ('Precio y Disponibilidad', {
            'fields': ('price', 'available')
        }),
        ('Imagen', {
            'fields': ('image',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class OrderItemInline(admin.TabularInline):
    """Inline para mostrar ítems del pedido"""
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'unit_price', 'subtotal']
    can_delete = False
    
    def subtotal(self, obj):
        return f"${obj.subtotal}"
    subtotal.short_description = 'Subtotal'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Administración de pedidos"""
    list_display = [
        'id', 'customer_name', 'customer_phone', 
        'delivery_type', 'payment_method', 'status', 
        'total', 'created_at'
    ]
    list_filter = ['status', 'delivery_type', 'payment_method', 'created_at']
    search_fields = ['customer_name', 'customer_phone', 'customer_email']
    readonly_fields = ['created_at', 'updated_at', 'total']
    inlines = [OrderItemInline]
    
    fieldsets = (
        ('Información del Cliente', {
            'fields': ('customer_name', 'customer_phone', 'customer_email')
        }),
        ('Detalles de Entrega', {
            'fields': ('delivery_type', 'address', 'address_notes')
        }),
        ('Pago y Estado', {
            'fields': ('payment_method', 'status', 'total')
        }),
        ('Notas', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        """Hacer algunos campos de solo lectura después de crear el pedido"""
        if obj:  # Editando pedido existente
            return self.readonly_fields + ['customer_name', 'customer_phone', 
                                          'delivery_type', 'payment_method']
        return self.readonly_fields
