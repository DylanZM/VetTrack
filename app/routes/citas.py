from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Cita, Paciente
from app import db
from datetime import datetime
from app.routes.main import login_required

citas_bp = Blueprint('citas', __name__)

@citas_bp.route('/citas')
@login_required
def lista_citas():
    citas = Cita.query.order_by(Cita.fecha_cita.desc()).all()
    return render_template('citas/lista.html', citas=citas)

@citas_bp.route('/cita/nueva', methods=['GET', 'POST'])
@login_required
def nueva_cita():
    if request.method == 'POST':
        cita = Cita(
            id_paciente=request.form['id_paciente'],
            fecha_cita=datetime.strptime(request.form['fecha_cita'], '%Y-%m-%dT%H:%M'),
            motivo=request.form['motivo'],
            estado='Pendiente'
        )
        db.session.add(cita)
        db.session.commit()
        flash('Cita agendada exitosamente', 'success')
        return redirect(url_for('citas.lista_citas'))
    
    pacientes = Paciente.query.all()
    return render_template('citas/form.html', pacientes=pacientes)

@citas_bp.route('/cita/cambiar-estado/<int:id>/<estado>')
@login_required
def cambiar_estado(id, estado):
    cita = Cita.query.get_or_404(id)
    cita.estado = estado
    db.session.commit()
    flash(f'Cita marcada como {estado}', 'success')
    return redirect(url_for('citas.lista_citas'))
