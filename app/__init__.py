from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vettrack.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'your_super_secret_key_here'

    db.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

        # Auth Routes
        from .routes.auth import auth_bp
        app.register_blueprint(auth_bp)

        # Main Routes
        from .routes.main import main_bp
        app.register_blueprint(main_bp)

        # Client Routes
        from .routes.clientes import clientes_bp
        app.register_blueprint(clientes_bp)

        # Patient Routes
        from .routes.pacientes import pacientes_bp
        app.register_blueprint(pacientes_bp)
        
        # Citas Routes
        from .routes.citas import citas_bp
        app.register_blueprint(citas_bp)
        
        # Productos Routes
        from .routes.productos import productos_bp
        app.register_blueprint(productos_bp)
        
        # User Management Routes (Admin only)
        from .routes.usuarios import usuarios_bp
        app.register_blueprint(usuarios_bp)
        
        # Create default admin if neeeded
        from .models import Usuario
        if not Usuario.query.filter_by(correo='admin@vettrack.com').first():
            admin = Usuario(
                nombre='Admin',
                apellido='User',
                correo='admin@vettrack.com',
                rol='Admin'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()

    return app
