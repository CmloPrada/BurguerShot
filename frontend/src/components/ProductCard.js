import React from 'react';

const ProductCard = ({ product, onAddToCart }) => {
  return (
    <div className="product-card">
      {product.image && (
        <div className="product-image">
          <img src={product.image} alt={product.name} />
        </div>
      )}
      <div className="product-info">
        <h3>{product.name}</h3>
        <p className="product-description">{product.description}</p>
        <div className="product-footer">
          <span className="product-price">${parseFloat(product.price).toLocaleString('es-CO')}</span>
          <button 
            className="btn-add-cart"
            onClick={() => onAddToCart(product)}
          >
            Agregar
          </button>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;
