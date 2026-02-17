from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Cliente
from app import db
from app.routes.main import login_required

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/clientes')
@login_required
def lista_clientes():
    clientes = Cliente.query.all()
    return render_template('clientes/lista.html', clientes=clientes)

@clientes_bp.route('/cliente/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_cliente():
    if request.method == 'POST':
        cliente = Cliente(
            nombre=request.form['nombre'],
            apellido=request.form['apellido'],
            telefono=request.form['telefono'],
            direccion=request.form['direccion'],
            correo=request.form['correo']
        )
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('clientes.detalle_cliente', id=cliente.id_cliente))
    return render_template('clientes/form.html')

@clientes_bp.route('/cliente/<int:id>')
@login_required
def detalle_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    return render_template('clientes/detalle.html', cliente=cliente)
