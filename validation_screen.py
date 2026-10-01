import tkinter as tk
import joblib

# ==========================================
# LOAD AI MODEL
# ==========================================

model = joblib.load("regen_model.pkl")


# ==========================================
# CREATE MAIN WINDOW
# ==========================================

window = tk.Tk()

window.title("EV Regenerative Braking Validation")
window.geometry("700x750")

window.configure(bg="#F2F2F2")


# ==========================================
# VALIDATION FUNCTION
# ==========================================

def validate():

    try:

        # Get input values
        speed = float(speed_entry.get())
        battery = float(battery_entry.get())
        brake = float(brake_entry.get())

        # ----------------------------------
        # INPUT VALIDATION
        # ----------------------------------

        if not (20 <= speed <= 100):

            result_label.config(
                text="INVALID SPEED",
                fg="white",
                bg="red"
            )

            result_box.config(bg="red")

            status_label.config(
                text="✗ INVALID INPUT",
                fg="red"
            )

            return

        if not (20 <= battery <= 100):

            result_label.config(
                text="INVALID BATTERY",
                fg="white",
                bg="red"
            )

            result_box.config(bg="red")

            status_label.config(
                text="✗ INVALID INPUT",
                fg="red"
            )

            return

        if not (10 <= brake <= 100):

            result_label.config(
                text="INVALID BRAKE",
                fg="white",
                bg="red"
            )

            result_box.config(bg="red")

            status_label.config(
                text="✗ INVALID INPUT",
                fg="red"
            )

            return


        # ----------------------------------
        # AI PREDICTION
        # ----------------------------------

        prediction = model.predict(
            [[speed, battery, brake]]
        )[0]


        # ----------------------------------
        # COLOUR INDICATOR
        # ----------------------------------

        if prediction == "Low":

            result_label.config(
                text="LOW",
                fg="white",
                bg="green"
            )

            result_box.config(
                bg="green"
            )

        elif prediction == "Medium":

            result_label.config(
                text="MEDIUM",
                fg="white",
                bg="orange"
            )

            result_box.config(
                bg="orange"
            )

        elif prediction == "High":

            result_label.config(
                text="HIGH",
                fg="white",
                bg="red"
            )

            result_box.config(
                bg="red"
            )


        # ----------------------------------
        # DISPLAY INPUT VALUES
        # ----------------------------------

        values_label.config(
            text=f"Speed: {speed} km/h\n"
                 f"Battery Level: {battery}%\n"
                 f"Brake Pressure: {brake}%"
        )


        # ----------------------------------
        # VALIDATION STATUS
        # ----------------------------------

        status_label.config(
            text="✓ VALIDATED SUCCESSFULLY",
            fg="green"
        )


    except ValueError:

        result_label.config(
            text="ENTER VALID NUMBERS",
            fg="white",
            bg="red"
        )

        result_box.config(
            bg="red"
        )

        status_label.config(
            text="✗ INVALID INPUT",
            fg="red"
        )


# ==========================================
# CLEAR FUNCTION
# ==========================================

def clear_fields():

    speed_entry.delete(0, tk.END)

    battery_entry.delete(0, tk.END)

    brake_entry.delete(0, tk.END)

    result_label.config(
        text="---",
        fg="black",
        bg="#E0E0E0"
    )

    result_box.config(
        bg="#E0E0E0"
    )

    values_label.config(
        text="Enter values and click VALIDATE"
    )

    status_label.config(
        text="Waiting for validation...",
        fg="black"
    )


# ==========================================
# TITLE
# ==========================================

title = tk.Label(
    window,
    text="EV REGENERATIVE BRAKING VALIDATION",
    font=("Arial", 20, "bold"),
    bg="#F2F2F2"
)

title.pack(pady=25)


# ==========================================
# INPUT SECTION
# ==========================================

input_box = tk.Frame(
    window,
    bg="#F2F2F2"
)

input_box.pack(pady=10)


# ------------------------------------------
# SPEED
# ------------------------------------------

tk.Label(
    input_box,
    text="Speed (km/h):",
    font=("Arial", 14),
    bg="#F2F2F2"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)

speed_entry = tk.Entry(
    input_box,
    font=("Arial", 14),
    width=15
)

speed_entry.grid(
    row=0,
    column=1
)


# ------------------------------------------
# BATTERY
# ------------------------------------------

tk.Label(
    input_box,
    text="Battery Level (%):",
    font=("Arial", 14),
    bg="#F2F2F2"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)

battery_entry = tk.Entry(
    input_box,
    font=("Arial", 14),
    width=15
)

battery_entry.grid(
    row=1,
    column=1
)


# ------------------------------------------
# BRAKE
# ------------------------------------------

tk.Label(
    input_box,
    text="Brake Pressure (%):",
    font=("Arial", 14),
    bg="#F2F2F2"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=10
)

brake_entry = tk.Entry(
    input_box,
    font=("Arial", 14),
    width=15
)

brake_entry.grid(
    row=2,
    column=1
)


# ==========================================
# VALIDATE BUTTON
# ==========================================

validate_button = tk.Button(
    window,
    text="VALIDATE",
    font=("Arial", 15, "bold"),
    command=validate,
    width=15
)

validate_button.pack(pady=15)


# ==========================================
# CLEAR BUTTON
# ==========================================

clear_button = tk.Button(
    window,
    text="CLEAR",
    font=("Arial", 12, "bold"),
    command=clear_fields,
    width=15
)

clear_button.pack(pady=5)


# ==========================================
# AI RESULT BOX
# ==========================================

result_box = tk.LabelFrame(
    window,
    text="AI PREDICTION",
    font=("Arial", 16, "bold"),
    padx=50,
    pady=30,
    bg="#E0E0E0"
)

result_box.pack(pady=15)


result_label = tk.Label(
    result_box,
    text="---",
    font=("Arial", 32, "bold"),
    width=20,
    height=2,
    bg="#E0E0E0"
)

result_label.pack()


# ==========================================
# INPUT VALUES
# ==========================================

values_label = tk.Label(
    window,
    text="Enter values and click VALIDATE",
    font=("Arial", 12),
    bg="#F2F2F2"
)

values_label.pack(pady=10)


# ==========================================
# MODEL ACCURACY
# ==========================================

accuracy_label = tk.Label(
    window,
    text="Model Accuracy: 88.89%",
    font=("Arial", 12, "bold"),
    bg="#F2F2F2"
)

accuracy_label.pack(pady=5)


# ==========================================
# VALIDATION STATUS
# ==========================================

status_label = tk.Label(
    window,
    text="Waiting for validation...",
    font=("Arial", 12, "bold"),
    bg="#F2F2F2"
)

status_label.pack(pady=8)


# ==========================================
# COLOUR LEGEND
# ==========================================

legend_label = tk.Label(
    window,
    text="🟢 LOW     🟠 MEDIUM     🔴 HIGH",
    font=("Arial", 12, "bold"),
    bg="#F2F2F2"
)

legend_label.pack(pady=10)


# ==========================================
# START APPLICATION
# ==========================================

window.mainloop()