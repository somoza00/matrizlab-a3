export type Matrix = number[][]
export type Vector = number[]
export type Page = 'home' | 'tutorial' | 'calc' | 'solve'
export type Operation = 'add' | 'sub' | 'mul' | 'tra' | 'det' | 'inv'

export interface ApiResult<T = unknown> {
  ok: boolean
  result?: T
  error?: string
  steps?: string
}

export function makeMatrix(rows: number, cols: number): Matrix {
  return Array.from({ length: rows }, () => Array<number>(cols).fill(0))
}

export function makeVector(n: number): Vector {
  return Array<number>(n).fill(0)
}

export const BINARY_OPS: Operation[] = ['add', 'sub', 'mul']

export const OP_LABELS: Record<Operation, string> = {
  add: 'Soma',
  sub: 'Subtração',
  mul: 'Multiplicação',
  tra: 'Transposta',
  det: 'Determinante',
  inv: 'Inversa',
}
