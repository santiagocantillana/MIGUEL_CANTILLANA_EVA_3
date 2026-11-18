from flask import Flask, render_template, request

app = Flask(__name__)

@app.route ("/")
def index ():
    return render_template ('index.html')

@app.route ("/ejercicio1", methods=["GET", "POST"])
def boton1 ():
    promedio = None
    estado = None

    if request.method == "POST":
        nota1 = int(request.form["nota1"])
        nota2 = int(request.form["nota2"])
        nota3 = int(request.form["nota3"])
        asistencia = int(request.form["asistencia"])

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"
    return render_template ('ejercicio1.html', promedio=promedio, estado=estado)


@app.route ("/ejercicio2", methods=["GET", "POST"])
def boton2 ():
    nombre_mayor = None
    cantidad = None

    if request.method == "POST":
        nombre1 = request.form["nombre1"].strip()
        nombre2 = request.form["nombre2"].strip()
        nombre3 = request.form["nombre3"].strip()

        nombre_mayor = max(nombre1, nombre2, nombre3, key=len)
        cantidad = len(nombre_mayor)
    return render_template ('ejercicio2.html', nombre_mayor=nombre_mayor, cantidad=cantidad)

if __name__ == '__main__':
    app.run (debug = True)