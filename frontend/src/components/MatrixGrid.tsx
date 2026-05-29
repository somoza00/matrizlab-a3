import { useState } from 'react'
import type { Matrix } from '../types'

interface Props {
  rows: number
  cols: number
  values: Matrix
  onChange: (values: Matrix) => void
  theme?: 'purple' | 'orange'
}

export function MatrixGrid({ rows, cols, values, onChange, theme = 'purple' }: Props) {
  const [display, setDisplay] = useState<string[][]>(() =>
    values.map(row => row.map(v => String(v)))
  )

  const handleChange = (r: number, c: number, raw: string) => {
    // Allow partial inputs while typing: "", "-", "1.", "-1.", etc.
    if (raw !== '' && !/^-?\d*\.?\d*$/.test(raw)) return
    const nextDisp = display.map(row => [...row])
    nextDisp[r][c] = raw
    setDisplay(nextDisp)

    const num = parseFloat(raw)
    if (!isNaN(num)) {
      const nextNum = values.map(row => [...row])
      nextNum[r][c] = num
      onChange(nextNum)
    }
  }

  const handleBlur = (r: number, c: number) => {
    const raw = display[r]?.[c] ?? '0'
    const num = parseFloat(raw)
    const cleaned = isNaN(num) ? '0' : String(num)
    if (cleaned !== raw) {
      const nextDisp = display.map(row => [...row])
      nextDisp[r][c] = cleaned
      setDisplay(nextDisp)
      if (isNaN(num)) {
        const nextNum = values.map(row => [...row])
        nextNum[r][c] = 0
        onChange(nextNum)
      }
    }
  }

  return (
    <div
      className={`mat-grid${theme === 'orange' ? ' orange-theme' : ''}`}
      style={{ gridTemplateColumns: `repeat(${cols}, 1fr)` }}
    >
      {Array.from({ length: rows }, (_, r) =>
        Array.from({ length: cols }, (_, c) => (
          <input
            key={`${r}-${c}`}
            type="text"
            inputMode="decimal"
            value={display[r]?.[c] ?? '0'}
            onChange={e => handleChange(r, c, e.target.value)}
            onBlur={() => handleBlur(r, c)}
            onFocus={e => e.target.select()}
          />
        ))
      )}
    </div>
  )
}
