import React from 'react';

const Cart = ({ cart, onUpdateQuantity, onRemoveItem, onCheckout }) => {
  const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);

  if (cart.length === 0) {
    return (
      <div className="cart empty-cart">
        <h2>Carrito de Compras</h2>
        <p>Tu carrito está vacío</p>
      </div>
    );
  }

  return (
    <div className="cart">
      <h2>Carrito de Compras</h2>
      <div className="cart-items">
        {cart.map((item) => (
          <div key={item.id} className="cart-item">
            <div className="cart-item-info">
              <h4>{item.name}</h4>
              <p className="cart-item-price">${parseFloat(item.price).toLocaleString('es-CO')}</p>
            </div>
            <div className="cart-item-actions">
              <button 
                className="btn-quantity"
                onClick={() => onUpdateQuantity(item.id, item.quantity - 1)}
                disabled={item.quantity <= 1}
              >
                -
              </button>
              <span className="quantity">{item.quantity}</span>
              <button 
                className="btn-quantity"
                onClick={() => onUpdateQuantity(item.id, item.quantity + 1)}
              >
                +
              </button>
              <button 
                className="btn-remove"
                onClick={() => onRemoveItem(item.id)}
              >
                🗑️
              </button>
            </div>
            <div className="cart-item-subtotal">
              ${(item.price * item.quantity).toLocaleString('es-CO')}
            </div>
          </div>
        ))}
      </div>
      <div className="cart-total">
        <h3>Total: ${total.toLocaleString('es-CO')}</h3>
        <button className="btn-checkout" onClick={onCheckout}>
          Proceder al Pago
        </button>
      </div>
    </div>
  );
};

export default Cart;
