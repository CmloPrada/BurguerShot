import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'burguershot.settings')
django.setup()

from menu.models import Category, Product

# Limpiar datos existentes
print("Limpiando datos existentes...")
Product.objects.all().delete()
Category.objects.all().delete()

# Crear categorías
print("Creando categorías...")
hamburguesas = Category.objects.create(
    name="Hamburguesas",
    description="Nuestras deliciosas hamburguesas artesanales",
    order=1
)

bebidas = Category.objects.create(
    name="Bebidas",
    description="Bebidas frías y refrescantes",
    order=2
)

acompañamientos = Category.objects.create(
    name="Acompañamientos",
    description="Los mejores complementos para tu hamburguesa",
    order=3
)

postres = Category.objects.create(
    name="Postres",
    description="Endulza tu experiencia",
    order=4
)

# Crear productos - Hamburguesas
print("Creando productos...")

Product.objects.create(
    name="Clásica",
    description="Carne de res, lechuga, tomate, cebolla, queso cheddar y nuestra salsa especial",
    price=15000,
    category=hamburguesas,
    available=True
)

Product.objects.create(
    name="Doble Carne",
    description="Doble carne de res, doble queso, bacon crujante, cebolla caramelizada",
    price=22000,
    category=hamburguesas,
    available=True
)

Product.objects.create(
    name="BBQ Crispy",
    description="Carne de res, aros de cebolla, bacon, queso, salsa BBQ ahumada",
    price=20000,
    category=hamburguesas,
    available=True
)

Product.objects.create(
    name="Vegetariana",
    description="Hamburguesa de lentejas y quinoa, aguacate, vegetales frescos, alioli",
    price=16000,
    category=hamburguesas,
    available=True
)

Product.objects.create(
    name="Pollo Crispy",
    description="Pechuga de pollo empanizada, lechuga, tomate, salsa ranch",
    price=17000,
    category=hamburguesas,
    available=True
)

Product.objects.create(
    name="Mexicana",
    description="Carne de res, jalapeños, guacamole, pico de gallo, queso pepper jack",
    price=19000,
    category=hamburguesas,
    available=True
)

# Bebidas
Product.objects.create(
    name="Coca-Cola",
    description="Coca-Cola 400ml",
    price=3500,
    category=bebidas,
    available=True
)

Product.objects.create(
    name="Coca-Cola Zero",
    description="Coca-Cola Zero 400ml",
    price=3500,
    category=bebidas,
    available=True
)

Product.objects.create(
    name="Sprite",
    description="Sprite 400ml",
    price=3500,
    category=bebidas,
    available=True
)

Product.objects.create(
    name="Limonada Natural",
    description="Limonada natural con hierbabuena",
    price=5000,
    category=bebidas,
    available=True
)

Product.objects.create(
    name="Agua",
    description="Agua mineral 500ml",
    price=2500,
    category=bebidas,
    available=True
)

Product.objects.create(
    name="Cerveza",
    description="Cerveza nacional 330ml",
    price=6000,
    category=bebidas,
    available=True
)

# Acompañamientos
Product.objects.create(
    name="Papas Francesas",
    description="Papas fritas crujientes con sal marina",
    price=7000,
    category=acompañamientos,
    available=True
)

Product.objects.create(
    name="Papas con Cheddar y Bacon",
    description="Papas fritas con queso cheddar fundido y bacon",
    price=10000,
    category=acompañamientos,
    available=True
)

Product.objects.create(
    name="Aros de Cebolla",
    description="Aros de cebolla empanizados y fritos",
    price=8000,
    category=acompañamientos,
    available=True
)

Product.objects.create(
    name="Nuggets de Pollo",
    description="8 nuggets de pollo con salsa a elección",
    price=9000,
    category=acompañamientos,
    available=True
)

Product.objects.create(
    name="Ensalada",
    description="Ensalada mixta con aderezo de la casa",
    price=8000,
    category=acompañamientos,
    available=True
)

# Postres
Product.objects.create(
    name="Brownie con Helado",
    description="Brownie de chocolate caliente con helado de vainilla",
    price=9000,
    category=postres,
    available=True
)

Product.objects.create(
    name="Milkshake de Chocolate",
    description="Milkshake cremoso de chocolate",
    price=8000,
    category=postres,
    available=True
)

Product.objects.create(
    name="Milkshake de Fresa",
    description="Milkshake cremoso de fresa",
    price=8000,
    category=postres,
    available=True
)

Product.objects.create(
    name="Helado",
    description="2 bolas de helado (vainilla, chocolate o fresa)",
    price=6000,
    category=postres,
    available=True
)

print("✓ Datos de ejemplo cargados exitosamente!")
print(f"- {Category.objects.count()} categorías creadas")
print(f"- {Product.objects.count()} productos creados")