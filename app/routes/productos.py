from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Producto
from app import db
from app.routes.main import login_required

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/productos')
@login_required
def lista_productos():
    productos = Producto.query.filter_by(activo=True).all()
    return render_template('productos/lista.html', productos=productos)

@productos_bp.route('/producto/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_producto():
    if request.method == 'POST':
        producto = Producto(
            nombre=request.form['nombre'],
            descripcion=request.form['descripcion'],
            precio=float(request.form['precio']),
            categoria=request.form['categoria'],
            stock=int(request.form['stock']),
            activo=True
        )
        db.session.add(producto)
        db.session.commit()
        flash('Producto agregado exitosamente', 'success')
        return redirect(url_for('productos.lista_productos'))
    
    return render_template('productos/form.html')

@productos_bp.route('/producto/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_producto(id):
    producto = Producto.query.get_or_404(id)
    
    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descripcion']
        producto.precio = float(request.form['precio'])
        producto.categoria = request.form['categoria']
        producto.stock = int(request.form['stock'])
        
        db.session.commit()
        flash('Producto actualizado', 'success')
        return redirect(url_for('productos.lista_productos'))
    
    return render_template('productos/form.html', producto=producto)
