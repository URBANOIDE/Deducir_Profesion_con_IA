from flask import redirect, render_template, request, url_for, flash
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
        flash("Se ha producido un error, porfavor intente más tarde.")
        return redirect(url_for('index'))

    #return render_template('respuesta.html', res = res)


    return render_template('respuesta.html', res = res)