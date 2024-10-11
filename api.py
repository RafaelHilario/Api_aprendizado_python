from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

users = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30},
    3: {"name": "Charlie", "age": 35}
}

@app.route('/')
def home():
    return jsonify({"message": "Bem-vindo à API!"})

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Usuário não encontrado"}), 404

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/user', methods=['POST'])
def create_user():
    new_user = request.json
    if "name" in new_user and "age" in new_user:
        # Atribuir um novo ID automaticamente
        new_id = max(users.keys()) + 1
        users[new_id] = new_user
        return jsonify({"message": "Usuário criado com sucesso", "user": new_user}), 201
    else:
        return jsonify({"error": "Dados inválidos"}), 400

# Função para fazer requisição POST para criar um usuário novo
def create_user_request(name, age):
    url = 'http://localhost:5000/user'
    new_user = {"name": name, "age": age}
    response = requests.post(url, json=new_user)

    if response.status_code == 201:
        print("Usuário criado com sucesso:", response.json())
    else:
        print("Erro ao criar o usuário:", response.status_code, response.json())

if __name__ == '__main__':
    app.run(debug=True)
