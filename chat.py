import requests

# Definieren der URL des Flask-Servers
url = 'http://localhost:8080/chat'  # Ersetzen Sie 'localhost:8080' durch Ihre tatsächliche URL

# Definieren der Daten für die Anfrage
data = {
    'thread_id': 'thread_PLGeY7s7ItgrGkvVDPzUXFZR',
    'message': 'Do we have a chicken with the name Hans?'
}

# Senden der POST-Anfrage an den /chat-Endpunkt
response = requests.post(url, json=data)

# Ausgabe der erhaltenen Daten
print(response.json())
