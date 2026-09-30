import joblib

# Load trained AI model
model = joblib.load("regen_model.pkl")

print("Regenerative Braking AI")
print("-----------------------")

speed = float(input("Enter Speed: "))
battery = float(input("Enter Battery Level: "))
brake = float(input("Enter Brake Pressure: "))

prediction = model.predict([[speed, battery, brake]])

print("\nRegenerative Braking Level:", prediction[0])