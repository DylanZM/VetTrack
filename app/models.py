from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(50), nullable=False)  # Admin / Empleado
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    activo = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(200))
    correo = db.Column(db.String(150))
    pacientes = db.relationship('Paciente', backref='cliente', lazy=True, cascade="all, delete-orphan")

class Paciente(db.Model):
    __tablename__ = 'pacientes'
    id_paciente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    raza = db.Column(db.String(100))
    fecha_nacimiento = db.Column(db.Date)
    peso = db.Column(db.Numeric(5, 2))
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'), nullable=False)
    visitas = db.relationship('Visita', backref='paciente', lazy=True, cascade="all, delete-orphan")
    citas = db.relationship('Cita', backref='paciente', lazy=True, cascade="all, delete-orphan")

    def edad(self):
        if self.fecha_nacimiento:
            today = datetime.today()
            return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return None

class Visita(db.Model):
    __tablename__ = 'visitas'
    id_visita = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id_paciente'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=True)
    fecha_visita = db.Column(db.DateTime, default=datetime.utcnow)
    motivo = db.Column(db.String(200), nullable=False)
    diagnostico = db.Column(db.String(500))
    observaciones = db.Column(db.String(500))
    tratamientos = db.relationship('Tratamiento', backref='visita', lazy=True, cascade="all, delete-orphan")
    usuario = db.relationship('Usuario')

class Tratamiento(db.Model):
    __tablename__ = 'tratamientos'
    id_tratamiento = db.Column(db.Integer, primary_key=True)
    id_visita = db.Column(db.Integer, db.ForeignKey('visitas.id_visita'), nullable=False)
    medicamento = db.Column(db.String(150), nullable=False)
    dosis = db.Column(db.String(100))
    duracion = db.Column(db.String(100))
    indicaciones = db.Column(db.String(500))

class Producto(db.Model):
    __tablename__ = 'productos'
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.String(300))
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    categoria = db.Column(db.String(100))
    imagen_url = db.Column(db.String(255))
    stock = db.Column(db.Integer, default=0)
    activo = db.Column(db.Boolean, default=True)

class Cita(db.Model):
    __tablename__ = 'citas'
    id_cita = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id_paciente'), nullable=False)
    fecha_cita = db.Column(db.DateTime, nullable=False)
    motivo = db.Column(db.String(200))
    estado = db.Column(db.String(50), default='Pendiente')
