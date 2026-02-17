# VetTrack - Sistema de Gestión Veterinaria 🐾

Sistema web moderno y profesional para la gestión integral de clínicas veterinarias. Permite administrar pacientes, citas, tratamientos, inventario y usuarios con una interfaz intuitiva y elegante.

![VetTrack Hero](https://images.unsplash.com/photo-1623387641168-d9803ddd3f35?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80)
_(Imagen representativa)_

## 🚀 Características Principales

- **Gestión de Pacientes (Mascotas)**: Registro completo con historial médico, visitas y tratamientos.
- **Control de Clientes**: Administración de dueños y vinculación con sus mascotas.
- **Agenda de Citas**: Sistema para programar y controlar el estado de las citas (Pendiente, Completada, Cancelada).
- **Inventario de Productos**: Control de stock, precios y categorías (Medicamentos, Alimentos, etc.).
- **Gestión de Usuarios**: Roles diferenciados (Admin/Empleado) para el control de acceso.
- **Dashboard Interactivo**: Vista general con estadísticas clave del negocio.
- **Diseño Responsive**: Interfaz adaptada a móviles y tablets con diseño moderno.

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3.14+, Flask
- **Base de Datos**: SQLite (SQLAlchemy ORM)
- **Frontend**: HTML5, CSS3 (Custom Styling + Bootstrap Grid), Jinja2
- **Iconos**: FontAwesome 6

## 📋 Requisitos Previos

- Python 3.8 o superior instalado en tu sistema.
- pip (gestor de paquetes de Python).

## ⚙️ Instalación y Configuración

1. **Clonar el repositorio (o descargar archivos):**

   ```bash
   git clone https://github.com/tu-usuario/vettrack.git
   cd vettrack
   ```

2. **Crear un entorno virtual (recomendado):**

   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate
   ```

3. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Inicializar la Base de Datos:**
   La base de datos se crea automáticamente al iniciar la aplicación por primera vez.

## ▶️ Ejecución

Para iniciar el servidor de desarrollo:

```bash
python run.py
```

Abre tu navegador y visita: `http://127.0.0.1:5000`

## 🔐 Credenciales de Acceso

El sistema crea un usuario administrador por defecto en el primer inicio:

- **Usuario**: `admin@vettrack.com`
- **Contraseña**: `admin123`

> ⚠️ **Nota**: Se recomienda cambiar la contraseña inmediatamente después del primer inicio de sesión o crear un nuevo usuario administrador.

## 📂 Estructura del Proyecto

```
VetTrack/
├── app/
│   ├── routes/          # Lógica de rutas (Controladores)
│   ├── static/          # Archivos estáticos (CSS, JS, Imágenes)
│   ├── templates/       # Plantillas HTML
│   ├── __init__.py      # Fábrica de la aplicación
│   └── models.py        # Modelos de Base de Datos
├── instance/            # Base de datos SQLite
├── run.py               # Punto de entrada
├── requirements.txt     # Dependencias
└── README.md            # Documentación
```

## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir qué te gustaría cambiar.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.
