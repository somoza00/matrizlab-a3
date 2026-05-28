from display import clear_screen, header, subheader, pause, print_matrix


def what_is_matrix():
    clear_screen()
    header("O QUE E UMA MATRIZ?")
    print("""
  Uma MATRIZ e uma tabela retangular de numeros organizados em
  linhas (horizontais) e colunas (verticais).

  Notacao: Matriz A com m linhas e n colunas  =>  A_{m x n}

  Cada elemento e identificado por dois indices:
    A[i][j]  =  elemento na linha i, coluna j
""")
    print_matrix([[1, 2, 3], [4, 5, 6]], "A (2x3)  -  2 linhas, 3 colunas")
    print("""
  Elementos:
    A[1][1]=1   A[1][2]=2   A[1][3]=3
    A[2][1]=4   A[2][2]=5   A[2][3]=6

  ONDE SÃO USADAS?
  - Graficos 3D (rotacao, escala, projecao de objetos)
  - Redes neurais (pesos e ativacoes)
  - Sistemas de equacoes lineares
  - Economia (tabelas de insumo-produto)
  - Estatistica (matrizes de covariancia)
""")
    pause()


def matrix_types():
    clear_screen()
    header("TIPOS DE MATRIZES")

    subheader("1. Matriz Quadrada (n x n)")
    print("  Mesmo numero de linhas e colunas.")
    print_matrix([[1, 2], [3, 4]], "2x2")

    subheader("2. Matriz Identidade (I)")
    print("  Diagonal principal = 1, todos os outros = 0.")
    print("  Propriedade: A * I = I * A = A  (neutro da multiplicacao)")
    print_matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]], "I_3  (identidade 3x3)")

    subheader("3. Matriz Nula (O)")
    print("  Todos os elementos sao zero.")
    print_matrix([[0, 0], [0, 0]], "O  (nula 2x2)")

    subheader("4. Matriz Transposta (A^T)")
    print("  Trocamos linhas por colunas: A^T[i][j] = A[j][i]")
    print_matrix([[1, 2, 3], [4, 5, 6]], "A  (2x3)")
    print_matrix([[1, 4], [2, 5], [3, 6]], "A^T  (3x2)")

    subheader("5. Matriz Simetrica")
    print("  A = A^T  (simetria em relacao a diagonal principal)")
    print_matrix([[1, 2, 3], [2, 5, 4], [3, 4, 6]], "Simetrica 3x3")

    subheader("6. Matriz Diagonal")
    print("  Apenas a diagonal principal pode ter valores != 0.")
    print_matrix([[3, 0, 0], [0, -1, 0], [0, 0, 5]], "Diagonal 3x3")

    subheader("7. Matriz Triangular Superior / Inferior")
    print("  Superior: zeros abaixo da diagonal")
    print_matrix([[1, 2, 3], [0, 4, 5], [0, 0, 6]], "Triangular Superior")
    print("  Inferior: zeros acima da diagonal")
    print_matrix([[1, 0, 0], [2, 3, 0], [4, 5, 6]], "Triangular Inferior")
    pause()


def tut_add_subtract():
    clear_screen()
    header("SOMA E SUBTRACAO DE MATRIZES")
    print("""
  CONDICAO obrigatoria: as duas matrizes devem ter as MESMAS dimensoes.
  Nao e possivel somar uma 2x3 com uma 3x2, por exemplo.

  REGRA:
    (A + B)[i][j] = A[i][j] + B[i][j]
    (A - B)[i][j] = A[i][j] - B[i][j]
  Operamos elemento a elemento, na mesma posicao.
""")
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print_matrix(A, "A")
    print_matrix(B, "B")

    print("  A + B  (somamos posicao a posicao):")
    print("    [1+5  2+6]   [ 6   8]")
    print("    [3+7  4+8] = [10  12]")
    print_matrix([[6, 8], [10, 12]], "A + B")

    print("  A - B  (subtraimos posicao a posicao):")
    print("    [1-5  2-6]   [-4  -4]")
    print("    [3-7  4-8] = [-4  -4]")
    print_matrix([[-4, -4], [-4, -4]], "A - B")

    print("""  PROPRIEDADES:
    Comutativa:   A + B = B + A
    Associativa:  (A+B)+C = A+(B+C)
    Neutro:       A + O = A
    Oposto:       A + (-A) = O
""")
    pause()


