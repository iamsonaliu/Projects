import sqlite3
from tkinter import messagebox
DB_NAME = 'student_feedback.db'

def initialize_database():
    #Initializes the database and creates the necessary tables.
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create feedback table with a composite primary key
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS feedback (
        student_id TEXT,
        faculty_name TEXT,
        course TEXT,
        section TEXT,
        rating INTEGER,
        comments TEXT,
        PRIMARY KEY (student_id, faculty_name))'''
    )
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")
           
"""USER PANEL FUNCTIONS"""

def feedback_taker(student_id, course, section, faculty_name, rating, comments):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        # Insert the feedback data into the database
        cursor.execute('''INSERT INTO feedback (student_id, faculty_name, course, section, rating, comments)
                        VALUES (?, ?, ?, ?, ?, ?)''', (student_id, faculty_name, course, section, rating, comments))
        conn.commit()
        messagebox.showinfo("Success", "Feedback submitted successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Feedback for this faculty by the same student already exists.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        conn.close()

def view_my_feedback():
    #Allows a student to view their submitted feedback.
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    student_id = input("Enter your Student ID: ")
    
    # Fetch feedback for the given student ID
    cursor.execute("SELECT * FROM feedback WHERE student_id = ?", (student_id,))
    feedback_data = cursor.fetchall()

    if feedback_data:
        print("\n--- Your Feedback ---")
        for row in feedback_data:
            print(f"Faculty: {row[1]}, Course: {row[2]}, Section: {row[3]}, Rating: {row[4]}, Comments: {row[5]}")
    else:
        print("No feedback found for your Student ID.")

    conn.close()

def add_is_updated_column():
    # Adds the is_updated column to the feedback table if it doesn't exist
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("ALTER TABLE feedback ADD COLUMN is_updated INTEGER DEFAULT 0")
        conn.commit()
        print("Column 'is_updated' added successfully!")
    except sqlite3.OperationalError:
        # This error occurs if the column already exists
        print("Column 'is_updated' already exists in the database.")

    conn.close()


def update_comments():
    # Allows a student to update comments once
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    student_id = input("Enter your Student ID: ")
    faculty_name = input("Enter the Faculty Name for which you want to update the comments: ")

    # Check if the feedback exists and if it's already updated
    cursor.execute('''
        SELECT comments, is_updated 
        FROM feedback 
        WHERE student_id = ? AND faculty_name = ?
    ''', (student_id, faculty_name))
    result = cursor.fetchone()

    if not result:
        print("\nNo feedback found for the given Student ID and Faculty Name.")
    elif result[1] == 1:
        print("\nYou have already updated your comments. Further updates are not allowed.")
    else:
        print(f"\nCurrent Comments: {result[0]}")
        new_comments = input("Enter your new comments: ")

        # Update comments in the database
        cursor.execute('''
            UPDATE feedback 
            SET comments = ?, is_updated = 1 
            WHERE student_id = ? AND faculty_name = ?
        ''', (new_comments, student_id, faculty_name))
        conn.commit()
        print("\nComments updated successfully!")

    conn.close()


def user_panel():
    while True:
        print("\n--- User Panel ---")
        print("1. Submit Feedback")
        print("2. View My Feedback")
        print("3. Update My Comments")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            feedback_taker()
        elif choice == '2':
            view_my_feedback()
        elif choice == '3':
            update_comments()  # Add this line
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")

"""ADMIN PANEL FUNCTIONS"""

def view_feedback():
    # Admin can view all feedback records
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM feedback")
    feedback_records = cursor.fetchall()

    if feedback_records:
        print("\n--- All Feedback Records ---")
        for record in feedback_records:
            print(f"Student ID: {record[0]}, Faculty: {record[1]}, Course: {record[2]}, Section: {record[3]}, Rating: {record[4]}, Comments: {record[5]}")
    else:
        print("\nNo feedback found in the database.")

    conn.close()

def view_student_feedback():
    # Admin can view feedback for a specific student
    student_id = input("Enter the Student ID to view their feedback: ")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM feedback WHERE student_id = ?", (student_id,))
    feedback_records = cursor.fetchall()

    if feedback_records:
        print(f"\n--- Feedback for Student ID {student_id} ---")
        for record in feedback_records:
            print(f"Faculty: {record[1]}, Course: {record[2]}, Section: {record[3]}, Rating: {record[4]}, Comments: {record[5]}")
    else:
        print(f"\nNo feedback found for Student ID {student_id}.")

    conn.close()

def view_faculty_feedback():
    # Admin can view feedback grouped by faculty
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT faculty_name, AVG(rating) as avg_rating FROM feedback GROUP BY faculty_name")
    feedback_records = cursor.fetchall()

    if feedback_records:
        print("\n--- Feedback Summary by Faculty ---")
        for record in feedback_records:
            print(f"Faculty: {record[0]}, Average Rating: {record[1]:.2f}")
    else:
        print("\nNo feedback found in the database.")

    conn.close()

def view_section_feedback():
    # Admin can view feedback grouped by section
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT section, AVG(rating) as avg_rating FROM feedback GROUP BY section")
    feedback_records = cursor.fetchall()

    if feedback_records:
        print("\n--- Feedback Summary by Section ---")
        for record in feedback_records:
            print(f"Section: {record[0]}, Average Rating: {record[1]:.2f}")
    else:
        print("\nNo feedback found in the database.")

    conn.close()

import matplotlib.pyplot as plt

def plot_average_ratings_by_faculty():
    """Plot a bar chart of average ratings for each faculty."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT faculty_name, AVG(rating) as avg_rating FROM feedback GROUP BY faculty_name")
    data = cursor.fetchall()
    conn.close()

    if data:
        faculty_names = [row[0] for row in data]
        avg_ratings = [row[1] for row in data]

        plt.figure(figsize=(10, 6))
        plt.bar(faculty_names, avg_ratings, color='skyblue')
        plt.xlabel('Faculty Name')
        plt.ylabel('Average Rating')
        plt.title('Average Ratings by Faculty')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print("\nNo feedback data available to generate the graph.")

def plot_average_ratings_by_section():
    """Plot a bar chart of average ratings for each section."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT section, AVG(rating) as avg_rating FROM feedback GROUP BY section")
    data = cursor.fetchall()
    conn.close()

    if data:
        sections = [row[0] for row in data]
        avg_ratings = [row[1] for row in data]

        plt.figure(figsize=(8, 5))
        plt.bar(sections, avg_ratings, color='lightgreen')
        plt.xlabel('Section')
        plt.ylabel('Average Rating')
        plt.title('Average Ratings by Section')
        plt.tight_layout()
        plt.show()
    else:
        print("\nNo feedback data available to generate the graph.")


# Define the admin password
ADMIN_PASSWORD = "admin@2027"

def admin_login():
    """Prompt the admin for a password and verify access."""
    for attempt in range(3):  # Allow up to 3 attempts
        password = input("Enter the admin password: ").strip()
        if password == ADMIN_PASSWORD:
            print("Access granted!\n")
            return True
        else:
            print(f"Incorrect password! {2 - attempt} attempts remaining.")
    print("Too many failed attempts. Returning to the main menu.")
    return False

def admin_panel():
    """Admin panel with options for analysis and visualization."""
    if not admin_login():  # Check if the admin successfully logged in
        return

    while True:
        print("\n--- Admin Panel ---")
        print("1. View All Feedback")
        print("2. View Feedback by Student")
        print("3. View Feedback by Faculty")
        print("4. View Feedback by Section")
        print("5. Plot Average Ratings by Faculty")
        print("6. Plot Average Ratings by Section")
        print("7. Exit Admin Panel")

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            view_feedback()  # View all feedback
        elif choice == '2':
            view_student_feedback()  # View feedback by student
        elif choice == '3':
            view_faculty_feedback()  # View feedback by faculty
        elif choice == '4':
            view_section_feedback()  # View feedback by section
        elif choice == '5':
            plot_average_ratings_by_faculty()  # Plot ratings by faculty
        elif choice == '6':
            plot_average_ratings_by_section()  # Plot ratings by section
        elif choice == '7':
            print("Exiting Admin Panel...")
            break
        else:
            print("Invalid choice! Please try again.")

def main_menu():
    #Displays the main menu and directs the user to Admin or User panels.
    ch='Y'
    while (ch =='Y'):
        print("\n--- Student Feedback System ---")
        print("1. User Panel")
        print("2. Admin Panel")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            user_panel()
        elif choice == '2':
            admin_panel()
        elif choice == '3':
            break
        else:
            print("Invalid choice! Please try again.")
        ch=input("do you want to continue (Y/N)")
    print("THANKYOU FOR YOUR TIME\n HAVE A NICE DAY AHEAD!\n")
if __name__ == "__main__":
    initialize_database()
    main_menu()
