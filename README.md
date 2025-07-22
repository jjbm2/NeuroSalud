NeuroSalud - Sistema de Recomendación de Salud

Sistema web básico para recomendaciones de salud basado en síntomas ingresados por el usuario, con autenticación mediante login.  
El objetivo es brindar sugerencias sencillas y recordar siempre que no sustituyen la consulta médica.

Características

- Registro e inicio de sesión de usuarios (con SQLite).
- Formulario para ingresar temperatura, tos y otros síntomas.
- Motor simple de recomendaciones basado en reglas.
- Mensaje claro de advertencia para acudir al médico.
- Interfaz profesional y amigable, diseño adaptado a la identidad NeuroSalud.
- Backend con Flask (Python).

Tecnologías

- Python 3
- Flask
- SQLite (base de datos ligera)
- HTML5, CSS3 (estilos profesionales)
  
Instalación

1. Clonar repositorio:
bash
git clone https://github.com/tuusuario/neurosalud.git
cd neurosalud

2.Crear y activar entorno virtual (opcional pero recomendado):
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

3.Instalar dependencias:
pip install flask

4.Ejecutar aplicación:
python app.py

5.Abrir navegador en:
http://127.0.0.1:5000

6.Uso

- Regístrate con un usuario y contraseña.
- Inicia sesión.
- Completa el formulario con tus datos de salud.
- Recibe recomendaciones personalizadas.
- Recuerda que esto NO reemplaza atención médica profesional.

Estructura del proyecto

salud_app/

├── app.py

├── templates/

│   ├── login.html

│   ├── register.html

│   ├── home.html

│   └── result.html

└── static/

  └── style.css
    
Licencia

Proyecto creado para fines educativos y presentación de hackathon.
No se ofrece garantía médica ni responsabilidad por el uso del sistema.

Autor

Bernal Muñoz Jose de Jesus

Sebastián Badillo Romo

Contacto

Puedes contactarme para dudas o sugerencias vía correo
