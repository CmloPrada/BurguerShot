# 🍔 Burger Shop - Sistema de Pedidos Online

Aplicación web completa para un local de hamburguesas con Django (Backend) y React (Frontend).

## 🚀 Características

- Visualización del menú de productos
- Carrito de compras interactivo
- Resumen de pedido
- Selección de método de pago (sin pasarela de pago)
- Opción de retiro en local o delivery a domicilio
- API RESTful con Django REST Framework
- Frontend moderno con React

## 📋 Requisitos

- Python 3.8+
- Node.js 14+
- npm o yarn

## 🛠️ Instalación

### Backend (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

El backend estará corriendo en `http://localhost:8000`

### Frontend (React)

```bash
cd frontend
npm install
npm start
```

El frontend estará corriendo en `http://localhost:3000`

## 📁 Estructura del Proyecto

```
burger-shop/
├── backend/
│   ├── burger_shop/          # Configuración del proyecto Django
│   ├── menu/                 # App de menú y pedidos
│   ├── manage.py
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/       # Componentes React
    │   ├── services/         # Servicios API
    │   ├── App.js
    │   └── index.js
    ├── public/
    └── package.json
```

## 🎯 Uso

1. Accede al admin de Django en `http://localhost:8000/admin` para agregar productos
2. Abre la aplicación en `http://localhost:3000`
3. Navega por el menú y agrega productos al carrito
4. Completa el formulario de pedido con:
   - Método de pago (Efectivo, Tarjeta débito, Tarjeta crédito, Transferencia)
   - Tipo de entrega (Retiro en local o Delivery)
   - Datos de contacto y dirección (si es delivery)

## 📝 API Endpoints

- `GET /api/products/` - Lista todos los productos
- `GET /api/products/{id}/` - Detalle de un producto
- `POST /api/orders/` - Crear un nuevo pedido
- `GET /api/orders/` - Lista todos los pedidos
- `GET /api/orders/{id}/` - Detalle de un pedido

## 🔧 Personalización

Puedes personalizar:
- Categorías de productos en `backend/menu/models.py`
- Estilos en `frontend/src/App.css`
- Métodos de pago en `backend/menu/models.py`
- Configuración del proyecto en `backend/burger_shop/settings.py`
