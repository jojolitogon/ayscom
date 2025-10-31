import requests

response = requests.get("https://api.github.com/users/estelaromer")

if response.status_code == 200:
    data = response.json()
    print(data["login"], data["public_repos"])
else:
    print("Failed to fetch data:", response.status_code)


# API pública gratuita de GitHub (no requiere clave)
url = "https://api.github.com/users/octocat"

# Realizamos la solicitud GET
response = requests.get(url)

# Verificamos que la respuesta fue exitosa
if response.status_code == 200:
    data = response.json()  # convierte JSON → diccionario Python
    print("✅ Conexión correcta\n")

    # Mostramos algunos datos concretos
    print(f"Usuario: {data['login']}")
    print(f"ID: {data['id']}")
    print(f"Repos públicos: {data['public_repos']}")
    print(f"URL: {data['html_url']}")
else:
    print("❌ Error al obtener datos:", response.status_code)