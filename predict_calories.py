import sys
import joblib
import warnings
import pandas as pd

# Desactivar la advertencia de sklearn
warnings.filterwarnings("ignore", message="X does not have valid feature names")

# Cargar el modelo desde el archivo
model = joblib.load('modelo_calorias_galleta.pkl')  # Actualiza la ruta si es necesario

# Obtener los valores de entrada desde los argumentos de línea de comandos
total_fat = float(sys.argv[1])
carbohydrate = float(sys.argv[2])
protein = float(sys.argv[3])
sodium = float(sys.argv[4])

# Crear la entrada para el modelo con nombres de características
nueva_galleta = pd.DataFrame([[total_fat, carbohydrate, protein, sodium]], columns=['total_fat', 'carbohydrate', 'protein', 'sodium'])

# Hacer la predicción
calorias_predichas = model.predict(nueva_galleta)

# Imprimir la predicción para que Node.js la reciba
print(calorias_predichas[0])
