#Chat bot simple 
import openai

openai.api_key=""


def chatbot(message):
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role":"user",
                "content":message
            }
        ]
    )
    respuesta=response.choices[0].message.content
    return  respuesta

print("Bienvenido al Modelo GPT 3.5")
print("Realiza tu consulta")
pregunta=input(">: ")
resultado=chatbot(pregunta)
print("\nRespuesta: ", resultado)


