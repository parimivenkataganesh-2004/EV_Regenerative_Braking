import pandas as pd

data = []

for speed in range(20, 101, 10):
    for battery in range(20, 101, 10):
        for brake in range(10, 101, 10):

            speed_score = (speed / 100) * 40
            brake_score = (brake / 100) * 40
            battery_effect = ((100 - battery) / 100) * 20

            score = speed_score + brake_score + battery_effect

            if score < 40:
                regeneration = "Low"
            elif score < 70:
                regeneration = "Medium"
            else:
                regeneration = "High"

            data.append([
                speed,
                battery,
                brake,
                regeneration
            ])

dataset = pd.DataFrame(
    data,
    columns=["Speed", "Battery", "Brake", "Regeneration"]
)

dataset.to_csv("dataset.csv", index=False)

print("New dataset created successfully!")
print("Total examples:", len(dataset))