import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def load_and_prepare_data():
    data = pd.read_csv('C:/Users/sonal/OneDrive/Desktop/python projs/Fertilizer Prediction.csv')

    # Encoding categorical columns
    encoder_soil = LabelEncoder()
    encoder_crop = LabelEncoder()
    encoder_fertiliser = LabelEncoder()

    data['Soil Type'] = encoder_soil.fit_transform(data['Soil Type'])
    data['Crop Type'] = encoder_crop.fit_transform(data['Crop Type'])
    data['Fertilizer Name'] = encoder_fertiliser.fit_transform(data['Fertilizer Name'])

    X = data.drop('Fertilizer Name', axis=1)
    y = data['Fertilizer Name']

    # Splitting the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    return model, encoder_soil, encoder_crop, encoder_fertiliser

# GUI Integration
class FertilizerRecommendationApp:
    def __init__(self, root, model, encoder_soil, encoder_crop, encoder_fertiliser):
        self.root = root
        self.model = model
        self.encoder_soil = encoder_soil
        self.encoder_crop = encoder_crop
        self.encoder_fertiliser = encoder_fertiliser

        self.root.title("Fertilizer Recommendation System")
        tk.Label(root,text="Fertilizer Recommendation System",font=("verdana",20,'bold'),anchor='center').grid(row=0,column=0,sticky='ew')
        self.root.configure(background="green")

        # Input Fields
        tk.Label(root, text="Temperature (°C):",fg="white",bg="green",font=("verdana",14,'italic')).grid(row=1, column=0)
        tk.Label(root, text="Humidity (%):",fg="white",bg="green",font=("verdana",14,'italic')).grid(row=2, column=0)
        tk.Label(root, text="Moisture (%):",fg="white",bg="green",font=("verdana",14,'italic')).grid(row=3, column=0)
        tk.Label(root, text="Soil Type:",fg="white",bg="green",font=("verdana",14,'italic')).grid(row=4, column=0)
        tk.Label(root, text="Crop Type:",fg="white",bg="green",font=("verdana",14,'italic')).grid(row=5, column=0)
        tk.Label(root, text="Nitrogen Level:",fg="white",bg="green",font=("verdana",14,'italic')).grid(row=6, column=0)
        tk.Label(root, text="Phosphorus Level:",fg="white",bg="green",font=("verdana",14,'italic')).grid(row=7, column=0)
        tk.Label(root, text="Potassium Level:",fg="white",bg="green",font=("verdana",14,'italic')).grid(row=8, column=0)

        # Entry Fields
        self.temperature = tk.Entry(root)
        self.humidity = tk.Entry(root)
        self.moisture = tk.Entry(root)
        self.nitrogen = tk.Entry(root)
        self.phosphorus = tk.Entry(root)
        self.potassium = tk.Entry(root)

        # Dropdowns for Soil Type and Crop Type
        self.soil_type = ttk.Combobox(root, values=['Sandy', 'Loamy', 'Black', 'Red', 'Clayey'])
        self.crop_type = ttk.Combobox(root, values=['Maize', 'Sugarcane', 'Cotton', 'Tobacco', 'Paddy', 'Barley',
       'Wheat', 'Millets', 'Oil seeds', 'Pulses', 'Ground Nuts'])

        # Placing the fields
        self.temperature.grid(row=1,column=1,columnspan=5,pady=10,sticky='sw')
        self.humidity.grid(row=2, column=1,columnspan=5,pady=10,sticky='sw')
        self.moisture.grid(row=3, column=1,columnspan=5,pady=10,sticky='sw')
        self.soil_type.grid(row=4, column=1,columnspan=5,pady=10,sticky='sw')
        self.crop_type.grid(row=5, column=1,columnspan=5,pady=10,sticky='sw')
        self.nitrogen.grid(row=6, column=1,columnspan=5,pady=10,sticky='sw')
        self.phosphorus.grid(row=7, column=1,columnspan=5,pady=10,sticky='sw')
        self.potassium.grid(row=8, column=1,columnspan=5,pady=10,sticky='sw')

        # Buttons
        tk.Button(root, text="Recommend",bg="yellow",fg="black",width=15,height=2, command=self.recommend_fertilizer).grid(row=9, column=0, pady=10)
        tk.Button(root, text="Clear", bg="yellow",fg="black",width=15,height=2,command=self.clear_fields).grid(row=9, column=1, pady=10)

        # Output Field
        self.result = tk.Label(root, text="",font=('verdana',20,'bold'),fg="yellow",background="green")
        self.result.grid(row=10, column=0, columnspan=5)

    def recommend_fertilizer(self):
        try:
            # Collect input values
            temperature = float(self.temperature.get())
            humidity = float(self.humidity.get())
            moisture = float(self.moisture.get())
            nitrogen = float(self.nitrogen.get())
            phosphorus = float(self.phosphorus.get())
            potassium = float(self.potassium.get())

            # Get selected values from the dropdown menus
            soil_type = self.encoder_soil.transform([self.soil_type.get()])[0]
            crop_type = self.encoder_crop.transform([self.crop_type.get()])[0]

            # Prepare input for prediction
            input_data = [[temperature, humidity, moisture, nitrogen, phosphorus, potassium, soil_type, crop_type]]
            prediction = self.model.predict(input_data)[0]
            fertilizer_name = self.encoder_fertiliser.inverse_transform([prediction])[0]

            # Display the result
            self.result.config(text=f"Recommended Fertilizer: {fertilizer_name}")

        except Exception as e:
            messagebox.showerror("Error", f"Invalid input or error occurred: {e}")

    def clear_fields(self):
        self.temperature.delete(0, tk.END)
        self.humidity.delete(0, tk.END)
        self.moisture.delete(0, tk.END)
        self.nitrogen.delete(0, tk.END)
        self.phosphorus.delete(0, tk.END)
        self.potassium.delete(0, tk.END)
        self.soil_type.set('select')  # Reset the Soil Type dropdown
        self.crop_type.set('select')  # Reset the Crop Type dropdown
        self.result.config(text="")

# Main Program
if __name__ == "__main__":
    model, encoder_soil, encoder_crop, encoder_fertiliser = load_and_prepare_data()

    root = tk.Tk()
    app = FertilizerRecommendationApp(root, model, encoder_soil, encoder_crop, encoder_fertiliser)
    root.mainloop()