def tut_multiply():
    clear_screen()
    header("MULTIPLICACAO DE MATRIZES")
    print("""
  CONDICAO: colunas de A = linhas de B
    A_{m x n}  *  B_{n x p}  =  C_{m x p}

  REGRA:
    C[i][j] = A[i][1]*B[1][j] + A[i][2]*B[2][j] + ... + A[i][n]*B[n][j]
    (produto escalar da linha i de A com a coluna j de B)

  ATENCAO: A*B  !=  B*A  (NAO e comutativa em geral!)
""")
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print_matrix(A, "A  (2x2)")
    print_matrix(B, "B  (2x2)")

    print("  Calculando C = A * B:")
    print("    C[1][1] = 1*5 + 2*7 = 5 + 14 = 19")
    print("    C[1][2] = 1*6 + 2*8 = 6 + 16 = 22")
    print("    C[2][1] = 3*5 + 4*7 = 15 + 28 = 43")
    print("    C[2][2] = 3*6 + 4*8 = 18 + 32 = 50")
    print_matrix([[19, 22], [43, 50]], "C = A * B")

    print("""  PROPRIEDADES:
    Associativa:   (A*B)*C = A*(B*C)
    Distributiva:  A*(B+C) = A*B + A*C
    Identidade:    A*I = I*A = A
    NAO comutativa: A*B != B*A  (em geral)
    Transposta:    (A*B)^T = B^T * A^T
""")
    pause()


def tut_determinant():
    clear_screen()
    header("DETERMINANTE")
    print("""
  O DETERMINANTE e um numero escalar associado a toda matriz QUADRADA.
  Notacao: det(A) ou |A|

  PARA QUE SERVE?
    det(A) = 0  =>  A e SINGULAR (nao tem inversa, sistema sem solucao unica)
    det(A) != 0 =>  A e INVERSIVEL

  ================================================================
  DETERMINANTE 2x2
  ================================================================
  Para A = | a  b |
           | c  d |

    det(A) = a*d - b*c    (diagonal principal - diagonal secundaria)

  Exemplo:
""")
    print_matrix([[3, 2], [1, 4]], "A")
    print("    det(A) = 3*4 - 2*1 = 12 - 2 = 10")
    print("    det(A) = 10  (!=0 -> inversivel)\n")

    print("""  ================================================================
  DETERMINANTE 3x3  (Regra de Sarrus)
  ================================================================
  Repetimos as duas primeiras colunas a direita:

    | a  b  c  |  a  b
    | d  e  f  |  d  e
    | g  h  i  |  g  h

  Diagonais para baixo (sinal +):   aei,  bfg,  cdh
  Diagonais para cima  (sinal -):   ceg,  afh,  bdi

    det(A) = (aei + bfg + cdh) - (ceg + afh + bdi)

  Exemplo:
""")
    print_matrix([[2, 1, -1], [3, -2, 1], [1, 4, -3]], "A")
    print("    Diagonais positivas: 2*(-2)*(-3) + 1*1*1 + (-1)*3*4 = 12 + 1 - 12 = 1")
    print("    Diagonais negativas: (-1)*(-2)*1 + 2*1*4 + 1*3*(-3) = 2 + 8 - 9 = 1")
    print("    det(A) = 1 - 1 = 0")
    print("    det = 0  =>  linhas linearmente dependentes!\n")

    print("""  PROPRIEDADES:
    det(I) = 1
    det(A^T) = det(A)
    det(A*B) = det(A) * det(B)
    Se uma linha/coluna e zero: det = 0
    Trocar duas linhas: muda sinal do det
""")
    pause()


