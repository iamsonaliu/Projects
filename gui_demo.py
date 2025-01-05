from tkinter import *
from tkinter import messagebox
import main_copy as m  # Ensure this file exists and contains the required functions

# Initialize the main window
root = Tk()
root.configure(background="#b5651d")
root.geometry("500x600")
root.title("Feedback Page")
root.resizable(0, 0)

# Frames for the main page and sub-pages
main_page = Frame(root, bg="#b5651d")
stud_page = Frame(root, bg="grey")
admin_page = Frame(root, bg="purple")
feedback_page = Frame(root, bg="grey")

for frame in (main_page, stud_page, admin_page,feedback_page):
    frame.place(relwidth=1, relheight=1)

# page calling function
def show_frame(frame):
    frame.tkraise()

# Function to handle form submission
def submit_feedback():
    # Collect feedback form data
    student_id = student_id_entry.get().strip()
    course = course_entry.get().strip()
    section = section_var.get()
    faculty_name = faculty_var.get()
    rating = rating_var.get()
    comments = comments_text.get("1.0", END).strip()

    if not all([student_id, course, section, faculty_name, rating]):
        messagebox.showerror("Error", "All fields except comments are mandatory.")
        return

    try:
        # Call the feedback_taker function from the main.py file
        m.feedback_taker(student_id, course, section, faculty_name, rating, comments)

        # Clear the form after successful submission
        student_id_entry.delete(0, END)
        course_entry.delete(0, END)
        section_var.set(sections[0])
        faculty_var.set(faculty_by_section[sections[0]][0])
        rating_var.set(3)
        comments_text.delete("1.0", END)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Widgets for feedback form
Label(feedback_page, text="Student Feedback Form", bg="grey", fg="white", font=("Verdana", 16)).pack(pady=10)

Label(feedback_page, text="Student ID:", bg="#b5651d", fg="white").pack(anchor=W, padx=20, pady=(10, 0))
student_id_entry = Entry(feedback_page)
student_id_entry.pack(pady=5)

Label(feedback_page, text="Course Name:", bg="#b5651d", fg="white").pack(anchor=W, padx=20, pady=(10, 0))
course_entry = Entry(feedback_page)
course_entry.pack(pady=5)

Label(feedback_page, text="Section:", bg="#b5651d", fg="white").pack(anchor=W, padx=20, pady=(10, 0))
sections = ["A1", "A2"]
section_var = StringVar(value=sections[0])
OptionMenu(feedback_page, section_var, *sections).pack(pady=5)

Label(feedback_page, text="Faculty Name:", bg="#b5651d", fg="white").pack(anchor=W, padx=20, pady=(10, 0))
faculty_by_section = {
    "A1": ["Dr. Mahesh Manchanda", "Mr. Suhail Vij", "Dr. Ankit Kumar", "Ms. Ayushi Jain", "Ms. Geetika", "Dr. Ankit Kumar", "Mr. Rahul Chauhan", "Mr. Suhail Vij", "Dr. Ashish Garg"],
    "A2": ["Dr. Mahesh Manchanda", "Mr. Suhail Vij", "Dr. Ankit Kumar", "Ms. Ayushi Jain", "Ms. Geetika", "Dr. Ankit Kumar", "Mr. Rahul Chauhan", "Mr. Suhail Vij", "Dr. Ashish Garg"],
}
faculty_var = StringVar(value=faculty_by_section[sections[0]][0])

def update_faculty_list(*args):
    faculty_var.set(faculty_by_section[section_var.get()][0])
    faculty_menu["menu"].delete(0, "end")
    for faculty in faculty_by_section[section_var.get()]:
        faculty_menu["menu"].add_command(label=faculty, command=lambda f=faculty: faculty_var.set(f))

section_var.trace("w", update_faculty_list)
faculty_menu = OptionMenu(feedback_page, faculty_var, *faculty_by_section[sections[0]])
faculty_menu.pack(pady=5)

Label(feedback_page, text="Rating (1-5):", bg="#b5651d", fg="white").pack(anchor=W, padx=20, pady=(10, 0))
rating_var = IntVar(value=3)
Scale(feedback_page, from_=1, to=5, orient=HORIZONTAL, variable=rating_var, length=200).pack(pady=5)

Label(feedback_page, text="Comments (optional):", bg="#b5651d", fg="white").pack(anchor=W, padx=20, pady=(10, 0))
comments_text = Text(feedback_page, height=4, width=30)
comments_text.pack(pady=5)

Button(feedback_page, text="Submit", command=submit_feedback, bg="white", fg="black", width=15).pack(pady=20)
Button(feedback_page, text="BACK", bg="white", fg="black", width=10, command=lambda: show_frame(stud_page)).pack(pady=(20))
#Main Page
main_label = Label(main_page, text="Feedback Portal", fg="white", bg="#b5651d", font=("Verdana", 25))
main_label.pack(pady=(20, 10))
main_labell = Label(main_page, text="Login as", fg="white", bg="#b5651d", font=("Verdana", 20))
main_labell.pack(pady=(10, 10))
# Button to navigate to Student page
next_btn1 = Button(main_page, text="STUDENT", bg="white", fg="black", width=20, height=1,command=lambda: show_frame(stud_page))
next_btn1.pack(pady=(10, 5))
# Button to navigate to Admin page
next_btn2 = Button(main_page, text="ADMIN", bg="white", fg="black", width=20, height=1,command=lambda: show_frame(admin_page))
next_btn2.pack(pady=(5, 10))

# Add your feedback form elements here (for example, Text boxes, Rating, etc.)
feedback_label = Label(feedback_page, text="Feedback Form", fg="black", bg="grey", font=("Verdana", 16))
feedback_label.pack(pady=(20, 10))

#Student Page
stud_label = Label(stud_page, text="Student Feedback", fg="white", bg="grey", font=("Verdana", 16))
stud_label.pack(pady=(20, 10))
feedback_btn = Button(stud_page, text="Submit Feedback", bg="white", fg="black", width=10, command=lambda: show_frame(feedback_page))
feedback_btn.pack(pady=(20,10))

back_btn_stud = Button(stud_page, text="BACK", bg="white", fg="black", width=10,command=lambda: show_frame(main_page))
back_btn_stud.pack(pady=(20, 10))

#Admin Page
admin_label = Label(admin_page, text="Admin Panel", fg="white", bg="#b5651d", font=("Verdana", 16))
admin_label.pack(pady=(20, 10))

back_btn_admin = Button(admin_page, text="BACK", bg="white", fg="black", width=10,command=lambda: show_frame(main_page))
back_btn_admin.pack(pady=(20, 10))


#main page open
show_frame(main_page)
root.mainloop()
