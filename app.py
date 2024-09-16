from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)

# Configurar CORS
CORS(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/v1/api/predecir_calorias', methods=['POST'])
def predecir_calorias():
    # Obtener los datos del cuerpo de la solicitud
    data = request.json
    total_fat = data.get('total_fat')
    carbohydrate = data.get('carbohydrate')
    protein = data.get('protein')
    sodium = data.get('sodium')

    # Ejecutar el script Python y pasarle los parámetros
    try:
        result = subprocess.run(
            ['python', 'predict_calories.py', str(total_fat), str(carbohydrate), str(protein), str(sodium)],
            capture_output=True, text=True, check=True
        )
        predicted_calories = result.stdout.strip()
        return jsonify({'calorias_estimadas': predicted_calories})
    except subprocess.CalledProcessError as e:
        print(f'Error: {e.stderr}')
        return 'Error al predecir las calorías.', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

