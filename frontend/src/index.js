import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import 'bootstrap/dist/css/bootstrap.css'
import Example from './components/navbar';

ReactDOM.render(<Example />, document.getElementById('root'));
registerServiceWorker();
