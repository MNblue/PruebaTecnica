import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import DeviceView from './views/DeviceView'
import IndustryView from './views/IndustryView'
import WharehouseView from './views/WharehouseView'


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    
    <DeviceView/>
    <IndustryView/>
    <WharehouseView/>
  </React.StrictMode>,
)
