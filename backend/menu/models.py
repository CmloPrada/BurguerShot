from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    """Categoría de productos (Hamburguesas, Bebidas, Acompañamientos, etc.)"""
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(blank=True, verbose_name="Descripción")
    order = models.IntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class Product(models.Model):
    """Producto del menú"""
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Precio"
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="Categoría"
    )
    image = models.ImageField(
        upload_to='products/', 
        blank=True, 
        null=True,
        verbose_name="Imagen"
    )
    available = models.BooleanField(default=True, verbose_name="Disponible")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['category', 'name']
    
    def __str__(self):
        return f"{self.name} - ${self.price}"


class Order(models.Model):
    """Pedido realizado por un cliente"""
    
    PAYMENT_METHODS = [
        ('efectivo', 'Efectivo'),
        ('debito', 'Tarjeta de Débito'),
        ('credito', 'Tarjeta de Crédito'),
        ('transferencia', 'Transferencia Bancaria'),
    ]
    
    DELIVERY_TYPES = [
        ('pickup', 'Retiro en Local'),
        ('delivery', 'Delivery a Domicilio'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmado'),
        ('preparing', 'En Preparación'),
        ('ready', 'Listo'),
        ('delivered', 'Entregado'),
        ('cancelled', 'Cancelado'),
    ]
    
    # Información del cliente
    customer_name = models.CharField(max_length=200, verbose_name="Nombre del Cliente")
    customer_phone = models.CharField(max_length=20, verbose_name="Teléfono")
    customer_email = models.EmailField(blank=True, verbose_name="Email")
    
    # Tipo de entrega
    delivery_type = models.CharField(
        max_length=10,
        choices=DELIVERY_TYPES,
        verbose_name="Tipo de Entrega"
    )
    
    # Dirección (solo para delivery)
    address = models.TextField(blank=True, verbose_name="Dirección")
    address_notes = models.TextField(blank=True, verbose_name="Notas de Dirección")
    
    # Método de pago
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS,
        verbose_name="Método de Pago"
    )
    
    # Estado y total
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="Estado"
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Total"
    )
    
    # Notas adicionales
    notes = models.TextField(blank=True, verbose_name="Notas del Pedido")
    
    # Fechas
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Pedido #{self.id} - {self.customer_name} - ${self.total}"


class OrderItem(models.Model):
    """Ítem individual dentro de un pedido"""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Pedido"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name="Producto"
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Cantidad"
    )
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Precio Unitario"
    )
    
    class Meta:
        verbose_name = "Ítem de Pedido"
        verbose_name_plural = "Ítems de Pedido"
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name}"
    
    @property
    def subtotal(self):
        """Calcula el subtotal del ítem"""
        return self.quantity * self.unit_price
