# AI-Generated Comments (Typical Style)
# Create a class for SRU students
class SRU_Student:
    def __init__(self, self, name, roll_no, hostel_status):
        # Initialize student details
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee_paid = False

    def fee_update(self, status):
        # Update fee payment status
        self.fee_paid = status

    def display_details(self):
        # Print student information
        print("\n-- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Hostel Status: {'Yes' if self.hostel_status else 'No'}")
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")

# Get user input for student details
name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")

hostel_input = input("Is the student staying in hostel? (yes/no): ").strip().lower()
hostel_status = True if hostel_input == 'yes' else False

# Create student object
student = SRU_Student(name, roll_no, hostel_status)

# Get fee status input
fee_input = input("Has the student paid the fee? (yes/no): ").strip().lower()
fee_status = True if fee_input == 'yes' else False

student.fee_update(fee_status)

# Display student details
student.display_details()
