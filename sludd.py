from flask import Flask
import json
import requests

app = Flask(__name__)

base_url = 'https://wttr.in/sandvika?format=j1'

@app.get('/<string:sted>')
def rute_index(sted):
    res = requests.get(f'https://wttr.in/{sted}?format=j1')
    data = res.json()
    akkurat_naa = data['current_condition'][0]['temp_C']
    return f'<h1>{akkurat_naa}</h1>'

app.run(port=5000, debug=True)

