// Importing modules
import React, { useState, useEffect } from 'react';
import ScriptForm from './components/ScriptForm';
import './App.css';
import logo from './logo.png';

function App() {
  return (
    <div className='App'>
      <header className='App-header'>
        <img
          style={{ marginTop: '15px', height: '150px', width: '500px' }}
          src={logo}
          alt='AI SPARC Flows'
        />
        <br />
        <h4 style={{ color: 'black' }}>
          Please first download and select files for analysis and prepare a local directory
          structured acording to instructions in our{' '}
          <a href='https://github.com/SPARC-FAIR-Codeathon/2023-team-6/blob/main/README.md'>
            readme
          </a>
          . The <a href='https://sparc.science/data?type=dataset'>SPARC website</a> is a great
          resource for exploring publically available datasets and downloading specific files for
          analysis.
        </h4>
        <br />
        <br />
        <ScriptForm />
      </header>
    </div>
  );
}

export default App;
