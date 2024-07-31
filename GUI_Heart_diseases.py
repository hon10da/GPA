import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from ttkthemes import ThemedStyle

# Load the dataset
heart_data = pd.read_csv(r'D:\data set\archive (6)\heart.csv')

# Prepare the data
X = heart_data.drop('target', axis=1)
y = heart_data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize StandardScaler with feature names
scaler = StandardScaler()
scaler.fit(X_train)

# Build and train the model
model = LogisticRegression(max_iter=1000)
model.fit(scaler.transform(X_train), y_train)

def predict():
    if (age_entry.get() == '' or sex_combobox.get() == '' or cp_combobox.get() == '' or
            trestbps_entry.get() == '' or chol_entry.get() == '' or fbs_combobox.get() == '' or
            restecg_combobox.get() == '' or thalach_entry.get() == '' or exang_combobox.get() == '' or
            oldpeak_entry.get() == '' or slope_combobox.get() == '' or ca_entry.get() == '' or
            thal_entry.get() == ''):
        result_label.config(text="Please fill in all fields.")
        return

    try:
        # Convert input data to appropriate types
        age = int(age_entry.get())
        sex = int(gender_options[sex_combobox.get()])  # Corrected encoding
        cp = int(cp_combobox.get())
        trestbps = int(trestbps_entry.get())
        chol = int(chol_entry.get())
        fbs = int(fbs_combobox.get())
        restecg = int(restecg_combobox.get())
        thalach = int(thalach_entry.get())
        exang = int(exang_combobox.get())
        oldpeak = float(oldpeak_entry.get())
        slope = int(slope_combobox.get())
        ca = int(ca_entry.get())
        thal = int(thal_entry.get())
    except ValueError:
        result_label.config(text="Please enter valid numeric values.")
        return
    
    try:
        # Scale the input data using the same scaler
        input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        input_data_scaled = scaler.transform(input_data)
    except Exception as e:
        result_label.config(text="Error occurred during data scaling: " + str(e))
        return

    prediction = model.predict(input_data_scaled)
    probability = model.predict_proba(input_data_scaled)[0]
    
    if prediction[0] == 1:
        result_label.config(text=f"The patient has a {probability[1]*100:.2f}% probability of having heart disease.", foreground="green")
    else:
        result_label.config(text=f"The patient has a {probability[0]*100:.2f}% probability of not having heart disease.", foreground="green")

    # Plotting the bar chart
    fig, ax = plt.subplots(figsize=(7, 5))
    features = X.columns
    input_values = input_data[0]

    # Plot the mean values as a line
    ax.plot(features, scaler.mean_, marker='o', color='blue', label='Mean')

    # Plot the input values as bars
    ax.bar(features, input_values, color='orange', label='Input')

    # Add error bars for standard deviation
    ax.errorbar(features, scaler.mean_, yerr=scaler.scale_, fmt=' ', color='blue', capsize=4, label='Std Dev')

    ax.set_title('Patient Information vs Normal Values with Standard Deviation')
    ax.set_ylabel('Values')
    ax.set_xlabel('Features')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Convert matplotlib figure to Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=5, padx=12, pady=12, sticky="nsew")

def clear_fields():
    # Clear all entry fields
    age_entry.delete(0, tk.END)
    sex_combobox.set('')
    cp_combobox.set('')
    trestbps_entry.delete(0, tk.END)
    chol_entry.delete(0, tk.END)
    fbs_combobox.set('')
    restecg_combobox.set('')
    thalach_entry.delete(0, tk.END)
    exang_combobox.set('')
    oldpeak_entry.delete(0, tk.END)
    slope_combobox.set('')
    ca_entry.delete(0, tk.END)
    thal_entry.delete(0, tk.END)
    # Clear result label
    result_label.config(text='')

# Create the main application window
app = tk.Tk()
app.title("Heart Disease Prediction")
app.configure(background='white')  # Set background color

# Set ttk theme
style = ThemedStyle(app)
style.set_theme("arc")

# Create and place the input fields and labels
input_frame = ttk.LabelFrame(app, text="Enter Patient Information", padding=20)
input_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Age
age_label = ttk.Label(input_frame, text="Age:", padding=5)
age_label.grid(row=0, column=0, padx=2, pady=5, sticky="w")
age_entry = ttk.Entry(input_frame)
age_entry.grid(row=0, column=1, padx=2, pady=5)

