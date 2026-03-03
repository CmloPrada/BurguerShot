import React, { useState, useEffect } from 'react';
import { menuAPI } from './services/api';
import ProductCard from './components/ProductCard';
import Cart from './components/Cart';
import CheckoutForm from './components/CheckoutForm';
import OrderConfirmation from './components/OrderConfirmation';
import './App.css';

function App() {
  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState([]);
  const [cart, setCart] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [currentStep, setCurrentStep] = useState('menu');
  const [confirmedOrder, setConfirmedOrder] = useState(null);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      setLoading(true);
      const response = await menuAPI.getProductsByCategory();
      setCategories(response.data);
      
      // Extraer todos los productos de todas las categorías
      const allProducts = response.data.reduce((acc, category) => {
        return [...acc, ...category.products];
      }, []);
      setProducts(allProducts);
      
      setLoading(false);
    } catch (err) {
      console.error('Error fetching products:', err);
      setError('Error al cargar el menú. Por favor, intenta de nuevo.');
      setLoading(false);
    }
  };

  const addToCart = (product) => {
    setCart(prevCart => {
      const existingItem = prevCart.find(item => item.id === product.id);
      
      if (existingItem) {
        return prevCart.map(item =>
          item.id === product.id
            ? { ...item, quantity: item.quantity + 1 }
            : item
        );
      }
      
      return [...prevCart, { ...product, quantity: 1 }];
    });
  };

  const updateQuantity = (productId, newQuantity) => {
    if (newQuantity < 1) return;
    
    setCart(prevCart =>
      prevCart.map(item =>
        item.id === productId
          ? { ...item, quantity: newQuantity }
          : item
      )
    );
  };

  const removeFromCart = (productId) => {
    setCart(prevCart => prevCart.filter(item => item.id !== productId));
  };

  const handleCheckout = () => {
    setCurrentStep('checkout');
  };

  const handleSubmitOrder = async (orderData) => {
    try {
      setLoading(true);
      const response = await menuAPI.createOrder(orderData);
      setConfirmedOrder(response.data);
      setCurrentStep('confirmation');
      setCart([]);
      setLoading(false);
    } catch (err) {
      console.error('Error creating order:', err);
      alert('Error al crear el pedido. Por favor, intenta de nuevo.');
      setLoading(false);
    }
  };

  const handleCancelCheckout = () => {
    setCurrentStep('menu');
  };

  const handleNewOrder = () => {
    setCurrentStep('menu');
    setConfirmedOrder(null);
  };

  if (loading && products.length === 0) {
    return <div className="loading">Cargando menú...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="App">
      <header className="app-header">
        <h1>🍔 BurguerShot</h1>
        <p>Las mejores hamburguesas de la ciudad</p>
      </header>

      <div className="app-container">
        {currentStep === 'menu' && (
          <>
            <main className="menu-section">
              <h2>Nuestro Menú</h2>
              {categories.map((category) => (
                <div key={category.id} className="category-section">
                  <h3 className="category-title">{category.name}</h3>
                  {category.description && (
                    <p className="category-description">{category.description}</p>
                  )}
                  <div className="products-grid">
                    {category.products.map((product) => (
                      <ProductCard
                        key={product.id}
                        product={product}
                        onAddToCart={addToCart}
                      />
                    ))}
                  </div>
                </div>
              ))}
            </main>

            <aside className="cart-section">
              <Cart
                cart={cart}
                onUpdateQuantity={updateQuantity}
                onRemoveItem={removeFromCart}
                onCheckout={handleCheckout}
              />
            </aside>
          </>
        )}

        {currentStep === 'checkout' && (
          <div className="checkout-section">
            <CheckoutForm
              cart={cart}
              onSubmitOrder={handleSubmitOrder}
              onCancel={handleCancelCheckout}
            />
          </div>
        )}

        {currentStep === 'confirmation' && confirmedOrder && (
          <div className="confirmation-section">
            <OrderConfirmation
              order={confirmedOrder}
              onNewOrder={handleNewOrder}
            />
          </div>
        )}
      </div>

      <footer className="app-footer">
        <p>&copy; 2026 BurguerShot. Todos los derechos reservados.</p>
      </footer>
    </div>
  );
}

export default App;
