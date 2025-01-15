# 🌱 Fertilizer Recommendation System (Machine Learning + GUI)

This **Fertilizer Recommendation System** uses a **Decision Tree Classifier** to predict the most suitable fertilizer for crops based on input features like **temperature**, **humidity**, **soil type**, and more. The system is integrated with a **Tkinter GUI** for user interaction, making it accessible for farmers and agriculturalists.

---

## 📋 Features
- **Machine Learning Model**: Uses a **Decision Tree Classifier** for predictions.
- **Data Handling**: Loads and prepares data from a CSV file.
- **GUI Application**: Built with **Tkinter**, providing a user-friendly interface.
- **Real-Time Prediction**: Recommends fertilizers based on the given inputs.

---

## 🧩 Project Structure
```
fertilizer_recommender_ml_gui.py  # Main Python file
Fertilizer Prediction.csv         # Dataset
README.md                         # Documentation
```

---

## ⚙️ Dependencies
- **Python 3.x**
- **pandas**: For data manipulation and analysis.
- **scikit-learn**: For building the machine learning model.
- **Tkinter**: For GUI development.

---

## 📚 How to Run the Application
1. **Install the Required Libraries**:
   ```bash
   pip install pandas scikit-learn
   ```

2. **Ensure the Dataset is Available**:
   Place the `Fertilizer Prediction.csv` file in the specified path:
   ```
   C:/Users/sonal/OneDrive/Desktop/python projs/Fertilizer Prediction.csv
   ```

3. **Run the Application**:
   ```bash
   python fertilizer_recommender_ml_gui.py
   ```

---

## 🧪 Dataset Description
The dataset used is a CSV file containing the following columns:
- **Temperature (°C)**
- **Humidity (%)**
- **Moisture (%)**
- **Soil Type** (Categorical: Sandy, Loamy, Black, Red, Clayey)
- **Crop Type** (Categorical: Maize, Sugarcane, Cotton, Tobacco, etc.)
- **Nitrogen Level** (N)
- **Phosphorus Level** (P)
- **Potassium Level** (K)
- **Fertilizer Name** (Target Variable)

### Example Row:
| Temperature | Humidity | Moisture | Soil Type | Crop Type | Nitrogen | Phosphorus | Potassium | Fertilizer Name |
|-------------|----------|----------|-----------|-----------|----------|------------|-----------|-----------------|
| 26.5        | 68       | 30       | Loamy     | Maize     | 10       | 15         | 12        | Urea            |

---

## 🖥️ User Interface
The application includes the following input fields:
- **Temperature (°C)**
- **Humidity (%)**
- **Moisture (%)**
- **Soil Type** (Dropdown: Sandy, Loamy, Black, Red, Clayey)
- **Crop Type** (Dropdown: Maize, Sugarcane, Cotton, Tobacco, etc.)
- **Nitrogen Level (N)**
- **Phosphorus Level (P)**
- **Potassium Level (K)**

### Buttons:
- **Recommend**: Predicts the recommended fertilizer based on inputs.
- **Clear**: Clears all the input fields.

### Output:
The recommended fertilizer is displayed on the screen.

---

## 🧩 Machine Learning Model
The **Decision Tree Classifier** is trained on the dataset using the following steps:
1. **Data Preprocessing**: Categorical columns are encoded using **LabelEncoder**.
2. **Train-Test Split**: The dataset is split into **80% training** and **20% testing**.
3. **Model Training**: The model is trained using the **Decision Tree Classifier** from **scikit-learn**.

---

## 📈 Example Predictions
| Inputs                            | Recommended Fertilizer |
|-----------------------------------|------------------------|
| Temp: 26.5, Soil: Loamy, Crop: Maize | Urea                   |
| Temp: 30.2, Soil: Sandy, Crop: Wheat | DAP                    |

---

## 🎯 Future Improvements
- Enhance the model with **Random Forest** or **Gradient Boosting** for better accuracy.
- Add a **database** to store previous recommendations.
- Deploy the application as a **web app** using **Flask** or **Django**.
- Add real-time weather API integration for more precise recommendations.

---

## 📧 Contact
For any queries or suggestions, reach out to **Sonali Upadhyay**.
