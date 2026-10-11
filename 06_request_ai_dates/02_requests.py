# Cómo hacer peticiones a APIs con Python
# con y sin dependencias

# Limpiar la terminal
import subprocess
_ = subprocess.run(["clear"], check=False)

# 1. Sin dependencias
import urllib.request
import urllib.error
import json

api_posts = "https://jsonplaceholder.typicode.com/posts/"

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
# [:10] para que se imprima solo los primeros 10 elementos
print(json.dumps(response.json()[:10], indent=2, ensure_ascii=False))

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