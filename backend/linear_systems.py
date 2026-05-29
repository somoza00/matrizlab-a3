from display import fmt, subheader, print_matrix


def input_system(n):
    print(f"\n  Sistema {n}x{n}: {n} equacoes, {n} variaveis (x1, x2, ..., x{n})\n")
    A, b = [], []
    for i in range(n):
        print(f"  Equacao {i+1}:  a1*x1 + a2*x2 + ... + a{n}*x{n} = b")
        while True:
            try:
                coefs = input(f"    Coeficientes (a1 a2 ... a{n}): ").strip().split()
                if len(coefs) != n:
                    print(f"    Esperado {n} valores!")
                    continue
                row = [float(x) for x in coefs]
                bi  = float(input(f"    Termo independente (b): "))
                A.append(row)
                b.append(bi)
                break
            except ValueError:
                print("    Valores invalidos! Use numeros.")

    print("\n  Sistema inserido:")
    for i in range(n):
        terms = " + ".join(f"({fmt(A[i][j])})*x{j+1}" for j in range(n))
        print(f"    {terms} = {fmt(b[i])}")
    print()
    return A, b


def solve(A, b):
    n = len(A)
    subheader("ELIMINACAO DE GAUSS COM SUBSTITUICAO REVERSA")
    print("  Montamos a matriz aumentada [A | b] e escalonamos.")
    print("  Em seguida, resolvemos de baixo para cima (substituicao reversa).\n")

    aug = [A[i][:] + [b[i]] for i in range(n)]
    _print_sys(aug, n, "Matriz aumentada inicial [A | b]")

    step = 1

    # Forward elimination with partial pivoting
    for col in range(n):
        max_row = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[max_row][col]) < 1e-12:
            print("  Sistema SEM SOLUCAO UNICA (coluna de zeros detectada).")
            return None

        if max_row != col:
            aug[col], aug[max_row] = aug[max_row], aug[col]
            print(f"  Passo {step}: Troca  L{col+1} <-> L{max_row+1}  (pivot maior)")
            _print_sys(aug, n)
            step += 1

        pivot = aug[col][col]
        for row in range(col + 1, n):
            if abs(aug[row][col]) < 1e-12:
                continue
            factor = aug[row][col] / pivot
            aug[row] = [aug[row][k] - factor * aug[col][k] for k in range(n + 1)]
            s = "-" if factor > 0 else "+"
            print(f"  Passo {step}: Elim.  L{row+1} = L{row+1} {s} {fmt(abs(factor))}*L{col+1}")
            _print_sys(aug, n)
            step += 1

    print("  Forma escalonada obtida! Iniciando substituicao reversa:\n")

    # Back substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        if abs(aug[i][i]) < 1e-12:
            print("  Sistema SEM SOLUCAO UNICA (pivo zero na substituicao).")
            return None
        soma = aug[i][n]
        terms_str = f"{fmt(aug[i][n])}"
        for j in range(i + 1, n):
            soma -= aug[i][j] * x[j]
            terms_str += f" - {fmt(aug[i][j])}*{fmt(x[j])}"
        x[i] = soma / aug[i][i]
        print(f"  x{i+1} = ( {terms_str} ) / {fmt(aug[i][i])}  =  {fmt(x[i])}")

    print("\n" + "="*40)
    print("  SOLUCAO DO SISTEMA:")
    for i, xi in enumerate(x):
        print(f"    x{i+1} = {fmt(xi)}")
    print("="*40)

    print("\n  Verificacao  (A*x deve ser igual a b):")
    ok = True
    for i in range(n):
        calc = sum(A[i][j] * x[j] for j in range(n))
        diff = abs(calc - b[i])
        status = "(OK)" if diff < 1e-6 else "(ERRO)"
        print(f"    Equacao {i+1}: {fmt(calc)} = {fmt(b[i])}  {status}")
        if diff >= 1e-6:
            ok = False
    if ok:
        print("\n  Solucao verificada com sucesso!")
    return x


def _print_sys(aug, n, label=None):
    if label:
        print(f"\n  {label}:")
    rows = len(aug)
    all_vals = [aug[i][j] for i in range(rows) for j in range(n + 1)]
    max_w = max(len(fmt(v)) for v in all_vals)
    max_w = max(max_w, 1)
    for row in aug:
        left  = "  ".join(f"{fmt(v):>{max_w}}" for v in row[:n])
        right = f"{fmt(row[n]):>{max_w}}"
        print(f"  [ {left}  |  {right} ]")
    print()
