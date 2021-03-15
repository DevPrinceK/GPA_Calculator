"""A GUI Desktop App|| Calculates the GPA and Class of a Student"""
"""A GUI Desktop App|| Calculates the GPA and Class of a Student"""
from tkinter import *

# Main window
root = Tk()
root.title("KP || GPA and CLass Calculator".upper())
root.geometry("700x600")    # Dimensions of the main window
root.resizable(False, False)


def reset():
    #Resets all entry widgets/boxes
    ent_c1_1.delete(0, END)
    ent_c1_2.delete(0, END)
    ent_c1_3.delete(0, END)

    ent_c2_1.delete(0, END)
    ent_c2_2.delete(0, END)
    ent_c2_3.delete(0, END)

    ent_c3_1.delete(0, END)
    ent_c3_2.delete(0, END)
    ent_c3_3.delete(0, END)

    ent_c4_1.delete(0, END)
    ent_c4_2.delete(0, END)
    ent_c4_3.delete(0, END)

    ent_c5_1.delete(0, END)
    ent_c5_2.delete(0, END)
    ent_c5_3.delete(0, END)

    ent_c6_1.delete(0, END)
    ent_c6_2.delete(0, END)
    ent_c6_3.delete(0, END)
    gpa_text.config(text="GPA: n/a\nClass: n/a")

def calculate():
    # Performs the actual computations
    credit_per_hour = []
    grades = []
    gpt = []
    try:
        entries_credits = [ent_c1_2.get(), ent_c2_2.get(), ent_c3_2.get(), 
        ent_c4_2.get(), ent_c5_2.get(), ent_c6_2.get()]

        entries_grades = [ent_c1_3.get(), ent_c2_3.get(), ent_c3_3.get(), 
        ent_c4_3.get(), ent_c5_3.get(), ent_c6_3.get()]

        for i in range(len(entries_credits)):
            #Takes all the credits into one list
            ent = entries_credits[i]
            credit_per_hour.append(int(ent))
            #Takes all the scores into one list
            grade = entries_grades[i]
            grades.append(grade)

            if grades[i].upper() == "A":
                gpt.append(4.0*credit_per_hour[i])
            elif grades[i].upper() == "B+":
                gpt.append(3.5*credit_per_hour[i])
            elif grades[i].upper() == "B": 
                gpt.append(3.0*credit_per_hour[i])
            elif grades[i].upper() == "C+":
                gpt.append(2.5*credit_per_hour[i])
            elif grades[i].upper() == "C":
                gpt.append(2.0*credit_per_hour[i])
            elif grades[i].upper() == "D+":
                gpt.append(1.5*credit_per_hour[i])
            elif grades[i].upper() == "D":
                gpt.append(1.0*credit_per_hour[i])
            elif grades[i].upper() == "E":
                gpt.append(0.5*credit_per_hour[i])
            else:
                gpt.append(0.0*credit_per_hour[i])
        # Finds the GPA to 2 decimal places
        gpa = float(round(sum(gpt) / sum(credit_per_hour), 2))
        # Assigns Classes
        if gpa > 3.59:
            class_gpa = "First Class"
        elif gpa > 2.59:
            class_gpa = "Second Class Upper"
        elif gpa > 1.99:
            class_gpa = "Second Class Lower"
        elif gpa > 1.59:
            class_gpa = "Third Class"
        elif gpa > 0.99:
            class_gpa = "Pass"
        else:
            class_gpa = "La Wu!"

        gpa_text.config(text=f"GPA: {str(gpa)}\nClass: {class_gpa}")

    except ValueError:
        gpa_text.config(text="Value Error!!\nCheck and enter the right input!")
    except TypeError:
        gpa_text.config(text="Type Error!!\nCheck the type of inputs available")
###################################################################################

label_1_text = "Please provide the necessary information".upper()
label_1 = Label(root, text =label_1_text, font=("Helvetica", 15))
label_1.place(x=100, y=10)

# Separator
line_up = Label(root, width=81, bg="blue")
line_up.place(x=60, y=40)

