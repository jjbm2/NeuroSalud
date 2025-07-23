from flask import Flask, render_template, request, redirect, session, flash, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = 'secreto'


def init_db():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS usuarios (usuario TEXT PRIMARY KEY, password TEXT)")
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        conn = sqlite3.connect('usuarios.db')
        c = conn.cursor()
        c.execute("SELECT * FROM usuarios WHERE usuario=? AND password=?", (usuario, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['usuario'] = usuario
            session['icp'] = False
            return redirect('/home')
        else:
            flash("Credenciales incorrectas")
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        conn = sqlite3.connect('usuarios.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO usuarios (usuario, password) VALUES (?, ?)", (usuario, password))
            conn.commit()
            conn.close()
            flash("Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect('/login')
        except:
            flash("El usuario ya existe")
    return render_template('register.html')


@app.route('/login_icp', methods=['POST'])
def login_icp():
    data = request.get_json()
    principal = data.get('principal')
    if not principal:
        return jsonify({"error": "Principal ICP no proporcionado"}), 400

    session['usuario'] = principal
    session['icp'] = True
    return jsonify({"message": "Autenticado con éxito"}), 200


@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'usuario' not in session:
        return redirect('/login')

    usuario = session['usuario']
    icp_user = session.get('icp', False)

    if request.method == 'POST':
        temperatura = float(request.form['temperatura'])
        tos = request.form.get('tos') == 'si'
        sintomas = request.form['sintomas'].lower()
        recomendaciones = []

        if temperatura >= 38:
            recomendaciones.append("Tomar paracetamol y mantenerse hidratado.")
        if temperatura >= 39:
            recomendaciones.append("Consultar a un médico por fiebre alta.")
        if tos:
            recomendaciones.append("Tomar jarabe para la tos y mantenerse abrigado.")
        if "dolor de cabeza" in sintomas:
            recomendaciones.append("Tomar ibuprofeno o paracetamol.")
        if "dolor de garganta" in sintomas:
            recomendaciones.append("Hacer gárgaras con agua tibia con sal y tomar té.")
        if "congestión nasal" in sintomas or "nariz tapada" in sintomas:
            recomendaciones.append("Usar descongestionante nasal y vaporizaciones.")
        if "diarrea" in sintomas:
            recomendaciones.append("Tomar suero oral y evitar comidas irritantes.")
        if "náusea" in sintomas or "vómito" in sintomas:
            recomendaciones.append("Mantenerse hidratado y comer alimentos suaves.")
        if "dolor muscular" in sintomas or "cuerpo cortado" in sintomas:
            recomendaciones.append("Descansar y tomar analgésicos como paracetamol.")
        if not recomendaciones:
            recomendaciones.append("Descansar y observar los síntomas.")

        return render_template('result.html', recomendaciones=recomendaciones)

    return render_template('home.html', usuario=usuario, icp=icp_user)


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    session.pop('icp', None)
    return redirect('/login')


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
