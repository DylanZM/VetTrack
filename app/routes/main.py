from flask import Blueprint, render_template, session, redirect, url_for
from app.models import Paciente, Cliente, Cita, Producto, db
from datetime import datetime
from functools import wraps

main_bp = Blueprint('main', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@main_bp.route('/')
def landing():
    # If user is logged in, redirect to dashboard
    if 'user_id' in session:
        return redirect(url_for('main.index'))
    return render_template('landing.html')

@main_bp.route('/dashboard')
@login_required
def index():
    # Dashboard stats
    total_pacientes = Paciente.query.count()
    total_clientes = Cliente.query.count()
    citas_hoy = Cita.query.filter(db.func.date(Cita.fecha_cita) == datetime.today().date()).count()
    total_productos = Producto.query.filter_by(activo=True).count()
    
    return render_template('index.html', 
                           total_pacientes=total_pacientes, 
                           total_clientes=total_clientes, 
                           citas_hoy=citas_hoy,
                           total_productos=total_productos)
