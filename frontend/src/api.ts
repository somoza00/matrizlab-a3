import type { Matrix, Vector, ApiResult } from './types'

async function post<T>(path: string, body: object): Promise<ApiResult<T>> {
  const res = await fetch(path, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  })
  if (!res.ok) throw new Error(`HTTP ${res.status}`)
  return res.json() as Promise<ApiResult<T>>
}

export const api = {
  add:         (A: Matrix, B: Matrix) => post<Matrix>('/api/add',        { A, B }),
  subtract:    (A: Matrix, B: Matrix) => post<Matrix>('/api/subtract',   { A, B }),
  multiply:    (A: Matrix, B: Matrix) => post<Matrix>('/api/multiply',   { A, B }),
  transpose:   (A: Matrix)            => post<Matrix>('/api/transpose',  { A }),
  determinant: (A: Matrix)            => post<number>('/api/determinant',{ A }),
  inverse:     (A: Matrix)            => post<Matrix>('/api/inverse',    { A }),
  solve:       (A: Matrix, b: Vector) => post<Vector>('/api/solve',      { A, b }),
}
