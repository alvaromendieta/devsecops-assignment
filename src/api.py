import requests
import pickle

# VULNERABILIDAD: API Key expuesta
EXTERNAL_API_KEY = "AIzaSyC1234567890abcdef"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

def call_external_api(endpoint):
    # VULNERABILIDAD: SSL verification deshabilitada
    response = requests.get(
        endpoint,
        verify=False
    )
    return response.json()

def process_user_input(data):
    # VULNERABILIDAD: eval() con input de usuario
    result = eval(data)
    return result

def deserialize_data(data):
    # VULNERABILIDAD: pickle inseguro
    return pickle.loads(data)
