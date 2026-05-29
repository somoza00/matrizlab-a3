from display import fmt, print_matrix, print_aug, subheader


# ── Input ──────────────────────────────────────────────────────────────────

def input_matrix(name, rows=None, cols=None):
    print(f"\n  === Inserir Matriz {name} ===")
    while rows is None:
        try:
            rows = int(input(f"  Numero de linhas de {name}: "))
            if rows <= 0: raise ValueError
        except ValueError:
            print("  Digite um inteiro positivo!")
            rows = None
    while cols is None:
        try:
            cols = int(input(f"  Numero de colunas de {name}: "))
            if cols <= 0: raise ValueError
        except ValueError:
            print("  Digite um inteiro positivo!")
            cols = None

    print(f"  Digite cada linha com {cols} valor(es) separados por espaco:")
    matrix = []
    for i in range(rows):
        while True:
            try:
                parts = input(f"  Linha {i+1}: ").strip().split()
                if len(parts) != cols:
                    print(f"  Esperado {cols} valores, recebido {len(parts)}!")
                    continue
                matrix.append([float(x) for x in parts])
                break
            except ValueError:
                print("  Valores invalidos! Use numeros (ex: 1 2.5 -3)")

    print_matrix(matrix, f"Matriz {name}")
    return matrix


# ── Basic operations ────────────────────────────────────────────────────────

