import type { Page } from '../types'

interface Props {
  setPage: (p: Page) => void
}

export function HomePage({ setPage }: Props) {
  return (
    <div className="page">
      <div className="welcome-box">
        <div className="bounce">🎉</div>
        <h2>Bem-vindo ao MatriX Fun!</h2>
        <p>
          Aqui você vai aprender o que são matrizes,<br />
          fazer cálculos incríveis e resolver equações como um(a) cientista!
        </p>
      </div>

      <div className="home-grid">
        <button className="home-tile tile-pink" onClick={() => setPage('tutorial')}>
          <span className="icon">📚</span>
          Aprender
          <div className="sub">Descubra o que são matrizes!</div>
        </button>
        <button className="home-tile tile-blue" onClick={() => setPage('calc')}>
          <span className="icon">🧮</span>
          Calculadora
          <div className="sub">Some, multiplique e muito mais!</div>
        </button>
        <button className="home-tile tile-green" onClick={() => setPage('solve')}>
          <span className="icon">✏️</span>
          Sistemas
          <div className="sub">Resolva equações juntas!</div>
        </button>
        <button className="home-tile tile-yellow" onClick={() => setPage('tutorial')}>
          <span className="icon">🎯</span>
          Dica do Dia
          <div className="sub">O que é um Sistema Linear?</div>
        </button>
      </div>

      <div className="card fact-card">
        <div className="section-title">💡 Você sabia?</div>
        <p>
          Matrizes são usadas em <strong>jogos de videogame</strong> para mover
          personagens, em <strong>inteligência artificial</strong> para reconhecer
          rostos, e até em <strong>filmes de animação</strong> para criar os efeitos
          especiais! Aprender matrizes é aprender a linguagem do futuro. 🚀
        </p>
      </div>
    </div>
  )
}
