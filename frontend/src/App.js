 import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [chain, setChain] = useState([]);
  const [sender, setSender] = useState('');
  const [receiver, setReceiver] = useState('');
  const [amount, setAmount] = useState('');

  // Récupère la blockchain depuis le backend
  useEffect(() => {
    axios.get('/chain')
      .then(res => setChain(res.data.chain))
      .catch(err => console.error(err));
  }, []);

  // Envoie une transaction
  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/transactions/new', { sender, receiver, amount })
      .then(() => {
        alert('Transaction envoyée !');
        setSender('');
        setReceiver('');
        setAmount('');
      })
      .catch(err => console.error(err));
  };

  return (
    <div className="App">
      <h1>Mini Blockchain Explorer</h1>
      
      {/* Formulaire de transaction */}
      <form onSubmit={handleSubmit} className="transaction-form">
        <input
          type="text"
          placeholder="Expéditeur"
          value={sender}
          onChange={(e) => setSender(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Destinataire"
          value={receiver}
          onChange={(e) => setReceiver(e.target.value)}
          required
        />
        <input
          type="number"
          placeholder="Montant"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          required
        />
        <button type="submit">Envoyer</button>
      </form>

      {/* Affichage de la blockchain */}
      <div className="blockchain">
        {chain.map((block) => (
          <div key={block.index} className="block">
            <h3>Bloc #{block.index}</h3>
            <p><strong>Hash :</strong> {block.hash.substring(0, 20)}...</p>
            <p><strong>Transactions :</strong> {block.transactions.length}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
