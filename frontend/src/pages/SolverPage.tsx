import { useState, useEffect } from 'react'
import { MatrixGrid } from '../components/MatrixGrid'
import { StepsPanel } from '../components/StepsPanel'
import { api } from '../api'
import { type Matrix, type Vector, type ApiResult, makeMatrix, makeVector } from '../types'

const SIZES = [2, 3, 4]

function fmt(v: number): string {
  if (Number.isInteger(v)) return String(v)
  return parseFloat(v.toFixed(6)).toString()
}

export function SolverPage() {
  const [n,       setN]       = useState(2)
  const [matA,    setMatA]    = useState<Matrix>(makeMatrix(2, 2))
  const [vecB,    setVecB]    = useState<Vector>(makeVector(2))
  const [loading, setLoading] = useState(false)
  const [result,  setResult]  = useState<ApiResult<Vector> | null>(null)

  useEffect(() => {
    setMatA(makeMatrix(n, n))
    setVecB(makeVector(n))
    setResult(null)
  }, [n])

  const handleVecChange = (values: Matrix) => {
    setVecB(values.map(row => row[0]))
  }

  const solve = async () => {
    setLoading(true)
    setResult(null)
    try {
      const res = await api.solve(matA, vecB)
      setResult(res)
    } catch (e) {
      setResult({ ok: false, error: String(e) })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page">
      <div className="card">
        <div className="section-title">🎯 Resolver Sistema Linear (Ax = b)</div>
        <p style={{color:'#374151', marginBottom:'16px', lineHeight:'1.6'}}>
          Digite os coeficientes das equações (matriz A) e os resultados (vetor b).
          Vamos descobrir os valores de x₁, x₂, ... usando a Eliminação de Gauss!
        </p>

        <div className="section-title" style={{fontSize:'1.1rem'}}>
          <span className="badge">1</span> Número de variáveis:
        </div>
        <div className="size-row" style={{marginBottom:'20px'}}>
          {SIZES.map(s => (
            <button
              key={s}
              className={`size-btn${n === s ? ' active' : ''}`}
              onClick={() => setN(s)}
            >
              {s} variáveis
            </button>
          ))}
        </div>

        <div className="section-title" style={{fontSize:'1.1rem'}}>
          <span className="badge">2</span> Digite os números:
        </div>
        <div className="matrices-row">
          <div className="matrix-block">
            <h4>Matriz A (coeficientes)</h4>
            <MatrixGrid key={`a-${n}`} rows={n} cols={n} values={matA} onChange={setMatA} />
          </div>
          <div className="matrix-block orange">
            <h4 style={{color:'var(--orange)'}}>Vetor b (resultados)</h4>
            <MatrixGrid
              key={`b-${n}`}
              rows={n}
              cols={1}
              values={vecB.map(v => [v])}
              onChange={handleVecChange}
              theme="orange"
            />
          </div>
        </div>

        <button className="solve-btn" onClick={solve} disabled={loading}>
          🎯 Resolver!
        </button>
      </div>

      {loading && (
        <div className="loading">
          <div className="spinner" />
          <p>Resolvendo...</p>
        </div>
      )}

      {result && !loading && (
        <div className="card">
          {result.ok ? (
            <>
              <div className="result-banner">
                <span className="banner-icon">🏆</span>
                <div>
                  <div className="banner-title">Sistema resolvido!</div>
                  <div className="banner-sub">Encontramos os valores de todas as variáveis usando Eliminação de Gauss.</div>
                </div>
              </div>

              <div className="solution-list">
                {(result.result as Vector).map((val, i) => (
                  <div className="sol-item" key={i}>
                    <span className="sol-var">x{i + 1}</span>
                    <span className="sol-eq">=</span>
                    <span className="sol-val">{fmt(val)}</span>
                  </div>
                ))}
              </div>

              <div style={{marginTop:'16px'}}>
                <StepsPanel steps={result.steps ?? ''} />
              </div>
            </>
          ) : (
            <div className="error-banner">
              <span className="banner-icon">😕</span>
              <div>
                <div className="banner-title">Ops! Algo deu errado</div>
                <div className="banner-sub">{result.error}</div>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  )
}
