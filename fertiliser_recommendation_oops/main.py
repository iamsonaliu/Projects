import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
class FertilizerRecommender:
    def __init__(self):
        # List of possible fertilizers
        self.fertilizers = ['Urea', 'DAP', '14-35-14', '28-28', '17-17-17', '20-20', '10-26-26']
    
    def recommend_fertilizer(self, temperature, humidity, moisture, nitrogen, phosphorus, potassium, soil_type, crop_type):
        if soil_type == 'Sandy':
            if crop_type in ['Maize', 'Barley']:
                return 'Urea'  # Urea for Maize and Barley in Sandy soil
            elif crop_type in ['Paddy', 'Sugarcane']:
                return 'DAP'  # DAP for Paddy and Sugarcane in Sandy soil
        elif soil_type == 'Loamy':
            if crop_type in ['Cotton', 'Tobacco']:
                return '14-35-14'  # 14-35-14 for Cotton and Tobacco in Loamy soil
            elif crop_type in ['Wheat', 'Oil seeds']:
                return '17-17-17'  # 17-17-17 for Wheat and Oil seeds in Loamy soil
        elif soil_type == 'Clayey':
            if crop_type in ['Pulses', 'Ground Nuts']:
                return '20-20'  # 20-20 for Pulses and Ground Nuts in Clayey soil
            elif crop_type in ['Millets', 'Sugarcane']:
                return '10-26-26'  # 10-26-26 for Millets and Sugarcane in Clayey soil
        else:
            return '28-28'  # Default fertilizer for unknown soil types
        return 'Urea'

# GUI Integration
class FertilizerRecommendationApp:
    def __init__(self, root):
        self.root = root
        self.recommender = FertilizerRecommender()
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
        self.soil_type = ttk.Combobox(root, values=['Sandy', 'Loamy', 'Clayey'])
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
            soil_type = self.soil_type.get()
            crop_type = self.crop_type.get()

            # Get the fertilizer recommendation
            fertilizer_name = self.recommender.recommend_fertilizer(
                temperature, humidity, moisture, nitrogen, phosphorus, potassium, soil_type, crop_type
            )

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
    root = tk.Tk()
    app = FertilizerRecommendationApp(root)
    root.mainloop()
