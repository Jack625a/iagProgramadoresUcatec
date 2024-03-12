import openai

openai.api_key=""

prompt="Caballo en la luna estilo cyberpunk"

response=openai.Image.create(
    prompt=prompt,
    n=3,
    size="1024x1024"
)

image_url=response['data'][0]['url']

print(image_url)