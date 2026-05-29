import type { Matrix } from '../types'

function fmt(v: number): string {
  if (Number.isInteger(v)) return String(v)
  return parseFloat(v.toFixed(4)).toString()
}

export function MatrixDisplay({ matrix }: { matrix: Matrix }) {
  return (
    <div className="res-matrix">
      <table>
        <tbody>
          {matrix.map((row, r) => (
            <tr key={r}>
              {row.map((v, c) => (
                <td key={c}>{fmt(v)}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
