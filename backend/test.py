import requests

url = 'http://localhost:5000/generate_history'

data = {
    'persons': 2,
    'target': 'adultos',
    'theme': 'amizade',
    'environment': 'escritório',
    'ending': 'seja inesperado'
}

response = requests.post(url, json=data)

print(response.json()['history'])
