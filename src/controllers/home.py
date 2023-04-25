from flask import render_template, request
from src import app
from src.models.consultaGPT import ConsultasModel


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/respuesta', methods =['GET', 'POST'])
def respuesta():
    gustos = request.form.get('gustos')
    pasiones = request.form.get('pasiones')
    habilidades = request.form.get('habilidades')

    #consultasModel = ConsultasModel()
    #res = consultasModel.OpenAI(gustos, pasiones, habilidades)

    consultasModel = ConsultasModel()
    try:
        res = consultasModel.OpenAI(gustos, pasiones, habilidades)
    except Exception as e:
        # Manejar el error aquí, puedes imprimirlo, registrarlo en un archivo de registro, o mostrar un mensaje de error al usuario.
        res = 'Error: {}'.format(str(e))

    #return render_template('respuesta.html', res = res)


    return render_template('respuesta.html', res = res)