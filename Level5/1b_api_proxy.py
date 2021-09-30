# Create a simple local web server with an API endpoint that proxies the TODOs API used above and accepts the
# "completed" and the "name" filtering. You can use any web framework you prefer.

import flask
from flask import request, jsonify
from urllib.request import urlopen
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True
API_URL = 'https://jsonplaceholder.typicode.com/todos/'


@app.route('/', methods=['GET'])
def home():
    link1 = "http://127.0.0.1:5000/api/v1/resources/todos?completed=False&name=harry"
    link2 = "http://127.0.0.1:5000/api/v1/resources/todos?completed=True"
    alink1 = '<a href="' + link1 + '" target="_blank">Filtering by completed and name</a>'
    alink2 = '<a href="' + link2 + '" target="_blank">Filtering by completed</a>'
    return "<h1>Simple API Proxy</h1><p>This is a simple API Proxy  " + API_URL + ".</p><br>" + alink1 + "<br>" + alink2


@app.route('/api/v1/resources/todos/all', methods=['GET'])
def api_all():
    return jsonify(fetch_all())


@app.route('/api/v1/resources/todos', methods=['GET'])
def api_filter():
    results = []
    all_data = fetch_all()

    if 'completed' in request.args:
        completed = request.args['completed']
        completed_value = True if completed == 'True' else False
        results = data_filter(all_data, 'completed', completed_value)
    # field "name" does not exists in original json API response
    if 'name' in request.args:
        name = request.args['name']
        # results = data_filter(all_data, 'name', name)

    return jsonify(results)


def fetch_all():
    url = 'https://jsonplaceholder.typicode.com/todos/'
    response = urlopen(url)
    data = json.loads(response.read())
    return data


def data_filter(data, field, value):
    json_str = json.dumps(data)
    data_dict = json.loads(json_str)
    filtered_dict = [x for x in data_dict if x[field] == value]
    return list(filtered_dict)


app.run()
# test: http://127.0.0.1:5000/api/v1/resources/todos?completed=False&name=harry
# test: http://127.0.0.1:5000/api/v1/resources/todos?completed=True
