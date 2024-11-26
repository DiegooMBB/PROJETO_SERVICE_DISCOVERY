from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/consume', methods=['GET'])
def consume_service():
    # Consulta o Consul para encontrar o endereço de Service B
    consul_url = "http://localhost:8500/v1/catalog/service/service-b"
    response = requests.get(consul_url).json()
    service_b = response[0]
    service_b_address = f"http://{service_b['ServiceAddress']}:{service_b['ServicePort']}/message"

    # Faz requisição ao Service B
    service_b_response = requests.get(service_b_address).json()
    return jsonify({"service_b_response": service_b_response})

if __name__ == '__main__':
    # Registra o serviço no Consul
    consul_url = "http://localhost:8500/v1/agent/service/register"
    service_definition = {
        "Name": "service-a",
        "ID": "service-a-1",
        "Address": "localhost",
        "Port": 5000
    }
    requests.put(consul_url, json=service_definition)
    app.run(port=5000)
