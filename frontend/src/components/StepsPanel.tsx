import { useState } from 'react'

export function StepsPanel({ steps }: { steps: string }) {
  const [open, setOpen] = useState(false)
  if (!steps) return null
  return (
    <div className="steps-panel">
      <button className="steps-toggle" onClick={() => setOpen(o => !o)}>
        {open ? '🔼 Esconder passo a passo' : '📋 Ver passo a passo'}
      </button>
      {open && (
        <div className="steps-box">
          <div className="steps-header">🔬 Como chegamos lá:</div>
          <pre>{steps}</pre>
        </div>
      )}
    </div>
  )
}
