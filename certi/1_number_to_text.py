''' Na linguagem de sua preferência, crie um servidor HTTP que, para cada requisição GET, retorne um JSON cuja chave extenso
 seja a versão por extenso do número inteiro enviado no path. Os números podem estar no intervalo [-99999, 99999].'''

from flask import Flask, jsonify
from num2words import num2words
app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"erro" : "Forneça um numero valido"}), 406


@app.route("/<number>")
def get_multiply_by_10(number):
    number = int(number)
    if number < -99999 or number > 99999:
        return jsonify({"erro":"O numero deve estar dentro da faixa -99999 a 99999"}), 406
    num = num2words(number,lang='pt_BR')
    return jsonify({"extenso" : num }), 200


if __name__ == '__main__':
    app.run(debug=True)
