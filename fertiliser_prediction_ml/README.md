#  Heart Disease Prediction System

A **Heart Disease Prediction System** built using **Python** and **Logistic Regression** to predict whether a person has a heart condition based on medical data. The system uses a trained machine learning model to classify patients as healthy or in need of medical attention based on input features.

---

## 📂 Project Structure
```
heart_disease_prediction.ipynb  # Main Notebook file
heart_disease_data.csv          # Dataset containing patient records
README.md                       # Documentation
```

---

## 📋 Dataset Overview
The project uses the **Heart Disease Dataset**, which contains several medical features to predict whether a patient has heart disease.

### **Dataset Columns:**
| Feature        | Description                                       |
|----------------|---------------------------------------------------|
| `age`          | Age of the patient                                |
| `sex`          | Gender (0 = Female, 1 = Male)                     |
| `cp`           | Chest pain type (0-3)                             |
| `trestbps`     | Resting blood pressure (mm Hg)                    |
| `chol`         | Serum cholesterol (mg/dl)                         |
| `fbs`          | Fasting blood sugar > 120 mg/dl (1 = True, 0 = False) |
| `restecg`      | Resting electrocardiographic results (0-2)        |
| `thalach`      | Maximum heart rate achieved                       |
| `exang`        | Exercise-induced angina (1 = Yes, 0 = No)         |
| `oldpeak`      | ST depression induced by exercise relative to rest |
| `slope`        | The slope of the peak exercise ST segment         |
| `ca`           | Number of major vessels (0-4) colored by fluoroscopy |
| `thal`         | Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect) |
| `target`       | Heart disease status (1 = Defective Heart, 0 = Healthy) |

---

## 🧪 Libraries Used
- **pandas**: Data manipulation and analysis
- **numpy**: Array operations
- **scikit-learn**: Machine learning tools
  - `train_test_split`: Splitting the dataset into training and test sets
  - `LogisticRegression`: Logistic Regression model
  - `accuracy_score`: Model performance evaluation

---

## 📈 Workflow
### 1. **Loading the Dataset**
The dataset is loaded using **pandas**:
```python
df = pd.read_csv('/heart_disease_data.csv')
```

### 2. **Data Inspection**
Basic inspection of the dataset:
- `df.head()`: View the first 5 rows
- `df.tail()`: View the last 5 rows
- `df.shape`: Check the number of rows and columns
- `df.info()`: Check the data types and non-null values
- `df.describe()`: View statistical summary

### 3. **Splitting the Data**
The dataset is split into **features (X)** and **target (Y)**:
```python
X = df.drop(columns='target', axis=1)
Y = df['target']
```

Using **train_test_split()** to split the data into **training** and **testing** sets:
```python
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=23)
```

### 4. **Model Training**
A **Logistic Regression** model is used for training:
```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, Y_train)
```

### 5. **Model Evaluation**
The trained model is evaluated using **accuracy_score**:
```python
from sklearn.metrics import accuracy_score

Y_pred = model.predict(X_test)
score = accuracy_score(Y_test, Y_pred)
print("The accuracy score is:", score)
```

---

## 🧠 Building a Predictive System
The predictive system takes a patient's medical data as input and predicts whether they are healthy or need medical attention.

### **Example Input:**
```python
input_data = (62, 0, 0, 140, 268, 0, 0, 160, 0, 3.6, 0, 2, 2)
```

### **Prediction Logic:**
```python
arr = np.array(input_data)
prediction = model.predict(arr.reshape(1, -1))

if prediction == 0:
    print("You are healthy")
else:
    print("Consult your doctor")
```

---

## 🔬 Model Performance
- **Model Used**: Logistic Regression
- **Accuracy Score**: The model achieved a high accuracy score on the test data.

---

## ⚙️ How to Run the Project
1. Ensure you have **Python 3.x** installed.
2. Install the required libraries:
   ```bash
   pip install pandas numpy scikit-learn
   ```
3. Run the **Jupyter Notebook** file:
   ```bash
   jupyter notebook heart_disease_prediction.ipynb
   ```

---

## 📈 Future Improvements
- Add more machine learning models (e.g., Random Forest, SVM) for better accuracy.
- Include feature engineering to improve the model's performance.
- Deploy the model using **Flask** or **Streamlit** for a user-friendly interface.

---

## 🤝 Contribution
Contributions are welcome! Fork the repository and submit a pull request with your improvements.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 📧 Contact
For any queries, reach out to **Sonali Upadhyay**.