# Course one
# Info for Course 1   || Info for Course 1
# Info for Course 1   || Info for Course 1
frame_1 = Frame(root)
frame_1.place(x=60, y=70)

lab_c1_1 = Label(frame_1, text="Course: ", font=("Sans", 14))
lab_c1_1.pack(side=LEFT)

ent_c1_1 = Entry(frame_1, width=10, font=("Sans", 14))
ent_c1_1.pack(side=LEFT)

lab_c1_2 = Label(frame_1, text="  Credit: ", font=("Sans", 14))
lab_c1_2.pack(side=LEFT)

ent_c1_2 = Entry(frame_1, width=10, font=("Sans", 14))
ent_c1_2.pack(side=LEFT)

lab_c1_3 = Label(frame_1, text="  Grade: ", font=("Sans", 14))
lab_c1_3.pack(side=LEFT)

ent_c1_3 = Entry(frame_1, width=10, font=("Sans", 14))
ent_c1_3.pack(side=LEFT)

# Course Two
# Info for Course 2   || Info for Course 2 || Course, Credit and Grade
# Info for Course 2   || Info for Course 2 || Course, Credit and Grade
frame_2 = Frame(root)
frame_2.place(x=60, y=110)

lab_c2_1 = Label(frame_2, text="Course: ", font=("Sans", 14))
lab_c2_1.pack(side=LEFT)

ent_c2_1 = Entry(frame_2, width=10, font=("Sans", 14))
ent_c2_1.pack(side=LEFT)

lab_c2_2 = Label(frame_2, text="  Credit: ", font=("Sans", 14))
lab_c2_2.pack(side=LEFT)

ent_c2_2 = Entry(frame_2, width=10, font=("Sans", 14))
ent_c2_2.pack(side=LEFT)

lab_c2_3 = Label(frame_2, text="  Grade: ", font=("Sans", 14))
lab_c2_3.pack(side=LEFT)

ent_c2_3 = Entry(frame_2, width=10, font=("Sans", 14))
ent_c2_3.pack(side=LEFT)

# Course Three
# Info for Course 3   || Info for Course 3 || Course, Credit and Grade
# Info for Course 3   || Info for Course 3 || Course, Credit and Grade
frame_3 = Frame(root)
frame_3.place(x=60, y=150)

lab_c3_1 = Label(frame_3, text="Course: ", font=("Sans", 14))
lab_c3_1.pack(side=LEFT)

ent_c3_1 = Entry(frame_3, width=10, font=("Sans", 14))
ent_c3_1.pack(side=LEFT)

lab_c3_2 = Label(frame_3, text="  Credit: ", font=("Sans", 14))
lab_c3_2.pack(side=LEFT)

ent_c3_2 = Entry(frame_3, width=10, font=("Sans", 14))
ent_c3_2.pack(side=LEFT)

lab_c3_3 = Label(frame_3, text="  Grade: ", font=("Sans", 14))
lab_c3_3.pack(side=LEFT)

ent_c3_3 = Entry(frame_3, width=10, font=("Sans", 14))
ent_c3_3.pack(side=LEFT)

# Course Four
# Info for Course 4   || Info for Course 4 || Course, Credit and Grade
# Info for Course 4   || Info for Course 4 || Course, Credit and Grade
frame_4 = Frame(root)
frame_4.place(x=60, y=190)

lab_c4_1 = Label(frame_4, text="Course: ", font=("Sans", 14))
lab_c4_1.pack(side=LEFT)

ent_c4_1 = Entry(frame_4, width=10, font=("Sans", 14))
ent_c4_1.pack(side=LEFT)

lab_c4_2 = Label(frame_4, text="  Credit: ", font=("Sans", 14))
lab_c4_2.pack(side=LEFT)

ent_c4_2 = Entry(frame_4, width=10, font=("Sans", 14))
ent_c4_2.pack(side=LEFT)

lab_c4_3 = Label(frame_4, text="  Grade: ", font=("Sans", 14))
lab_c4_3.pack(side=LEFT)

ent_c4_3 = Entry(frame_4, width=10, font=("Sans", 14))
ent_c4_3.pack(side=LEFT)

