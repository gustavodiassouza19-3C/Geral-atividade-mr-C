from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/produto")
def produto():
    produto = {
        "id": 1,
        "nome": "Teclado Mecânico",
        "preco": 199.90,
        "disponivel": True
    }
    return jsonify(produto)

if __name__ == "__main__":
    app.run(debug=True)