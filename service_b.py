from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Hello from Service B!"})

if __name__ == '__main__':
    # Registra o serviço no Consul
    consul_url = "http://localhost:8500/v1/agent/service/register"
    service_definition = {
        "Name": "service-b",
        "ID": "service-b-1",
        "Address": "localhost",
        "Port": 5001
    }
    requests.put(consul_url, json=service_definition)
    app.run(port=5001)
