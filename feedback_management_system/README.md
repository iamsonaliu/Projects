Here's a detailed `README.md` file in markdown format for your **Student Feedback System** project.

---

# 📝 Student Feedback System

A comprehensive **Student Feedback System** built using **Python**, **SQLite**, and **Matplotlib**. This project allows students to submit feedback for faculty members and provides an admin panel to analyze feedback records and visualize average ratings.

---

## 🗃️ Database Schema

The project uses an **SQLite** database (`student_feedback.db`) with a single table:  

### **Table: `feedback`**
| Column      | Data Type | Description                          |
|-------------|-----------|--------------------------------------|
| `student_id` | TEXT      | Unique ID of the student             |
| `faculty_name` | TEXT   | Name of the faculty                  |
| `course`    | TEXT      | Course name                          |
| `section`   | TEXT      | Section name                         |
| `rating`    | INTEGER   | Rating given by the student (1-5)    |
| `comments`  | TEXT      | Additional comments from the student |
| `is_updated`| INTEGER   | Flag to check if comments were updated (0 or 1) |

> **Primary Key**: `(student_id, faculty_name)`

---

## 🚀 How to Run the Project

1. Ensure you have **Python 3.x** installed.
2. Install necessary dependencies:
   ```bash
   pip install matplotlib
   ```
3. Run the script:
   ```bash
   python student_feedback_system.py
   ```

---

## 📋 Features

### 🧑‍🎓 **User Panel**

The User Panel allows students to perform the following actions:

1. **Submit Feedback**  
   Students can submit feedback for a faculty member by providing their details, course, section, rating, and comments.  

2. **View My Feedback**  
   Students can view their submitted feedback records.

3. **Update My Comments**  
   Students can update their feedback comments once. The system restricts further updates after the first modification.

---

### 👨‍💼 **Admin Panel**

The Admin Panel provides tools for viewing and analyzing feedback records:

1. **View All Feedback**  
   Displays all feedback records in the database.

2. **View Feedback by Student**  
   Allows the admin to search for feedback records submitted by a specific student.

3. **View Feedback by Faculty**  
   Shows average ratings grouped by faculty members.

4. **View Feedback by Section**  
   Shows average ratings grouped by sections.

5. **Plot Average Ratings by Faculty**  
   Generates a bar chart of average ratings for each faculty member.

6. **Plot Average Ratings by Section**  
   Generates a bar chart of average ratings for each section.

---

## 📈 Data Visualization

The project uses **Matplotlib** to generate the following visualizations:

1. **Average Ratings by Faculty** (Bar Chart)  
2. **Average Ratings by Section** (Bar Chart)  

---

## 🔐 Admin Login

To access the **Admin Panel**, you need to enter the admin password.

### **Admin Password:**  
`admin@2027`

---

## 📂 Project Structure

```
Student Feedback System
├── student_feedback_system.py   # Main script
├── student_feedback.db          # SQLite database (auto-generated)
└── README.md                    # Documentation
```

---

## ⚙️ Functions Overview

### **Database Initialization**
```python
def initialize_database():
    # Initializes the database and creates the necessary tables.
```

### **User Panel Functions**
| Function               | Description                                           |
|------------------------|-------------------------------------------------------|
| `feedback_taker()`      | Allows students to submit feedback.                  |
| `view_my_feedback()`    | Displays feedback submitted by the student.          |
| `update_comments()`     | Allows students to update their feedback comments.    |

### **Admin Panel Functions**
| Function                      | Description                                           |
|--------------------------------|-------------------------------------------------------|
| `view_feedback()`              | Displays all feedback records.                       |
| `view_student_feedback()`      | Displays feedback records for a specific student.     |
| `view_faculty_feedback()`      | Displays average ratings grouped by faculty.          |
| `view_section_feedback()`      | Displays average ratings grouped by section.          |
| `plot_average_ratings_by_faculty()` | Generates a bar chart of average ratings by faculty. |
| `plot_average_ratings_by_section()` | Generates a bar chart of average ratings by section. |

---

## 🖼️ Sample Visualizations

| Visualization                  | Description                          |
|---------------------------------|--------------------------------------|
| ![Faculty Ratings](faculty_ratings_chart.png) | Bar chart showing average faculty ratings |
| ![Section Ratings](section_ratings_chart.png) | Bar chart showing average section ratings |

---

## 💻 Main Menu Options

```text
--- Student Feedback System ---
1. User Panel
2. Admin Panel
3. Exit
```

### **User Panel Options**

```text
--- User Panel ---
1. Submit Feedback
2. View My Feedback
3. Update My Comments
4. Back to Main Menu
```

### **Admin Panel Options**

```text
--- Admin Panel ---
1. View All Feedback
2. View Feedback by Student
3. View Feedback by Faculty
4. View Feedback by Section
5. Plot Average Ratings by Faculty
6. Plot Average Ratings by Section
7. Exit Admin Panel
```

---

## ⚠️ Error Handling

The project handles the following errors:

- **IntegrityError**: When a student tries to submit duplicate feedback.
- **OperationalError**: When attempting to add an existing column.
- **General Exceptions**: Displayed using message boxes in the GUI.

---

## 📋 Future Improvements

- Add a **GUI** interface using **Tkinter**.
- Implement **login authentication** for both students and admins.
- Add more data visualization charts.
- Export feedback records as **CSV** or **Excel** files.

---

## 🤝 Contribution

Contributions are welcome! If you'd like to enhance the project, feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 📧 Contact

For any queries, contact **Sonali Upadhyay**.
