import { useState } from 'react'
import type { Page } from './types'
import { HomePage } from './pages/HomePage'
import { TutorialPage } from './pages/TutorialPage'
import { CalculatorPage } from './pages/CalculatorPage'
import { SolverPage } from './pages/SolverPage'

const NAV_ITEMS: { id: Page; label: string }[] = [
  { id: 'home',     label: '🏠 Início' },
  { id: 'tutorial', label: '📚 Aprender' },
  { id: 'calc',     label: '🧮 Calculadora' },
  { id: 'solve',    label: '✏️ Sistemas' },
]

export default function App() {
  const [page, setPage] = useState<Page>('home')

  return (
    <>
      <header className="app-header">
        <h1>🎓 MatriX Fun!</h1>
        <p>O jeito mais divertido de aprender Matrizes</p>
      </header>

      <nav className="nav">
        {NAV_ITEMS.map(item => (
          <button
            key={item.id}
            className={`nav-btn${page === item.id ? ' active' : ''}`}
            onClick={() => setPage(item.id)}
          >
            {item.label}
          </button>
        ))}
      </nav>

      <main>
        {page === 'home'     && <HomePage setPage={setPage} />}
        {page === 'tutorial' && <TutorialPage />}
        {page === 'calc'     && <CalculatorPage />}
        {page === 'solve'    && <SolverPage />}
      </main>
    </>
  )
}
