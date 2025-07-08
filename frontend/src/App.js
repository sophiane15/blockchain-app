import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [chain, setChain] = useState([]);

  useEffect(() => {
    fetch('https://votre-api-render.onrender.com/chain')
      .then(res => res.json())
      .then(data => setChain(data.chain));
  }, []);

  return (
    <div className="App">
      <h1>Mini Blockchain Explorer</h1>
      <div>
        {chain.map(block => (
          <div key={block.index} className="block">
            <p>Bloc #{block.index}</p>
            <p>Hash: {block.hash.substring(0, 15)}...</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
