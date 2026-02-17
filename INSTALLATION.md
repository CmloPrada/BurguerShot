# 📖 Guía de Instalación Detallada - Burger Shop

## 🔧 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.8 o superior**: [Descargar Python](https://www.python.org/downloads/)
- **Node.js 14 o superior**: [Descargar Node.js](https://nodejs.org/)
- **npm** (viene con Node.js) o **yarn**

## 📥 Paso 1: Descargar el Proyecto

Descarga todos los archivos del proyecto y descomprime en una carpeta llamada `burger-shop`.

## 🐍 Paso 2: Configurar el Backend (Django)

### 2.1 Navegar a la carpeta del backend

```bash
cd burger-shop/backend
```

### 2.2 Crear entorno virtual

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2.3 Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2.4 Crear la base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 2.5 Crear superusuario (administrador)

```bash
python manage.py createsuperuser
```

Te pedirá:
- Username (nombre de usuario)
- Email (opcional)
- Password (contraseña - escríbela dos veces)

### 2.6 Cargar datos de ejemplo (opcional pero recomendado)

```bash
python manage.py shell < load_sample_data.py
```

### 2.7 Iniciar el servidor

```bash
python manage.py runserver
```

El backend estará disponible en: `http://localhost:8000`

Panel de administración: `http://localhost:8000/admin`

## ⚛️ Paso 3: Configurar el Frontend (React)

**Abre una nueva terminal** (mantén el backend corriendo en la otra)

### 3.1 Navegar a la carpeta del frontend

```bash
cd burger-shop/frontend
```

### 3.2 Instalar dependencias

```bash
npm install
```

### 3.3 Iniciar el servidor de desarrollo

```bash
npm start
```

El frontend se abrirá automáticamente en tu navegador en: `http://localhost:3000`

## ✅ Verificación

Si todo está correcto, deberías poder:

1. Ver el menú de hamburguesas en `http://localhost:3000`
2. Agregar productos al carrito
3. Realizar un pedido completo
4. Ver los pedidos en el panel de administración en `http://localhost:8000/admin`

## 🎨 Agregar Productos desde el Admin

1. Ve a `http://localhost:8000/admin`
2. Inicia sesión con el superusuario que creaste
3. Haz clic en "Productos" → "Agregar Producto"
4. Completa los campos:
   - Nombre
   - Descripción
   - Precio
   - Categoría
   - Imagen (opcional)
   - Disponible (marca el checkbox)
5. Guarda

## 🔧 Comandos Útiles

### Backend (Django)

```bash
# Crear migraciones después de cambiar modelos
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Recolectar archivos estáticos
python manage.py collectstatic

# Ejecutar tests
python manage.py test
```

### Frontend (React)

```bash
# Instalar nuevas dependencias
npm install nombre-paquete

# Crear build de producción
npm run build

# Ejecutar tests
npm test
```

## 🐛 Solución de Problemas

### Error: "Port 8000 is already in use"

El puerto ya está en uso. Puedes:
- Detener el proceso que usa el puerto 8000
- Usar otro puerto: `python manage.py runserver 8001`

### Error: "Module not found"

Asegúrate de haber activado el entorno virtual y haber instalado las dependencias.

### Error de CORS en el frontend

Verifica que en `backend/burger_shop/settings.py` esté configurado:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

### No se ven las imágenes de productos

Las imágenes deben estar en `backend/media/products/`. Asegúrate de que el servidor esté sirviendo archivos media.

## 📝 Notas Importantes

- **No uses esto en producción** sin antes:
  - Cambiar la `SECRET_KEY` en settings.py
  - Poner `DEBUG = False`
  - Configurar HTTPS
  - Usar una base de datos más robusta (PostgreSQL)
  - Configurar archivos estáticos y media en un servidor de archivos

## 🆘 Ayuda

Si tienes problemas, verifica:
1. Que ambos servidores estén corriendo
2. Que no haya errores en la consola
3. Que las URLs sean correctas
4. Que el backend responda en `http://localhost:8000/api/products/`