def tut_inverse():
    clear_screen()
    header("MATRIZ INVERSA")
    print("""
  A inversa de A, escrita A-1, satisfaz:
    A * A-1 = A-1 * A = I

  CONDICAO: A-1 existe SOMENTE se det(A) != 0 !

  ================================================================
  FORMULA DIRETA PARA 2x2
  ================================================================
  Para A = | a  b |  com det(A) = ad - bc
           | c  d |

    A-1 = (1/det) * |  d  -b |
                    | -c   a |
  Exemplo:
""")
    print_matrix([[2, 1], [5, 3]], "A")
    print("    det(A) = 2*3 - 1*5 = 6 - 5 = 1")
    print()
    print("    A-1 = (1/1) * | 3  -1 | = | 3  -1 |")
    print("                  |-5   2 |   |-5   2 |")
    print_matrix([[3, -1], [-5, 2]], "A-1")
    print("    Verificacao: A * A-1:")
    print("      [2  1][3  -1] = [2*3+1*(-5)   2*(-1)+1*2] = [1  0]")
    print("      [5  3][-5  2]   [5*3+3*(-5)   5*(-1)+3*2]   [0  1]  (OK!)")

    print("""
  ================================================================
  METODO GAUSS-JORDAN (funciona para qualquer n)
  ================================================================
  1. Monte [A | I]  (augmentar com identidade a direita)
  2. Aplique operacoes de linha ate o lado esquerdo virar I
  3. O lado direito se torna A-1

  Operacoes de linha permitidas:
    * Multiplicar linha por escalar != 0
    * Somar multiplo de uma linha a outra
    * Trocar duas linhas

  Use a opcao "Matriz Inversa" na Calculadora para ver
  o passo a passo completo com suas proprias matrizes!
""")
    pause()


def tut_linear_systems():
    clear_screen()
    header("SISTEMAS LINEARES")
    print("""
  Um SISTEMA LINEAR e um conjunto de equacoes de 1o grau:

    a11*x1 + a12*x2 + ... + a1n*xn = b1
    a21*x1 + a22*x2 + ... + a2n*xn = b2
    ...
    an1*x1 + an2*x2 + ... + ann*xn = bn

  Na forma matricial: A * x = b
    A = matriz de coeficientes
    x = vetor de incognitas
    b = vetor de termos independentes

  CLASSIFICACAO:
    SPD (Sistema Possivel Determinado):   1 unica solucao   (det(A) != 0)
    SPI (Sistema Possivel Indeterminado): infinitas solucoes (det(A) = 0)
    SI  (Sistema Impossivel):             sem solucao

  ================================================================
  ELIMINACAO DE GAUSS  (metodo da Calculadora)
  ================================================================
  Objetivo: transformar [A|b] em forma triangular superior e
  depois resolver de baixo para cima (substituicao reversa).

  Exemplo  (sistema 2x2):
    2x + 3y = 8
    4x +  y = 6
""")
    print("  Matriz aumentada:")
    print("    [ 2  3  |  8 ]")
    print("    [ 4  1  |  6 ]\n")
    print("  Passo 1: L2 = L2 - 2*L1  (eliminar x da eq.2)")
    print("    [ 2  3  |  8 ]")
    print("    [ 0  -5 | -10 ]\n")
    print("  Substituicao reversa:")
    print("    y = -10 / -5 = 2")
    print("    x = (8 - 3*2) / 2 = 1\n")
    print("  Solucao: x = 1, y = 2")
    print("  Verificacao:")
    print("    2*1 + 3*2 = 8  (OK)")
    print("    4*1 + 1*2 = 6  (OK)\n")
    print("  Use a opcao 'Resolver Sistema Linear' para praticar!")
    pause()
