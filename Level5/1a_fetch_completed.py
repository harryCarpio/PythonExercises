# 1.a https://jsonplaceholder.typicode.com/todos/ and then print all the completed TODOs in the screen.
import json
from urllib.request import urlopen


def fetch_all():
    url = 'https://jsonplaceholder.typicode.com/todos/'
    response = urlopen(url)
    return response.read().decode('utf-8')


def print_completed(data):
    data_dict = json.loads(data)
    filtered_dict = [x for x in data_dict if x['completed']]
    filtered_json = json.dumps(filtered_dict)
    print(filtered_json)


data_json = fetch_all()
print_completed(data_json)
