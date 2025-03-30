from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Matheus31",
        database="ans_dados"
    )

@app.route('/operadoras', methods=['GET'])
def listar_operadoras():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT Registro_ANS, CNPJ, Razao_Social FROM operadoras_ativas")
    operadoras = cursor.fetchall()

    cursor.close()
    conexao.close()

    return jsonify(operadoras)

if __name__ == '__main__':
    app.run(debug=True)
