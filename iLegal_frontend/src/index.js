import React from 'react';
import ReactDOM from 'react-dom';

import './index.css';
import App from './views/App';
import registerServiceWorker from './registerServiceWorker';

window.SDK = require('./speech/Speech.Browser.Sdk.js');

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
