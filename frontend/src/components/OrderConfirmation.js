import React from 'react';

const OrderConfirmation = ({ order, onNewOrder }) => {
  return (
    <div className="order-confirmation">
      <div className="confirmation-icon">✓</div>
      <h2>¡Pedido Confirmado!</h2>
      <p className="order-number">Número de Pedido: #{order.id}</p>
      
      <div className="confirmation-details">
        <div className="detail-section">
          <h3>Información del Cliente</h3>
          <p><strong>Nombre:</strong> {order.customer_name}</p>
          <p><strong>Teléfono:</strong> {order.customer_phone}</p>
          {order.customer_email && (
            <p><strong>Email:</strong> {order.customer_email}</p>
          )}
        </div>

        <div className="detail-section">
          <h3>Tipo de Entrega</h3>
          <p>{order.delivery_type_display}</p>
          {order.delivery_type === 'delivery' && (
            <>
              <p><strong>Dirección:</strong> {order.address}</p>
              {order.address_notes && (
                <p><strong>Notas:</strong> {order.address_notes}</p>
              )}
            </>
          )}
        </div>

        <div className="detail-section">
          <h3>Método de Pago</h3>
          <p>{order.payment_method_display}</p>
        </div>

        <div className="detail-section">
          <h3>Resumen del Pedido</h3>
          {order.items.map((item) => (
            <div key={item.id} className="order-item">
              <span>{item.quantity}x {item.product_name}</span>
              <span>${parseFloat(item.subtotal).toLocaleString('es-CO')}</span>
            </div>
          ))}
          <div className="order-total">
            <strong>Total:</strong>
            <strong>${parseFloat(order.total).toLocaleString('es-CO')}</strong>
          </div>
        </div>

        {order.notes && (
          <div className="detail-section">
            <h3>Notas</h3>
            <p>{order.notes}</p>
          </div>
        )}
      </div>

      <div className="confirmation-message">
        <p>Gracias por tu pedido. Te contactaremos pronto para confirmar los detalles.</p>
      </div>

      <button className="btn-new-order" onClick={onNewOrder}>
        Hacer Nuevo Pedido
      </button>
    </div>
  );
};

export default OrderConfirmation;
