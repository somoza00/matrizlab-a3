import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fmt(val):
    if isinstance(val, (int, float)):
        rounded = round(val, 9)
        if abs(rounded) < 1e-9:
            return "0"
        if rounded == int(rounded) and abs(rounded) < 1e9:
            return str(int(rounded))
        return f"{rounded:.4g}"
    return str(val)

def header(title):
    line = "=" * 64
    print(f"\n{line}")
    print(f"  {title}")
    print(f"{line}")

def subheader(title):
    print(f"\n--- {title} ---\n")

def pause():
    input("\n  [Pressione ENTER para continuar...]")

def print_matrix(matrix, label=None):
    if not matrix or not matrix[0]:
        return
    if label:
        print(f"\n  {label}:")
    rows = len(matrix)
    cols = len(matrix[0])
    max_w = max(len(fmt(matrix[i][j])) for i in range(rows) for j in range(cols))
    max_w = max(max_w, 1)
    for row in matrix:
        parts = "  ".join(f"{fmt(v):>{max_w}}" for v in row)
        print(f"  [ {parts} ]")
    print()

def print_aug(aug, n, label=None):
    if label:
        print(f"\n  {label}:")
    rows = len(aug)
    all_vals = [aug[i][j] for i in range(rows) for j in range(len(aug[0]))]
    max_w = max(len(fmt(v)) for v in all_vals)
    max_w = max(max_w, 1)
    for row in aug:
        left  = "  ".join(f"{fmt(v):>{max_w}}" for v in row[:n])
        right = "  ".join(f"{fmt(v):>{max_w}}" for v in row[n:])
        print(f"  [ {left}  |  {right} ]")
    print()
