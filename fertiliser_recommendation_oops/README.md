# 🌱 Fertilizer Recommendation System (GUI)

This **Fertilizer Recommendation System** is a **GUI-based application** developed in **Python** using the **Tkinter** library. It helps farmers and agriculturalists to choose the best fertilizer for their crops based on various factors such as soil type, crop type, and environmental conditions.

---

## 📋 Features
- **GUI Application**: User-friendly interface built with Tkinter.
- **Fertilizer Recommendation**: Recommends the most suitable fertilizer based on the input parameters.
- **Input Fields**: Allows users to enter temperature, humidity, moisture, soil type, crop type, and NPK (Nitrogen, Phosphorus, Potassium) levels.
- **Dropdown Menus**: Easy selection of soil type and crop type through dropdown menus.
- **Clear Button**: Clears all the input fields with a single click.

---

## 🧩 Project Structure
```
fertilizer_recommender.py  # Main Python file
README.md                  # Documentation
```

---

## ⚙️ Dependencies
- **Python 3.x**
- **Tkinter** (comes pre-installed with Python)
- **ttk** (for advanced widgets)

---

## 📚 How to Run the Application
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/fertilizer-recommendation-system.git
   cd fertilizer-recommendation-system
   ```

2. **Run the Application**:
   ```bash
   python fertilizer_recommender.py
   ```

---

## 🖥️ User Interface
The application has the following input fields:
- **Temperature (°C)**
- **Humidity (%)**
- **Moisture (%)**
- **Soil Type** (Dropdown: Sandy, Loamy, Clayey)
- **Crop Type** (Dropdown: Maize, Sugarcane, Cotton, Tobacco, etc.)
- **Nitrogen Level**
- **Phosphorus Level**
- **Potassium Level**

### Buttons:
- **Recommend**: Generates the recommended fertilizer based on inputs.
- **Clear**: Clears all the input fields.

### Output:
The recommended fertilizer is displayed on the screen.

---

## 🌾 Fertilizer Recommendation Logic
The recommendation is based on the combination of **soil type** and **crop type**:

| Soil Type | Crop Type           | Recommended Fertilizer |
|-----------|---------------------|------------------------|
| Sandy     | Maize, Barley        | Urea                   |
| Sandy     | Paddy, Sugarcane     | DAP                    |
| Loamy     | Cotton, Tobacco      | 14-35-14               |
| Loamy     | Wheat, Oil seeds     | 17-17-17               |
| Clayey    | Pulses, Ground Nuts  | 20-20                  |
| Clayey    | Millets, Sugarcane   | 10-26-26               |
| Unknown   | Any                  | 28-28                  |

---

## 📜 Code Explanation
### **Class: `FertilizerRecommender`**
Contains the core logic for recommending fertilizers based on soil type and crop type.

### **Class: `FertilizerRecommendationApp`**
Builds the GUI interface using Tkinter. It has the following key methods:
- **`recommend_fertilizer()`**: Gathers input from the user, calls the recommendation logic, and displays the result.
- **`clear_fields()`**: Clears all input fields.

---

## 🎯 Future Improvements
- Add more advanced machine learning models for dynamic fertilizer recommendations.
- Connect to a real-time weather API for more accurate predictions.
- Deploy the app as a web application using **Flask** or **Django**.

---

## 📧 Contact
For any queries or improvements, reach out to **Sonali Upadhyay**.
