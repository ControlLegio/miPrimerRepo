
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/saludo', methods=['POST'])
def saludo():
    data = request.get_json()
    nombre = data.get('nombre')
    if nombre:
        return jsonify({"mensaje": "¡Excelente, lo lograste!"})
    else:
        return jsonify({"error": "Falta el campo 'nombre'"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
