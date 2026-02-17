import React, { useState } from 'react';

const CheckoutForm = ({ cart, onSubmitOrder, onCancel }) => {
  const [formData, setFormData] = useState({
    customer_name: '',
    customer_phone: '',
    customer_email: '',
    delivery_type: 'pickup',
    address: '',
    address_notes: '',
    payment_method: 'efectivo',
    notes: ''
  });

  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    // Limpiar error del campo cuando el usuario empieza a escribir
    if (errors[name]) {
      setErrors(prev => ({
        ...prev,
        [name]: ''
      }));
    }
  };

  const validate = () => {
    const newErrors = {};

    if (!formData.customer_name.trim()) {
      newErrors.customer_name = 'El nombre es obligatorio';
    }

    if (!formData.customer_phone.trim()) {
      newErrors.customer_phone = 'El teléfono es obligatorio';
    }

    if (formData.delivery_type === 'delivery' && !formData.address.trim()) {
      newErrors.address = 'La dirección es obligatoria para delivery';
    }

    return newErrors;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    const validationErrors = validate();
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }

    // Preparar datos del pedido
    const orderData = {
      ...formData,
      items: cart.map(item => ({
        product: item.id,
        quantity: item.quantity,
        unit_price: item.price
      }))
    };

    onSubmitOrder(orderData);
  };

  const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);

  return (
    <div className="checkout-form">
      <h2>Finalizar Pedido</h2>
      
      <div className="order-summary">
        <h3>Resumen del Pedido</h3>
        {cart.map(item => (
          <div key={item.id} className="summary-item">
            <span>{item.quantity}x {item.name}</span>
            <span>${(item.price * item.quantity).toLocaleString('es-CO')}</span>
          </div>
        ))}
        <div className="summary-total">
          <strong>Total:</strong>
          <strong>${total.toLocaleString('es-CO')}</strong>
        </div>
      </div>

      <form onSubmit={handleSubmit}>
        <div className="form-section">
          <h3>Información de Contacto</h3>
          
          <div className="form-group">
            <label>Nombre Completo *</label>
            <input
              type="text"
              name="customer_name"
              value={formData.customer_name}
              onChange={handleChange}
              className={errors.customer_name ? 'error' : ''}
            />
            {errors.customer_name && <span className="error-message">{errors.customer_name}</span>}
          </div>

          <div className="form-group">
            <label>Teléfono *</label>
            <input
              type="tel"
              name="customer_phone"
              value={formData.customer_phone}
              onChange={handleChange}
              className={errors.customer_phone ? 'error' : ''}
            />
            {errors.customer_phone && <span className="error-message">{errors.customer_phone}</span>}
          </div>

          <div className="form-group">
            <label>Email (opcional)</label>
            <input
              type="email"
              name="customer_email"
              value={formData.customer_email}
              onChange={handleChange}
            />
          </div>
        </div>

        <div className="form-section">
          <h3>Tipo de Entrega</h3>
          
          <div className="form-group">
            <label className="radio-group">
              <input
                type="radio"
                name="delivery_type"
                value="pickup"
                checked={formData.delivery_type === 'pickup'}
                onChange={handleChange}
              />
              <span>Retiro en Local</span>
            </label>
            
            <label className="radio-group">
              <input
                type="radio"
                name="delivery_type"
                value="delivery"
                checked={formData.delivery_type === 'delivery'}
                onChange={handleChange}
              />
              <span>Delivery a Domicilio</span>
            </label>
          </div>

          {formData.delivery_type === 'delivery' && (
            <>
              <div className="form-group">
                <label>Dirección *</label>
                <textarea
                  name="address"
                  value={formData.address}
                  onChange={handleChange}
                  rows="3"
                  className={errors.address ? 'error' : ''}
                />
                {errors.address && <span className="error-message">{errors.address}</span>}
              </div>

              <div className="form-group">
                <label>Notas de Dirección (opcional)</label>
                <input
                  type="text"
                  name="address_notes"
                  value={formData.address_notes}
                  onChange={handleChange}
                  placeholder="Ej: Casa color blanco, portón negro"
                />
              </div>
            </>
          )}
        </div>

        <div className="form-section">
          <h3>Método de Pago</h3>
          
          <div className="form-group">
            <select
              name="payment_method"
              value={formData.payment_method}
              onChange={handleChange}
            >
              <option value="efectivo">Efectivo</option>
              <option value="debito">Tarjeta de Débito</option>
              <option value="credito">Tarjeta de Crédito</option>
              <option value="transferencia">Transferencia Bancaria</option>
            </select>
          </div>
        </div>

        <div className="form-section">
          <h3>Notas Adicionales (opcional)</h3>
          
          <div className="form-group">
            <textarea
              name="notes"
              value={formData.notes}
              onChange={handleChange}
              rows="3"
              placeholder="Alguna indicación especial para tu pedido..."
            />
          </div>
        </div>

        <div className="form-actions">
          <button type="button" className="btn-cancel" onClick={onCancel}>
            Cancelar
          </button>
          <button type="submit" className="btn-submit">
            Confirmar Pedido
          </button>
        </div>
      </form>
    </div>
  );
};

export default CheckoutForm;