# Course Five
# Info for Course 5   || Info for Course 5 || Course, Credit and Grade
# Info for Course 5   || Info for Course 5 || Course, Credit and Grade
frame_5 = Frame(root)
frame_5.place(x=60, y=230)

lab_c5_1 = Label(frame_5, text="Course: ", font=("Sans", 14))
lab_c5_1.pack(side=LEFT)

ent_c5_1 = Entry(frame_5, width=10, font=("Sans", 14))
ent_c5_1.pack(side=LEFT)

lab_c5_2 = Label(frame_5, text="  Credit: ", font=("Sans", 14))
lab_c5_2.pack(side=LEFT)

ent_c5_2 = Entry(frame_5, width=10, font=("Sans", 14))
ent_c5_2.pack(side=LEFT)

lab_c5_3 = Label(frame_5, text="  Grade: ", font=("Sans", 14))
lab_c5_3.pack(side=LEFT)

ent_c5_3 = Entry(frame_5, width=10, font=("Sans", 14))
ent_c5_3.pack(side=LEFT)

# Course Six
# Info for Course 6   || Info for Course 6 || Course, Credit and Grade
# Info for Course 6   || Info for Course 6 || Course, Credit and Grade
frame_6 = Frame(root)
frame_6.place(x=60, y=270)

lab_c6_1 = Label(frame_6, text="Course: ", font=("Sans", 14))
lab_c6_1.pack(side=LEFT)

ent_c6_1 = Entry(frame_6, width=10, font=("Sans", 14))
ent_c6_1.pack(side=LEFT)

lab_c6_2 = Label(frame_6, text="  Credit: ", font=("Sans", 14))
lab_c6_2.pack(side=LEFT)

ent_c6_2 = Entry(frame_6, width=10, font=("Sans", 14))
ent_c6_2.pack(side=LEFT)

lab_c6_3 = Label(frame_6, text="  Grade: ", font=("Sans", 14))
lab_c6_3.pack(side=LEFT)

ent_c6_3 = Entry(frame_6, width=10, font=("Sans", 14))
ent_c6_3.pack(side=LEFT)

# Separator || Separator
line_down = Label(root, width=81, bg="blue")
line_down.place(x=60, y=310)

# Separator || Separator
line_down2 = Label(root, width=81, bg="blue")
line_down2.place(x=60, y=335)


## To display the computed GPA and Class
## To display the computed GPA and Class
label_g_n_c = Label(root, width=81, height=5, bg="indigo")
label_g_n_c.place(x=60, y=365)

gpa_text = Label(root, text="GPA:\nClass:", font=(
    "Helvetica", 15), bg="indigo", fg="#fff")
gpa_text.place(x=250, y=370)

# Separator || Separator
line_down3 = Label(root, width=81, bg="blue")
line_down3.place(x=60, y=455)

# Separator || Separator
line_down4 = Label(root, width=81, bg="blue")
line_down4.place(x=60, y=480)

# Separator || Separator || To shadow the buttons
line_down3 = Label(root, width=81, bg="indigo")
line_down3.place(x=60, y=510)
line_down4 = Label(root, width=81, bg="indigo")
line_down4.place(x=60, y=528)
# Separator || Separator || To shadow the buttons

# Buttons   || Buttons || QUit, Calculate and Reset
# Buttons   || Buttons || QUit, Calculate and Reset
frame_btn = Frame(root)
frame_btn.place(x=60, y=510)

# Quit button
btn_exit = Button(frame_btn, text="Quit", width=15 ,font=(
    "Sans", 14), bg="indigo", fg="#fff", command=root.quit)
btn_exit.pack(side=LEFT)

# Calculate button
btn_calc = Button(frame_btn, text="Calculate", width=19 ,font=(
    "Sans", 14), bg="indigo", fg="#fff", command=calculate)
btn_calc.pack(side=LEFT)

# Reset button
btn_reset = Button(frame_btn, text="Reset", width=15,font=(
    "Sans", 14), bg="indigo", fg="#fff", command=reset)
btn_reset.pack(side=LEFT)



if __name__ == "__main__":
    root.mainloop()