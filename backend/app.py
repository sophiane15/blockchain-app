from flask import Flask, jsonify, request
from flask_cors import CORS
from blockchain import Blockchain
from waitress import serve
import os

# Initialisation de l'application Flask
app = Flask(__name__)
CORS(app)  # Active CORS pour toutes les routes

# Initialisation de la blockchain
blockchain = Blockchain()

# Route pour obtenir la blockchain complète
@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify({
        'chain': [block.__dict__ for block in blockchain.chain],
        'length': len(blockchain.chain)
    })

# Route pour ajouter une nouvelle transaction
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    data = request.get_json()
    
    # Vérification des champs obligatoires
    required_fields = ['sender', 'receiver', 'amount']
    if not all(field in data for field in required_fields):
        return 'Champs manquants', 400
    
    # Ajout de la transaction
    blockchain.add_transaction(data['sender'], data['receiver'], data['amount'])
    return 'Transaction ajoutée avec succès', 201

# Route pour miner un nouveau bloc
@app.route('/mine', methods=['GET'])
def mine():
    # Mine le bloc avec les transactions en attente
    blockchain.mine_pending_transactions()
    response = {
        'message': 'Nouveau bloc miné',
        'block': blockchain.chain[-1].__dict__
    }
    return jsonify(response), 200

# Configuration du serveur de production
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Port par défaut ou celui de Render
    serve(app, host="0.0.0.0", port=port)  # Utilisation de Waitress comme serveur WSGI
