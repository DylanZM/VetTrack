from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import Usuario
from app import db, limiter

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']
        user = Usuario.query.filter_by(correo=correo, activo=True).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id_usuario
            session['user_name'] = f"{user.nombre} {user.apellido}"
            session['user_role'] = user.rol
            return redirect(url_for('main.index'))
        else:
            flash('Correo o contraseña incorrectos, o usuario inactivo', 'danger')
            
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.landing'))

