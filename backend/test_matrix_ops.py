from matrix_ops import add, subtract, multiply, transpose, determinant, inverse

def test_add():
    assert add([[1,2],[3,4]], [[5,6],[7,8]]) == [[6.0,8.0],[10.0,12.0]]

def test_add_dimensoes_incompativeis():
    assert add([[1,2]], [[1],[2]]) is None

def test_subtract():
    assert subtract([[5,6],[7,8]], [[1,2],[3,4]]) == [[4.0,4.0],[4.0,4.0]]

def test_multiply_identidade():
    I = [[1,0],[0,1]]
    A = [[3,4],[5,6]]
    assert multiply(A, I) == [[3.0,4.0],[5.0,6.0]]

def test_multiply_dimensoes_incompativeis():
    assert multiply([[1,2]], [[1,2]]) is None

def test_transpose():
    assert transpose([[1,2,3],[4,5,6]]) == [[1.0,4.0],[2.0,5.0],[3.0,6.0]]

def test_determinante_2x2():
    assert determinant([[1,2],[3,4]]) == -2.0

def test_determinante_singular():
    assert determinant([[1,2],[2,4]]) == 0.0

def test_inverse_2x2():
    result = inverse([[2,0],[0,2]])
    assert result == [[0.5,0.0],[0.0,0.5]]

def test_inverse_singular():
    assert inverse([[1,2],[2,4]]) is None