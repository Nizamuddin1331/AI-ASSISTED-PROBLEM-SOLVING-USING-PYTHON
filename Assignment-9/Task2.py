# Define a class to represent a student at SRU

# Constructor to initialize student attributes
class SRU_Student:
    def __init__(self, name, roll_no, hostel_status):
        self.name = name                 # Student's name
        self.roll_no = roll_no           # Student's roll number
        self.hostel_status = hostel_status   # Whether the student stays in hostel (True/False)
        self.fee_paid = False            # Initial fee status (True/False)

    # Method to update fee status
    def fee_update(self, status):
        self.fee_paid = status           # Update fee status based on input (True/False)

    # Method to display student details
    def display_details(self):
        print("\n-- Student Details --")
        print(f"Name: {self.name}") 
        print(f"Roll No: {self.roll_no}") 
        print(f"Hostel Status: {'Yes' if self.hostel_status else 'No'}")
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")


# Take input from user to create a student object
name = input("Enter student's name: ")        # Ask for name
roll_no = input("Enter roll number: ")        # Ask for roll number

hostel_input = input("Is the student staying in hostel? (yes/no): ").strip().lower()
hostel_status = True if hostel_input == 'yes' else False   # Convert input to boolean

# Create an instance of SRU_Student with user input
student = SRU_Student(name, roll_no, hostel_status)

# Ask user to update fee status
fee_input = input("Has the student paid the fee? (yes/no): ").strip().lower()
fee_status = True if fee_input == 'yes' else False         # Convert input to boolean

student.fee_update(fee_status)     # Update fee status

# Display all student details
student.display_details()
