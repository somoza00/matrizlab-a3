import sys
import io
import os
from contextlib import redirect_stdout
from flask import Flask, request, jsonify
from flask_cors import CORS

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import matrix_ops
import linear_systems

app = Flask(__name__)
CORS(app)


def capture(func, *args):
    buf = io.StringIO()
    with redirect_stdout(buf):
        result = func(*args)
    return result, buf.getvalue()


@app.route("/api/add", methods=["POST"])
def api_add():
    try:
        d = request.get_json()
        result, steps = capture(matrix_ops.add, d["A"], d["B"])
        if result is None:
            return jsonify({"ok": False, "error": steps})
        return jsonify({"ok": True, "result": result, "steps": steps})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)})


@app.route("/api/subtract", methods=["POST"])
def api_subtract():
    try:
        d = request.get_json()
        result, steps = capture(matrix_ops.subtract, d["A"], d["B"])
        if result is None:
            return jsonify({"ok": False, "error": steps})
        return jsonify({"ok": True, "result": result, "steps": steps})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)})


@app.route("/api/multiply", methods=["POST"])
def api_multiply():
    try:
        d = request.get_json()
        result, steps = capture(matrix_ops.multiply, d["A"], d["B"])
        if result is None:
            return jsonify({"ok": False, "error": steps})
        return jsonify({"ok": True, "result": result, "steps": steps})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)})


@app.route("/api/transpose", methods=["POST"])
def api_transpose():
    try:
        d = request.get_json()
        result, steps = capture(matrix_ops.transpose, d["A"])
        return jsonify({"ok": True, "result": result, "steps": steps})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)})


@app.route("/api/determinant", methods=["POST"])
def api_determinant():
    try:
        d = request.get_json()
        A = d["A"]
        if len(A) != len(A[0]):
            return jsonify({"ok": False, "error": "O determinante só existe para matrizes quadradas!"})
        result, steps = capture(matrix_ops.determinant, A)
        return jsonify({"ok": True, "result": result, "steps": steps})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)})


@app.route("/api/inverse", methods=["POST"])
def api_inverse():
    try:
        d = request.get_json()
        A = d["A"]
        if len(A) != len(A[0]):
            return jsonify({"ok": False, "error": "A inversa só existe para matrizes quadradas!"})
        result, steps = capture(matrix_ops.inverse, A)
        if result is None:
            return jsonify({"ok": False, "error": "Matriz singular — det = 0, não possui inversa.", "steps": steps})
        return jsonify({"ok": True, "result": result, "steps": steps})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)})


@app.route("/api/solve", methods=["POST"])
def api_solve():
    try:
        d = request.get_json()
        A, b = d["A"], d["b"]
        result, steps = capture(linear_systems.solve, A, b)
        if result is None:
            return jsonify({"ok": False, "error": "Sistema sem solução única!", "steps": steps})
        return jsonify({"ok": True, "result": result, "steps": steps})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
