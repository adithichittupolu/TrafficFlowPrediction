import joblib
import numpy as np

# Example input: hour=8, dayofweek=2, month=5, temp=290.0, rain_1h=0.0, snow_1h=0.0
input_data = np.array([[8, 2, 5, 290.0, 0.0, 0.0]])

model = joblib.load('traffic_model.pkl')
predicted_volume = model.predict(input_data)
print(f"Predicted traffic volume: {predicted_volume[0]:.0f}")
