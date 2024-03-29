import json
from jsonschema import validate, ValidationError

def task1(path, age):
    with open(path, 'r') as file:
        data = json.load(file)

    names = [person['name'] for person in data if person['age'] > age]
    return names

def task2(data, path):
  dataJson = json.dumps(data)
  
  with open(path, 'w') as file:
    file.write(dataJson)

def task3(schema, paths):
    invalidFiles = []
    
    for path in paths:
        try:
            with open(path, 'r') as file:
                data = json.load(file)
                validate(instance=data, schema=schema)
        except ValidationError:
            invalidFiles.append(path)
        except Exception:
            invalidFiles.append(path)
    
    return invalidFiles

def task4(path, key):
    with open(path, 'r') as file:
        data = json.load(file)
    values = []

    def convert_data(data):
        if isinstance(data, dict):
            for k, v in data.items():
                if k == key:
                    values.append(v)
                else:
                    convert_data(v)
        elif isinstance(data, list):
            for item in data:
                convert_data(item)

    convert_data(data)
    return values

def task5(path, category, func):
    with open(path, 'r') as file:
        data = json.load(file)
        
    for item in data:
        if item['category'] == category:
            func(item)
            
    with open(path, 'w') as file:
        json.dump(data, file)