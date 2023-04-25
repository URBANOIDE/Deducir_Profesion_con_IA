import openai

# Configura tus credenciales de API
openai.api_key = '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'

def hacer_pregunta(pregunta):
    # Llamada a la API para hacer la pregunta
    respuesta = openai.Completion.create(
        engine='text-davinci-002',
        prompt=pregunta,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return respuesta.choices[0].text.strip()

# Obtener la pregunta del usuario
pregunta = input("Haz una pregunta: ")

# Hacer la pregunta a ChatGPT y obtener la respuesta
respuesta = hacer_pregunta(pregunta)

# Mostrar la respuesta de ChatGPT
print("Respuesta de ChatGPT:", respuesta)