def add(A, B):
    m, n = len(A), len(A[0])
    if len(B) != m or len(B[0]) != n:
        print(f"  ERRO: dimensoes incompativeis ({m}x{n} vs {len(B)}x{len(B[0])})")
        return None
    subheader("SOMA DE MATRIZES")
    print("  Regra: C[i][j] = A[i][j] + B[i][j]  (somamos posicao a posicao)")
    print("  Condicao: A e B devem ter as mesmas dimensoes.\n")
    print_matrix(A, "A")
    print_matrix(B, "B")
    print("  Calculando elemento a elemento:")
    result = [[0.0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
            print(f"    C[{i+1}][{j+1}] = {fmt(A[i][j])} + {fmt(B[i][j])} = {fmt(result[i][j])}")
    print_matrix(result, "Resultado A + B")
    return result


def subtract(A, B):
    m, n = len(A), len(A[0])
    if len(B) != m or len(B[0]) != n:
        print(f"  ERRO: dimensoes incompativeis ({m}x{n} vs {len(B)}x{len(B[0])})")
        return None
    subheader("SUBTRACAO DE MATRIZES")
    print("  Regra: C[i][j] = A[i][j] - B[i][j]  (subtraimos posicao a posicao)")
    print("  Condicao: A e B devem ter as mesmas dimensoes.\n")
    print_matrix(A, "A")
    print_matrix(B, "B")
    print("  Calculando elemento a elemento:")
    result = [[0.0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            result[i][j] = A[i][j] - B[i][j]
            print(f"    C[{i+1}][{j+1}] = {fmt(A[i][j])} - ({fmt(B[i][j])}) = {fmt(result[i][j])}")
    print_matrix(result, "Resultado A - B")
    return result


def multiply(A, B):
    m, n = len(A), len(A[0])
    if len(B) != n:
        print(f"  ERRO: colunas de A ({n}) != linhas de B ({len(B)})")
        return None
    p = len(B[0])
    subheader("MULTIPLICACAO DE MATRIZES")
    print(f"  A eh {m}x{n}, B eh {n}x{p}  ->  C sera {m}x{p}")
    print("  Regra: C[i][j] = soma( A[i][k] * B[k][j] ) para k = 1..n\n")
    print_matrix(A, "A")
    print_matrix(B, "B")
    print("  Calculando (produto escalar linha x coluna):")
    result = [[0.0]*p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            terms = [f"{fmt(A[i][k])}*{fmt(B[k][j])}" for k in range(n)]
            val = sum(A[i][k] * B[k][j] for k in range(n))
            result[i][j] = val
            print(f"    C[{i+1}][{j+1}] = {' + '.join(terms)} = {fmt(val)}")
    print_matrix(result, "Resultado A x B")
    return result


def transpose(A):
    m, n = len(A), len(A[0])
    subheader("TRANSPOSTA")
    print("  Regra: AT[i][j] = A[j][i]  (trocamos linhas por colunas)\n")
    print_matrix(A, f"A ({m}x{n})")
    result = [[A[j][i] for j in range(m)] for i in range(n)]
    print(f"  A tem {m} linhas e {n} colunas  ->  AT tem {n} linhas e {m} colunas")
    print_matrix(result, f"Transposta AT ({n}x{m})")
    return result


# ── Determinant ─────────────────────────────────────────────────────────────

def _minor(A, row, col):
    return [[A[i][j] for j in range(len(A[0])) if j != col]
            for i in range(len(A)) if i != row]

def _det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    total = 0.0
    for j in range(n):
        total += ((-1)**j) * A[0][j] * _det(_minor(A, 0, j))
    return total


def determinant(A):
    n = len(A)
    subheader("DETERMINANTE")
    print_matrix(A, "A")

    if n == 1:
        print(f"  Matriz 1x1:  det(A) = {fmt(A[0][0])}")
        return A[0][0]

    if n == 2:
        a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
        det = a*d - b*c
        print("  Formula para 2x2:")
        print("    det(A) = a*d - b*c")
        print(f"    det(A) = {fmt(a)}*{fmt(d)} - {fmt(b)}*{fmt(c)}")
        print(f"    det(A) = {fmt(a*d)} - {fmt(b*c)}")
        print(f"\n  det(A) = {fmt(det)}")
        _det_meaning(det)
        return det

    if n == 3:
        print("  Expansao em cofatores pela 1a linha:\n")
        det = 0.0
        for j in range(3):
            sign = (-1)**j
            m = _minor(A, 0, j)
            m_det = m[0][0]*m[1][1] - m[0][1]*m[1][0]
            contrib = sign * A[0][j] * m_det
            det += contrib
            s = "+" if sign == 1 else "-"
            print(f"  {s} A[1][{j+1}] * det(M{j+1})  =  {s} {fmt(A[0][j])} * {fmt(m_det)}  =  {fmt(contrib)}")
        print(f"\n  det(A) = {fmt(det)}")
        _det_meaning(det)
        return det

    print(f"  Calculando det de {n}x{n} por expansao recursiva...")
    det = _det(A)
    print(f"\n  det(A) = {fmt(det)}")
    _det_meaning(det)
    return det


def _det_meaning(det):
    if abs(det) < 1e-9:
        print("  Interpretacao: det = 0  ->  matriz SINGULAR (sem inversa, linhas dependentes)")
    else:
        print(f"  Interpretacao: det != 0  ->  matriz INVERSIVEL")


# ── Inverse ─────────────────────────────────────────────────────────────────

def inverse(A):
    n = len(A)
    subheader("MATRIZ INVERSA  (Metodo de Gauss-Jordan)")
    print("  Objetivo: montar [A | I] e aplicar operacoes de linha ate obter [I | A-1]\n")
    print_matrix(A, "A")

    det = _det(A)
    print(f"  Verificando: det(A) = {fmt(det)}")
    if abs(det) < 1e-10:
        print("  RESULTADO: det = 0  ->  A eh SINGULAR e NAO possui inversa!")
        return None
    print("  det != 0  ->  A possui inversa. Iniciando Gauss-Jordan...\n")

    aug = [A[i][:] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    print_aug(aug, n, "Matriz aumentada [A | I]")

    step = 1
    for col in range(n):
        max_row = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[max_row][col]) < 1e-12:
            print("  SINGULAR: nao foi possivel calcular a inversa.")
            return None

        if max_row != col:
            aug[col], aug[max_row] = aug[max_row], aug[col]
            print(f"  Passo {step}: Troca  L{col+1} <-> L{max_row+1}")
            print_aug(aug, n)
            step += 1

        pivot = aug[col][col]
        if abs(pivot - 1.0) > 1e-10:
            aug[col] = [x / pivot for x in aug[col]]
            print(f"  Passo {step}: Escala  L{col+1} = L{col+1} / {fmt(pivot)}")
            print_aug(aug, n)
            step += 1

        for row in range(n):
            if row == col or abs(aug[row][col]) < 1e-12:
                continue
            factor = aug[row][col]
            aug[row] = [aug[row][k] - factor * aug[col][k] for k in range(2*n)]
            s = "-" if factor > 0 else "+"
            print(f"  Passo {step}: Elim.  L{row+1} = L{row+1} {s} {fmt(abs(factor))}*L{col+1}")
            print_aug(aug, n)
            step += 1

    inv = [[round(aug[i][n+j], 8) for j in range(n)] for i in range(n)]
    print_matrix(inv, "Matriz Inversa A-1")

    prod = [[round(sum(A[i][k]*inv[k][j] for k in range(n)), 6) for j in range(n)] for i in range(n)]
    print("  Verificacao: A x A-1 deve ser a identidade I")
    print_matrix(prod, "A x A-1")
    return inv
