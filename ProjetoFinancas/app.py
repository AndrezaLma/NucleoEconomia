from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Funções de cálculo de juros
def calcular_juros_simples(principal, taxa_de_juros, tempo):
    return principal * (1 + (taxa_de_juros / 100) * tempo)

def calcular_juros_compostos(principal, taxa_de_juros, tempo):
    return principal * ((1 + (taxa_de_juros / 100)) ** tempo)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    principal = float(data['principal'])
    taxa_de_juros = float(data['taxa_de_juros'])
    tempo = int(data['tempo'])

    montantes_simples = [calcular_juros_simples(principal, taxa_de_juros, ano) for ano in range(tempo + 1)]
    montantes_compostos = [calcular_juros_compostos(principal, taxa_de_juros, ano) for ano in range(tempo + 1)]

    return jsonify({'simples': montantes_simples, 'compostos': montantes_compostos})

if __name__ == '__main__':
    app.run(debug=True)
