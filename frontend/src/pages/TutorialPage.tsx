import { useState } from 'react'

type Topic = 'what' | 'tipos' | 'soma' | 'mult' | 'det' | 'inv' | 'linear'

interface Chip {
  id: Topic
  label: string
}

const CHIPS: Chip[] = [
  { id: 'what',   label: '🤔 O que é?' },
  { id: 'tipos',  label: '📊 Tipos' },
  { id: 'soma',   label: '➕➖ Soma/Subtr.' },
  { id: 'mult',   label: '✖️ Multiplicação' },
  { id: 'det',    label: '🔢 Determinante' },
  { id: 'inv',    label: '🔄 Inversa' },
  { id: 'linear', label: '🎯 Sist. Linear' },
]

function VisMatrix({ data, highlight }: { data: (string|number)[][], highlight?: [number,number][] }) {
  const hl = new Set((highlight ?? []).map(([r,c]) => `${r}-${c}`))
  return (
    <div className="vis-matrix">
      <table>
        <tbody>
          {data.map((row, r) => (
            <tr key={r}>
              {row.map((v, c) => (
                <td key={c} className={hl.has(`${r}-${c}`) ? 'h' : ''}>{v}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export function TutorialPage() {
  const [topic, setTopic] = useState<Topic>('what')

  return (
    <div className="page">
      <div className="card">
        <div className="section-title">📚 Escolha um tema para aprender:</div>
        <div className="tut-chips">
          {CHIPS.map(ch => (
            <button
              key={ch.id}
              className={`tut-chip${topic === ch.id ? ' active' : ''}`}
              onClick={() => setTopic(ch.id)}
            >
              {ch.label}
            </button>
          ))}
        </div>

        <div className="tut-content">
          {topic === 'what' && (
            <>
              <h2>🤔 O que é uma Matriz?</h2>
              <p>
                Uma <strong>matriz</strong> é como uma tabela organizada de números,
                dispostos em <strong>linhas</strong> e <strong>colunas</strong>.
              </p>
              <p>
                Pense em uma tabela de notas da escola — cada linha é um aluno e cada
                coluna é uma matéria. Isso é uma matriz!
              </p>
              <div className="highlight-box">
                💡 A posição de cada número é identificada por: <strong>linha × coluna</strong>.
                Por exemplo, A[2][3] = o número na 2ª linha e 3ª coluna!
              </div>
              <p>Abaixo uma <strong>matriz 3×2</strong> (3 linhas, 2 colunas):</p>
              <VisMatrix data={[[5,8],[2,7],[4,1]]} highlight={[[0,0],[1,1]]} />
              <p style={{marginTop:'10px'}}>Os números em roxo estão na <strong>diagonal</strong> (linha = coluna).</p>
              <div className="info-box">
                📐 Dizemos que uma matriz tem <strong>ordem m×n</strong>, onde m = nº de linhas e n = nº de colunas.
              </div>
            </>
          )}

          {topic === 'tipos' && (
            <>
              <h2>📊 Tipos de Matrizes</h2>
              <ul>
                <li><strong>Matriz Quadrada</strong> — mesmo número de linhas e colunas (ex: 3×3).</li>
                <li style={{marginTop:'8px'}}><strong>Matriz Identidade (I)</strong> — diagonal toda com <strong>1</strong> e o resto <strong>0</strong>. É o "1" das matrizes!</li>
                <li style={{marginTop:'8px'}}><strong>Matriz Nula (0)</strong> — todos os elementos são <strong>zero</strong>.</li>
                <li style={{marginTop:'8px'}}><strong>Matriz Transposta (Aᵀ)</strong> — as linhas viram colunas e as colunas viram linhas!</li>
                <li style={{marginTop:'8px'}}><strong>Matriz Diagonal</strong> — só tem números fora de zero na diagonal principal.</li>
              </ul>
              <div className="highlight-box">
                Identidade 3×3:
                <div style={{marginTop:'8px'}}>
                  <VisMatrix data={[[1,0,0],[0,1,0],[0,0,1]]} highlight={[[0,0],[1,1],[2,2]]} />
                </div>
              </div>
            </>
          )}

          {topic === 'soma' && (
            <>
              <h2>➕➖ Soma e Subtração</h2>
              <p>Para somar (ou subtrair) matrizes, as duas precisam ter o <strong>mesmo tamanho</strong>.</p>
              <p>Simples: some (ou subtraia) os elementos que estão na <strong>mesma posição</strong>!</p>
              <div className="highlight-box">📐 Regra: C[i][j] = A[i][j] + B[i][j]</div>
              <p><strong>Exemplo — A + B:</strong></p>
              <div className="vis-wrap">
                <VisMatrix data={[[1,2],[3,4]]} />
                <span className="op-symbol" style={{color:'var(--green)'}}>+</span>
                <VisMatrix data={[[5,6],[7,8]]} />
                <span className="op-symbol" style={{color:'var(--blue)'}}>= </span>
                <VisMatrix data={[[6,8],[10,12]]} highlight={[[0,0],[0,1],[1,0],[1,1]]} />
              </div>
              <div className="info-box" style={{marginTop:'14px'}}>
                ⚠️ Não é possível somar uma matriz 2×3 com uma 3×2! Elas precisam ser do <strong>mesmo tamanho</strong>.
              </div>
            </>
          )}

          {topic === 'mult' && (
            <>
              <h2>✖️ Multiplicação de Matrizes</h2>
              <p>A multiplicação é <strong>linha por coluna</strong> — não é elemento por elemento!</p>
              <div className="highlight-box">
                📐 Regra: C[i][j] = soma de A[i][k] × B[k][j]<br />
                Para multiplicar A×B, o nº de <strong>colunas de A</strong> deve ser igual ao nº de <strong>linhas de B</strong>.
              </div>
              <p><strong>Exemplo:</strong> Linha 1 de A × Coluna 1 de B = (1×5)+(2×7) = 5+14 = <strong>19</strong></p>
              <div className="vis-wrap">
                <VisMatrix data={[[1,2],[3,4]]} highlight={[[0,0],[0,1]]} />
                <span className="op-symbol" style={{color:'var(--orange)'}}>×</span>
                <VisMatrix data={[[5,6],[7,8]]} highlight={[[0,0],[1,0]]} />
                <span className="op-symbol" style={{color:'var(--blue)'}}>= </span>
                <VisMatrix data={[[19,22],[43,50]]} highlight={[[0,0]]} />
              </div>
              <div className="info-box" style={{marginTop:'14px'}}>
                🔄 Atenção! A×B ≠ B×A em geral. A multiplicação de matrizes <strong>não é comutativa!</strong>
              </div>
            </>
          )}

          {topic === 'det' && (
            <>
              <h2>🔢 Determinante</h2>
              <p>O <strong>determinante</strong> é um número especial calculado a partir de uma matriz <strong>quadrada</strong>.</p>
              <div className="highlight-box">
                🔑 det(A) ≠ 0 → a matriz tem <strong>inversa</strong> (é invertível)<br />
                ❌ det(A) = 0 → a matriz é <strong>singular</strong> (não tem inversa)
              </div>
              <p><strong>Fórmula para 2×2:</strong></p>
              <VisMatrix data={[['a','b'],['c','d']]} highlight={[[0,0],[1,1]]} />
              <p style={{marginTop:'8px',fontSize:'1.1rem'}}><strong>det = a×d − b×c</strong></p>
              <p style={{marginTop:'8px',color:'#6b7280'}}>
                Exemplo com [[3,2],[1,4]]: det = 3×4 − 2×1 = 12 − 2 = <strong>10</strong>
              </p>
              <div className="info-box">
                📐 Para 3×3 e maiores, usamos a <strong>Expansão de Cofatores</strong> — a calculadora faz isso automaticamente!
              </div>
            </>
          )}

          {topic === 'inv' && (
            <>
              <h2>🔄 Matriz Inversa</h2>
              <p>A <strong>inversa</strong> de uma matriz A, escrita como A⁻¹, é aquela que quando multiplicada por A dá a <strong>matriz identidade</strong>:</p>
              <div className="highlight-box" style={{textAlign:'center',fontSize:'1.1rem'}}>A × A⁻¹ = I</div>
              <p>É como a "divisão" das matrizes. Assim como 3 × (1/3) = 1, para matrizes temos A × A⁻¹ = I.</p>
              <ul style={{marginTop:'10px'}}>
                <li>Só existe para matrizes <strong>quadradas</strong></li>
                <li>Só existe se o <strong>determinante ≠ 0</strong></li>
                <li>Calculamos pelo método <strong>Gauss-Jordan</strong></li>
              </ul>
              <div className="info-box">
                🧮 A calculadora vai mostrar cada passo do método Gauss-Jordan! Dá pra acompanhar o raciocínio todo.
              </div>
            </>
          )}

          {topic === 'linear' && (
            <>
              <h2>🎯 Sistemas Lineares</h2>
              <p>Um <strong>sistema linear</strong> é um conjunto de equações que queremos resolver ao mesmo tempo!</p>
              <div className="highlight-box">
                2x + 3y = 8<br />
                x{'  '}+{'  '}y = 3
              </div>
              <p>Podemos escrever isso como <strong>Ax = b</strong>, onde:</p>
              <ul>
                <li><strong>A</strong> é a matriz de coeficientes</li>
                <li><strong>x</strong> é o vetor das incógnitas (o que queremos descobrir!)</li>
                <li><strong>b</strong> é o vetor dos termos independentes</li>
              </ul>
              <div className="vis-wrap" style={{marginTop:'12px'}}>
                <VisMatrix data={[[2,3],[1,1]]} />
                <span style={{fontWeight:900,fontSize:'1.1rem'}}>× [x, y] =</span>
                <VisMatrix data={[[8],[3]]} />
              </div>
              <div className="info-box" style={{marginTop:'14px'}}>
                🔬 Usamos a <strong>Eliminação de Gauss</strong> para resolver: isolamos cada variável passo a passo!
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  )
}
