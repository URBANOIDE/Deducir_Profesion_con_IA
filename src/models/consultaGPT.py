import openai
from src.config.config import OPENAI_API_KEY
#from src.controllers.home import index

# Configura tus credenciales de API
openai.api_key = OPENAI_API_KEY

class ConsultasModel():
    def OpenAI(self, gustos, pasiones, habilidades):
        pregunta = "De acuerdo a los siguientes gustos, pasiones y habilidades, decirme que profesion puedo estudiar, de ser necesario mostrar mas de una profesión: Gustos: " + gustos + ", Pasiones: " + pasiones + ", Habilidades: " + habilidades + "La respuesta debe empezar con 'Basado en tus gustos, pasiones y habilidades, la profesión que podrías estudiar es: '"
    
        respuesta = openai.Completion.create(
            engine='text-davinci-002',
            prompt=pregunta,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        res = respuesta.choices[0].text.strip()

        return res