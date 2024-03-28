import json

def task1(path, age):
    with open(path, 'r') as file:
        data = json.load(file)

    names = [person['name'] for person in data if person['age'] > age]
    return names
  
task1('data.json', 30)

