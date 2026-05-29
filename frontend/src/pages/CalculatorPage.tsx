import { useState, useEffect } from 'react'
import { MatrixGrid } from '../components/MatrixGrid'
import { MatrixDisplay } from '../components/MatrixDisplay'
import { StepsPanel } from '../components/StepsPanel'
import { api } from '../api'
import {
  type Operation,
  type Matrix,
  type ApiResult,
  makeMatrix,
  BINARY_OPS,
  OP_LABELS,
} from '../types'

const OPS: { id: Operation; icon: string; sub: string }[] = [
  { id: 'add', icon: '➕', sub: 'A + B' },
  { id: 'sub', icon: '➖', sub: 'A − B' },
  { id: 'mul', icon: '✖️', sub: 'A × B' },
  { id: 'tra', icon: '↕️', sub: 'Aᵀ' },
  { id: 'det', icon: '🔢', sub: 'det(A)' },
  { id: 'inv', icon: '🔄', sub: 'A⁻¹' },
]

const SIZES = [2, 3, 4]

export function CalculatorPage() {
  const [op,      setOp]      = useState<Operation>('add')
  const [sizeN,   setSizeN]   = useState(2)
  const [bCols,   setBCols]   = useState(2)
  const [matA,    setMatA]    = useState<Matrix>(makeMatrix(2, 2))
  const [matB,    setMatB]    = useState<Matrix>(makeMatrix(2, 2))
  const [loading, setLoading] = useState(false)
  const [result,  setResult]  = useState<ApiResult<Matrix | number> | null>(null)

  const isBinary = BINARY_OPS.includes(op)
  const isMultiply = op === 'mul'

  useEffect(() => {
    setMatA(makeMatrix(sizeN, sizeN))
    setMatB(makeMatrix(sizeN, isMultiply ? bCols : sizeN))
    setResult(null)
  }, [sizeN, bCols, op])

  const handleOp = (o: Operation) => {
    setOp(o)
    setResult(null)
  }

  const calculate = async () => {
    setLoading(true)
    setResult(null)
    try {
      const callApi = (): Promise<ApiResult<Matrix | number>> => {
        if (op === 'add') return api.add(matA, matB)
        if (op === 'sub') return api.subtract(matA, matB)
        if (op === 'mul') return api.multiply(matA, matB)
        if (op === 'tra') return api.transpose(matA)
        if (op === 'det') return api.determinant(matA)
        return api.inverse(matA)
      }
      setResult(await callApi())
    } catch (e) {
      setResult({ ok: false, error: String(e) })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page">
      {/* Step 1 – Operation */}
      <div className="card">
        <div className="section-title"><span className="badge">1</span> Escolha a operação:</div>
        <div className="ops-grid">
          {OPS.map(o => (
            <button
              key={o.id}
              className={`op-btn${op === o.id ? ' active' : ''}`}
              onClick={() => handleOp(o.id)}
            >
              <span className="op-icon">{o.icon}</span>
              {OP_LABELS[o.id]}<br />
              <small>{o.sub}</small>
            </button>
          ))}
        </div>
      </div>

      {/* Step 2 – Size */}
      <div className="card">
        <div className="section-title"><span className="badge">2</span> Tamanho da matriz:</div>
        <div className="size-row" style={{marginBottom: isMultiply ? '12px' : '0'}}>
          <label>Linhas / Colunas de A:</label>
          {SIZES.map(n => (
            <button
              key={n}
              className={`size-btn${sizeN === n ? ' active' : ''}`}
              onClick={() => setSizeN(n)}
            >
              {n}×{n}
            </button>
          ))}
        </div>

        {isMultiply && (
          <div className="size-row">
            <label>Colunas de B:</label>
            {SIZES.map(n => (
              <button
                key={n}
                className={`size-btn${bCols === n ? ' active' : ''}`}
                onClick={() => setBCols(n)}
              >
                {n} col.
              </button>
            ))}
          </div>
        )}
      </div>

      {/* Step 3 – Input */}
      <div className="card">
        <div className="section-title"><span className="badge">3</span> Digite os números:</div>
        <div className="matrices-row">
          <div className="matrix-block">
            <h4>Matriz A</h4>
            <MatrixGrid
              key={`a-${sizeN}-${op}`}
              rows={sizeN}
              cols={sizeN}
              values={matA}
              onChange={setMatA}
            />
          </div>
          {isBinary && (
            <div className="matrix-block">
              <h4>Matriz B</h4>
              <MatrixGrid
                key={`b-${sizeN}-${bCols}-${op}`}
                rows={sizeN}
                cols={isMultiply ? bCols : sizeN}
                values={matB}
                onChange={setMatB}
              />
            </div>
          )}
        </div>
        <button className="calc-btn" onClick={calculate} disabled={loading}>
          🚀 Calcular!
        </button>
      </div>

      {/* Loading */}
      {loading && (
        <div className="loading">
          <div className="spinner" />
          <p>Calculando...</p>
        </div>
      )}

      {/* Result */}
      {result && !loading && (
        <div className="card">
          {result.ok ? (
            <>
              <div className="result-banner">
                <span className="banner-icon">🎉</span>
                <div>
                  <div className="banner-title">Resultado da {OP_LABELS[op]}!</div>
                  <div className="banner-sub">Veja abaixo. Clique em "Ver passo a passo" para entender como chegamos lá!</div>
                </div>
              </div>

              <div className="result-wrap">
                <h4>Resultado — {OP_LABELS[op]}</h4>
                {op === 'det' ? (
                  <>
                    <span className="scalar-result">det(A) = {Number.isInteger(result.result) ? result.result : parseFloat((result.result as number).toFixed(6))}</span>
                    <p className="det-note">
                      {Math.abs(result.result as number) < 1e-9
                        ? '❌ det = 0 → a matriz é SINGULAR (não tem inversa)'
                        : '✅ det ≠ 0 → a matriz é INVERTÍVEL (tem inversa!)'}
                    </p>
                  </>
                ) : (
                  <MatrixDisplay matrix={result.result as Matrix} />
                )}
              </div>

              <StepsPanel steps={result.steps ?? ''} />
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