# Sex
sex_label = ttk.Label(input_frame, text="Sex:", padding=5)
sex_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
gender_options = {"Male": "0", "Female": "1"}  # Corrected encoding
sex_combobox = ttk.Combobox(input_frame, values=list(gender_options.keys()))  
sex_combobox.grid(row=0, column=3, padx=5, pady=5)

# Chest Pain Type
cp_label = ttk.Label(input_frame, text="Chest Pain Type:", padding=5)
cp_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
cp_combobox = ttk.Combobox(input_frame, values=["0", "1", "2", "3"])
cp_combobox.grid(row=1, column=1, padx=5, pady=5)

# Resting Blood Pressure
trestbps_label = ttk.Label(input_frame, text="Resting Blood Pressure:", padding=5)
trestbps_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")
trestbps_entry = ttk.Entry(input_frame)
trestbps_entry.grid(row=1, column=3, padx=5, pady=5)

# Cholesterol Level
chol_label = ttk.Label(input_frame, text="Cholesterol Level:", padding=5)
chol_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
chol_entry = ttk.Entry(input_frame)
chol_entry.grid(row=2, column=1, padx=5, pady=5)

# Fasting Blood Sugar
fbs_label = ttk.Label(input_frame, text="Fasting Blood Sugar:", padding=5)
fbs_label.grid(row=2, column=2, padx=5, pady=5, sticky="w")
fbs_combobox = ttk.Combobox(input_frame, values=["0", "1"])
fbs_combobox.grid(row=2, column=3, padx=5, pady=5)

# Resting Electrocardiographic Results
restecg_label = ttk.Label(input_frame, text="Resting Electrocardiographic Results:", padding=5)
restecg_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
restecg_combobox = ttk.Combobox(input_frame, values=["0", "1", "2"])
restecg_combobox.grid(row=3, column=1, padx=5, pady=5)

# Maximum Heart Rate Achieved
thalach_label = ttk.Label(input_frame, text="Maximum Heart Rate Achieved:", padding=5)
thalach_label.grid(row=3, column=2, padx=5, pady=5, sticky="w")
thalach_entry = ttk.Entry(input_frame)
thalach_entry.grid(row=3, column=3, padx=5, pady=5)

# Exercise Induced Angina
exang_label = ttk.Label(input_frame, text="Exercise Induced Angina:", padding=5)
exang_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
exang_combobox = ttk.Combobox(input_frame, values=["0", "1"])
exang_combobox.grid(row=4, column=1, padx=5, pady=5)

# ST Depression Induced by Exercise
oldpeak_label = ttk.Label(input_frame, text="ST Depression Induced by Exercise:", padding=5)
oldpeak_label.grid(row=4, column=2, padx=5, pady=5, sticky="w")
oldpeak_entry = ttk.Entry(input_frame)
oldpeak_entry.grid(row=4, column=3, padx=5, pady=5)

# Slope of the Peak Exercise ST Segment
slope_label = ttk.Label(input_frame, text="Slope of the Peak Exercise ST Segment:", padding=5)
slope_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
slope_combobox = ttk.Combobox(input_frame, values=["0", "1", "2"])
slope_combobox.grid(row=5, column=1, padx=5, pady=5)

# Number of Major Vessels Colored by Fluoroscopy
ca_label = ttk.Label(input_frame, text="Number of Major Vessels Colored by Fluoroscopy:", padding=5)
ca_label.grid(row=5, column=2, padx=5, pady=5, sticky="w")
ca_entry = ttk.Entry(input_frame)
ca_entry.grid(row=5, column=3, padx=5, pady=5)

# Thalassemia
thal_label = ttk.Label(input_frame, text="Thalassemia:", padding=5)
thal_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
thal_entry = ttk.Entry(input_frame)
thal_entry.grid(row=6, column=1, padx=5, pady=5)

# Create and place the prediction button on the left
predict_button = ttk.Button(app, text="Predict", command=predict)
predict_button.grid(row=1, column=0, padx=10, pady=10, sticky="e")  # Sticky to align to the right

# Create and place the clear button
clear_button = ttk.Button(app, text="Clear Fields", command=clear_fields)
clear_button.grid(row=2, column=0, padx=10, pady=10, sticky="e")  # Sticky to align to the left

# Label to display prediction result on the left
result_label = ttk.Label(app, text="", padding=20, foreground="red", font=("Arial", 12, "bold"))
result_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")  # Sticky to align to the left

# Configure grid weights to make the input frame expandable
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

# Bind Enter key to focus on the next widget
app.bind('<Return>', lambda event: event.widget.tk_focusNext().focus())

# Run the application
app.mainloop()
