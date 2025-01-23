class Student:
    college = "Sukkur IBA University"

    def __init__(self, name, CMS_ID, cgpa):
        self.name = name
        self.CMS_ID = CMS_ID
        self.cgpa = cgpa

    def previous_semester_CGPA(self, cgpa):
        return cgpa

    def subject_cgpa(self, marks, credit_hours):
        # Consolidated GPA calculation logic to avoid repetition
        if marks >= 93:
            return 4 * credit_hours
        elif 87 <= marks < 93:
            return 3.67 * credit_hours
        elif 84 <= marks < 87:
            return 3.33 * credit_hours
        elif 77 <= marks < 84:
            return 3 * credit_hours
        elif 74 <= marks < 77:
            return 2.67 * credit_hours
        elif 67 <= marks < 74:
            return 2.33 * credit_hours
        elif 64 <= marks < 67:
            return 2.11 * credit_hours
        elif 60 <= marks < 64:
            return 1.67 * credit_hours
        else:
            return 0 * credit_hours
    def Pr_cgpa(self, marks, credit_hours):
        # Consolidated GPA calculation logic to avoid repetition
        if marks >= 46:
            return 4 * credit_hours
        elif 44 <= marks < 46:
            return 3.67 * credit_hours
        elif 42 <= marks < 44:
            return 3.33 * credit_hours
        elif 39 <= marks < 44:
            return 3 * credit_hours
        elif 37 <= marks < 39:
            return 2.67 * credit_hours
        elif 35 <= marks < 37:
            return 2.33 * credit_hours
        elif 33 <= marks < 35:
            return 2.11 * credit_hours
        elif 30 <= marks < 33:
            return 1.67 * credit_hours
        else:
            return 0 * credit_hours

    def calculate_final_cgpa(self, marks_list, prectical_marks, credit_hours_list, previous_cgpa):
    # Calculate points for theory subjects
        total_theory_points = sum(
        [self.subject_cgpa(marks, hours) for marks, hours in zip(marks_list, credit_hours_list[:len(marks_list)])]
        )
    
    # Calculate points for practical subjects
        total_practical_points = sum(
        [self.Pr_cgpa(marks, hours) for marks, hours in zip(prectical_marks, credit_hours_list[len(marks_list):])]
        )
    
    # Total points and credit hours
        total_points = total_theory_points + total_practical_points
        total_credit_hours = sum(credit_hours_list)
    
    # Calculate current GPA and final CGPA
        current_gpa = total_points / total_credit_hours
        final_cgpa = (current_gpa + previous_cgpa) / 2
        return final_cgpa


    def display(self):
        print(f"Student Name: {self.name}")
        print(f"CMS ID: {self.CMS_ID}")
        print(f"CGPA: {self.cgpa:.2f}")

# Main method
def main():
    # Create a student instance
    name = input("Enter student's name: ")
    CMS_ID = input("Enter CMS ID: ")
    cgpa = float(input("Enter previous semester CGPA: "))
    student = Student(name, CMS_ID, cgpa)

    # Input marks and credit hours for each subject
    marks_list = []
    credit_hours_list = []
    prectical_marks=[]
    subjects = int(input("Enter the number of subjects: "))
    pr=int(input("Enter Your pricticals : "))
    for i in range(subjects):
        marks = float(input(f"Enter marks for subject {i + 1}: "))
        credit_hours = float(input(f"Enter credit hours for subject {i + 1}: "))
        marks_list.append(marks)
        credit_hours_list.append(credit_hours)
    
    for i in range(pr):
        mark=float(input(f"Enter marks for subject {i + 1}: "))
        credit_hours=float(input(f"Enter credit hours for subject {i + 1}: "))
        prectical_marks.append(mark)
        credit_hours_list.append(credit_hours)

    # Calculate final CGPA
    final_cgpa = student.calculate_final_cgpa(marks_list,prectical_marks, credit_hours_list, cgpa)

    # Display student details and final CGPA
    student.cgpa = final_cgpa  # Update CGPA
    student.display()

# Entry point
if __name__ == "__main__":
    main()
