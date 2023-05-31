from flask import Flask, request, render_template

app = Flask(__name__)


# Vista raíz
@app.route('/')
def index():
    return render_template('index.html')


# Vista para sumar dos números recibidos por formulario
@app.route('/sumar', methods=['GET'])
def sumar_formulario():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    suma = num1 + num2
    return f"La suma de {num1} y {num2} es: {suma}"


# Vista para sumar dos números recibidos por URL
@app.route('/sumar/<int:num1>/<int:num2>')
def sumar_url(num1, num2):
    suma = num1 + num2
    return f"La suma de {num1} y {num2} es: {suma}"


# Vista para construir usuario por formulario
@app.route('/usuario', methods=['GET'])
def construir_usuario_formulario():
    nombre = request.args.get('nombre')
    apellido = request.args.get('apellido')
    usuario = nombre[0].lower() + apellido.lower()
    return usuario


# Vista para construir usuario por URL
@app.route('/usuario/<string:nombre>/<string:apellido>')
def construir_usuario_url(nombre, apellido):
    usuario = nombre[0].lower() + apellido.lower()
    return usuario


# Lista ficticia de usuarios
usuarios = ['Maria', 'Juan', 'Pedro', 'Ana', 'Manuel']


# Vista búsqueda de usuario por formulario
@app.route('/buscar_usuario', methods=['GET'])
def buscar_usuario_formulario():
    texto = request.args.get('texto')
    usuarios_coincidentes = [usuario for usuario in usuarios if texto.lower() in usuario.lower()]
    return "Se encontraron " + len(
        usuarios_coincidentes).__str__() + " usuarios que coinciden con la búsqueda: " + texto + \
        " --> " + usuarios.__str__()


# Vista búsqueda de usuario por URL
@app.route('/buscar_usuario')
def buscar_usuario_url():
    texto = request.args.get('texto', '')  # Obtener el parámetro 'texto' de la URL
    usuarios_coincidentes = [usuario for usuario in usuarios if texto.lower() in usuario.lower()]
    return "Se encontraron " + len(
        usuarios_coincidentes).__str__() + " usuarios que coinciden con la búsqueda: " + texto + \
        " --> " + usuarios.__str__()


if __name__ == '__main__':
    app.run(debug=True)
