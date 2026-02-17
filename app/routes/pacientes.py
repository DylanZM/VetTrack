from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models import Paciente, Cliente
from app import db
from app.routes.main import login_required

pacientes_bp = Blueprint('pacientes', __name__)

@pacientes_bp.route('/mascotas')
@login_required
def lista_pacientes():
    pacientes = Paciente.query.all()
    return render_template('pacientes/lista.html', pacientes=pacientes)

@pacientes_bp.route('/paciente/nuevo/<int:cliente_id>', methods=['GET', 'POST'])
@login_required
def nuevo_paciente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    if request.method == 'POST':
        from datetime import datetime
        bday_str = request.form['fecha_nacimiento']
        bday = datetime.strptime(bday_str, '%Y-%m-%d').date() if bday_str else None
        
        paciente = Paciente(
            nombre=request.form['nombre'],
            especie=request.form['especie'],
            raza=request.form['raza'],
            fecha_nacimiento=bday,
            peso=float(request.form['peso']) if request.form['peso'] else None,
            id_cliente=cliente.id_cliente
        )
        db.session.add(paciente)
        db.session.commit()
        return redirect(url_for('clientes.detalle_cliente', id=cliente.id_cliente))
    return render_template('pacientes/form.html', cliente=cliente)

@pacientes_bp.route('/paciente/<int:id>')
@login_required
def detalle_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    return render_template('pacientes/detalle.html', paciente=paciente)

@pacientes_bp.route('/visita/nueva/<int:paciente_id>', methods=['GET', 'POST'])
@login_required
def nueva_visita(paciente_id):
    from app.models import Visita
    paciente = Paciente.query.get_or_404(paciente_id)
    if request.method == 'POST':
        visita = Visita(
            id_paciente=paciente.id_paciente,
            id_usuario=session.get('user_id'),
            motivo=request.form['motivo'],
            diagnostico=request.form['diagnostico'],
            observaciones=request.form['observaciones']
        )
        db.session.add(visita)
        db.session.commit()
        return redirect(url_for('pacientes.detalle_paciente', id=paciente.id_paciente))
    return render_template('visitas/form.html', paciente=paciente)

@pacientes_bp.route('/tratamiento/nuevo/<int:visita_id>', methods=['GET', 'POST'])
@login_required
def nuevo_tratamiento(visita_id):
    from app.models import Visita, Tratamiento
    visita = Visita.query.get_or_404(visita_id)
    if request.method == 'POST':
        tratamiento = Tratamiento(
            id_visita=visita.id_visita,
            medicamento=request.form['medicamento'],
            dosis=request.form['dosis'],
            duracion=request.form['duracion'],
            indicaciones=request.form['indicaciones']
        )
        db.session.add(tratamiento)
        db.session.commit()
        return redirect(url_for('pacientes.detalle_paciente', id=visita.paciente.id_paciente))
    return render_template('tratamientos/form.html', visita=visita)
