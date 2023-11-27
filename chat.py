import requests

# Definieren der URL des Flask-Servers
url = 'http://localhost:8080/chat'  # Ersetzen Sie 'localhost:8080' durch Ihre tatsächliche URL

# Definieren der Daten für die Anfrage
data = {
    'thread_id': 'thread_yWtod8uwsrOKgaoFBndddADW',
    'message': 'How much is your solar system?'
}

# Senden der POST-Anfrage an den /chat-Endpunkt
response = requests.post(url, json=data)

# Ausgabe der erhaltenen Daten
print(response.json())
