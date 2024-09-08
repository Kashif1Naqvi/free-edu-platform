import React from 'react'
import './App.css'
import { CounterProvider } from './contexts/CounterContext'
import CounterDisplay from './components/CounterDisplay'
import CounterControls from './components/CounterControls'

const App: React.FC = () => {
  return (
    <CounterProvider>
      <div>
        <CounterDisplay />
        <CounterControls />
      </div>
    </CounterProvider>
  )
}

export default App
