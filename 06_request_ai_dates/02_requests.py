# Cómo hacer peticiones a APIs con Python
# con y sin dependencias

# Limpiar la terminal
import subprocess
_ = subprocess.run(["clear"], check=False)

# 1. Sin dependencias
import urllib.request
import urllib.error
import json

api_posts = "https://jsonplaceholder.typicode.com/posts"

try:
  response = urllib.request.urlopen(api_posts)
  data = response.read()
  json_data = json.loads(data.decode("utf-8"))
  # print(f"Posts data: {json.dumps(json_data, indent=2)}")
  response.close()
except urllib.error.URLError as e:
  print(f"Error: {e}")

# 2. Con dependencia (requests)
# Instalamos UV con brew install uv
# uv venv -> para crear el entorno virtual
# source .venv/bin/activate -> para activar el entorno virtual
# uv pip install requests -> para instalar la dependencia
import requests

print("\nGET:")
response = requests.get(api_posts)
# json.dumps para convertir el JSON a un string legible
# ensure_ascii=False para que no se convierta a ASCII
# indent=2 para que el JSON se imprima con indentación
# [:10] para que se imprima solo los primeros 5 elementos
print(json.dumps(response.json()[:5], indent=2, ensure_ascii=False))

print("\nPOST:")
input = {
  "title": "Test Post",
  "body": "This is a test post",
  "userId": 1
}
try:
  response = requests.post(api_posts, json=input)
  print(json.dumps(response.json(), indent=2, ensure_ascii=False))
except requests.exceptions.RequestException as e:
  print(f"Error: {e}")

print("\nPUT:")
input = {
  "title": "Test Post",
  "body": "This is a test post",
  "userId": 1,
}
try:
  response = requests.put(f"{api_posts}/1", json=input)
  print(json.dumps(response.json(), indent=2, ensure_ascii=False))
except requests.exceptions.RequestException as e:
  print(f"Error: {e}")

# Utilizar la API de OpenAI
OPENAI_KEY = "sk-XXXXX"

def call_openai_gpt(api_key: str, prompt: str):
  url = "https://api.openai.com/v1/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "user",
        "content": prompt
      }
    ]
  }
  response = requests.post(url, headers=headers, json=data)
  return response.json()

api_response = call_openai_gpt(OPENAI_KEY, "¿Qué es la IA?")
print(json.dumps(api_response["choices"][0]["message"]["content"], indent=2, ensure_ascii=False))