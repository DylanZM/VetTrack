from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import Usuario
from app import db
from functools import wraps

usuarios_bp = Blueprint('usuarios', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        if session.get('user_role') != 'Admin':
            flash('Acceso denegado. Solo administradores.', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@usuarios_bp.route('/usuarios')
@admin_required
def lista_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios/lista.html', usuarios=usuarios)

@usuarios_bp.route('/usuario/nuevo', methods=['GET', 'POST'])
@admin_required
def nuevo_usuario():
    if request.method == 'POST':
        # Check if user already exists
        existing_user = Usuario.query.filter_by(correo=request.form['correo']).first()
        if existing_user:
            flash('El correo ya está registrado', 'danger')
            return redirect(url_for('usuarios.nuevo_usuario'))
        
        # Create new user
        new_user = Usuario(
            nombre=request.form['nombre'],
            apellido=request.form['apellido'],
            correo=request.form['correo'],
            rol=request.form['rol']
        )
        new_user.set_password(request.form['password'])
        
        db.session.add(new_user)
        db.session.commit()
        
        flash(f'Usuario {new_user.nombre} {new_user.apellido} creado exitosamente.', 'success')
        return redirect(url_for('usuarios.lista_usuarios'))
    
    return render_template('usuarios/form.html')

@usuarios_bp.route('/usuario/editar/<int:id>', methods=['GET', 'POST'])
@admin_required
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    
    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.apellido = request.form['apellido']
        usuario.correo = request.form['correo']
        usuario.rol = request.form['rol']
        
        # Only update password if provided
        if request.form.get('password'):
            usuario.set_password(request.form['password'])
        
        db.session.commit()
        flash(f'Usuario {usuario.nombre} {usuario.apellido} actualizado.', 'success')
        return redirect(url_for('usuarios.lista_usuarios'))
    
    return render_template('usuarios/form.html', usuario=usuario)

@usuarios_bp.route('/usuario/toggle/<int:id>')
@admin_required
def toggle_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    usuario.activo = not usuario.activo
    db.session.commit()
    
    status = 'activado' if usuario.activo else 'desactivado'
    flash(f'Usuario {usuario.nombre} {usuario.apellido} {status}.', 'success')
    return redirect(url_for('usuarios.lista_usuarios'))
