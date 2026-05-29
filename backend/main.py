from display import clear_screen, header, pause, print_matrix
import matrix_ops as mo
import linear_systems as ls
import tutorial as tut


def main():
    while True:
        clear_screen()
        header("SISTEMA DE ENSINO DE MATRIZES")
        print("""
  [1]  Tutorial Teorico
  [2]  Calculadora de Matrizes
  [3]  Resolver Sistema Linear
  [0]  Sair
""")
        ch = input("  Escolha uma opcao: ").strip()
        if ch == '1':
            menu_tutorial()
        elif ch == '2':
            menu_calculadora()
        elif ch == '3':
            menu_sistema()
        elif ch == '0':
            clear_screen()
            print("  Ate logo!\n")
            break
        else:
            print("  Opcao invalida!")
            pause()


# ── Tutorial ─────────────────────────────────────────────────────────────────

def menu_tutorial():
    while True:
        clear_screen()
        header("TUTORIAL TEORICO")
        print("""
  [1]  O que e uma Matriz?
  [2]  Tipos de Matrizes
  [3]  Soma e Subtracao
  [4]  Multiplicacao de Matrizes
  [5]  Determinante
  [6]  Matriz Inversa
  [7]  Sistemas Lineares
  [0]  Voltar
""")
        ch = input("  Escolha um topico: ").strip()
        if   ch == '1': tut.what_is_matrix()
        elif ch == '2': tut.matrix_types()
        elif ch == '3': tut.tut_add_subtract()
        elif ch == '4': tut.tut_multiply()
        elif ch == '5': tut.tut_determinant()
        elif ch == '6': tut.tut_inverse()
        elif ch == '7': tut.tut_linear_systems()
        elif ch == '0': break
        else:
            print("  Opcao invalida!")
            pause()


# ── Calculadora ───────────────────────────────────────────────────────────────

def menu_calculadora():
    while True:
        clear_screen()
        header("CALCULADORA DE MATRIZES")
        print("""
  [1]  Soma           (A + B)
  [2]  Subtracao      (A - B)
  [3]  Multiplicacao  (A x B)
  [4]  Transposta     (A^T)
  [5]  Determinante   det(A)
  [6]  Matriz Inversa A-1
  [0]  Voltar
""")
        ch = input("  Escolha uma operacao: ").strip()

        if ch == '1':
            clear_screen(); header("SOMA  A + B")
            A = mo.input_matrix("A")
            B = mo.input_matrix("B", rows=len(A), cols=len(A[0]))
            mo.add(A, B)
            pause()

        elif ch == '2':
            clear_screen(); header("SUBTRACAO  A - B")
            A = mo.input_matrix("A")
            B = mo.input_matrix("B", rows=len(A), cols=len(A[0]))
            mo.subtract(A, B)
            pause()

        elif ch == '3':
            clear_screen(); header("MULTIPLICACAO  A x B")
            A = mo.input_matrix("A")
            print(f"\n  B deve ter {len(A[0])} linha(s) para a multiplicacao ser possivel.")
            B = mo.input_matrix("B", rows=len(A[0]))
            mo.multiply(A, B)
            pause()

        elif ch == '4':
            clear_screen(); header("TRANSPOSTA  A^T")
            A = mo.input_matrix("A")
            mo.transpose(A)
            pause()

        elif ch == '5':
            clear_screen(); header("DETERMINANTE  det(A)")
            A = mo.input_matrix("A")
            if len(A) != len(A[0]):
                print(f"\n  ERRO: o determinante so existe para matrizes quadradas!")
                print(f"  Voce inseriu uma matriz {len(A)}x{len(A[0])}.")
            else:
                mo.determinant(A)
            pause()

        elif ch == '6':
            clear_screen(); header("MATRIZ INVERSA  A-1")
            A = mo.input_matrix("A")
            if len(A) != len(A[0]):
                print(f"\n  ERRO: a inversa so existe para matrizes quadradas!")
                print(f"  Voce inseriu uma matriz {len(A)}x{len(A[0])}.")
            else:
                mo.inverse(A)
            pause()

        elif ch == '0':
            break
        else:
            print("  Opcao invalida!")
            pause()


# ── Sistema Linear ────────────────────────────────────────────────────────────

def menu_sistema():
    clear_screen()
    header("RESOLVER SISTEMA LINEAR  Ax = b")
    print("""
  Este modulo resolve sistemas quadrados (n equacoes, n variaveis)
  usando o metodo de Eliminacao de Gauss com substituicao reversa.
""")
    try:
        n = int(input("  Numero de variaveis / equacoes (n): ").strip())
        if n <= 0:
            print("  O numero deve ser positivo!")
            pause()
            return
        A, b = ls.input_system(n)
        ls.solve(A, b)
    except ValueError:
        print("  Entrada invalida!")
    pause()


if __name__ == "__main__":
    main()
