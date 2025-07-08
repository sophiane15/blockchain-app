from flask import Flask, jsonify, request
from flask_cors import CORS
from blockchain import Blockchain

app = Flask(__name__)
CORS(app)  # Autorise les requêtes depuis React
blockchain = Blockchain()

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    data = request.get_json()
    blockchain.add_transaction(data['sender'], data['receiver'], data['amount'])
    return "Transaction ajoutée", 201

@app.route('/chain', methods=['GET'])
def full_chain():
    return jsonify({
        "chain": [block.__dict__ for block in blockchain.chain],
        "length": len(blockchain.chain)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
