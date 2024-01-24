
from flask import Flask, render_template, request

app = Flask(__name__)

# Definición de página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Desarrollo Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = None
    edad = 0
    tarros = 0
    total = 0
    total_final = 0
    valorTarro = 9000
    dscto = 0
    mostrarResultado = False
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        total = tarros * valorTarro

        if edad < 18:
            dscto = 0 # No tiene descuento
        elif edad >= 18 and edad <= 30:
            dscto = total * 0.15 # Descuento del 15%
        else:
            dscto = total * 0.25 # Descuento del 25%

        total_final = total - dscto
        mostrarResultado = True
    return render_template('ejercicio1.html', nombre=nombre, total=total, dscto=dscto, total_final=total_final, mostrarResultado=mostrarResultado)

# Desarrollo Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    # diccionario con los datos de los usuarios
    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }
    nombre = None
    mensaje = None
    mostrarResultado = False

    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['pass']

        if nombre in usuarios and usuarios[nombre] == contrasena:
            mostrarResultado = True
            if usuarios[nombre] == "admin":
                mensaje = "Bienvenido Administrador " + nombre
            else:
                mensaje = "Bienvenido Usuario " + nombre
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', nombre=nombre, mensaje=mensaje, mostrarResultado=mostrarResultado)

if __name__ == '__main__':
    app.run(debug=True)