import requests

# Definieren der URL des Flask-Servers
url = 'http://localhost:8080/chat'  # Ersetzen Sie 'localhost:8080' durch Ihre tatsächliche URL

# Starten einer Endlosschleife für die Benutzereingabe
while True:
    # Benutzereingabe abfragen
    user_input = input("Geben Sie einen Satz ein (oder 'exit' zum Beenden): ")

    # Überprüfen, ob der Benutzer das Programm beenden möchte
    if user_input.lower() == 'exit':
        break

    # Definieren der Daten für die Anfrage
    data = {
        'thread_id': 'thread_PLGeY7s7ItgrGkvVDPzUXFZR',
        'message': user_input
    }

    # Senden der POST-Anfrage an den /chat-Endpunkt
    response = requests.post(url, json=data)

    # Überprüfen, ob die Anfrage erfolgreich war
    response.raise_for_status()

    # Ausgabe der erhaltenen Daten
    print("Antwort vom Assistenten:", response.json().get('response', 'Keine Antwort verfügbar'))

# Ende des Skripts
