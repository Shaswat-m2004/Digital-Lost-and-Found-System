from tkinter import Tk, Toplevel, Text, Scrollbar, Frame,Label

class requestsspage:
    def __init__(self, master):
        self.master = Toplevel()
        self.master.geometry("1031x733")
        self.master.configure(bg="#D9D9D9")
        self.master.title("Registration")
        self.setup_ui()

    def setup_ui(self):
        self.header_label = Label(
            self.master,
            text="USER MANUAL",
            bg="#FFFFFF",
            fg="#000000",
            font=("Arial", 25, "bold")
        )
        self.header_label.pack(pady=10)

        self.frame = Frame(self.master, bg="#D9D9D9")
        self.frame.pack(fill="both", expand=True)

        self.text_area = Text(
            self.frame,
            bg="#D9D9D9",  # Set the background color to match the rectangle
            wrap="word",
            bd=5,
            highlightthickness=0,
            relief="raised"
        )
        self.text_area.pack(side="left", fill="both", expand=True,padx=(20,0))

        self.scrollbar = Scrollbar(self.frame, orient="vertical", command=self.text_area.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.text_area.configure(yscrollcommand=self.scrollbar.set)

        self.text_area.insert("end", "USER MANUAL\n\n")
        self.text_area.insert("end"," "*40+'''Foundmate User Manual

1. Introduction

Foundmate is a software application designed to help users report lost items, request assistance for finding lost items, register their own valuables, and access various features to aid in the recovery of lost items. This manual provides an overview of the functionalities available in Foundmate and instructions on how to use them effectively.

2. Getting Started

To use Foundmate, follow these steps:

Installation: No installation is required. Simply run the provided script file to launch the application.

User Interface: Upon launching the application, you will be presented with the main interface, featuring several buttons for different functionalities.

3. Functionality

3.1. Register

Click on the "Register" button to create a new account. You will be prompted to enter your details such as name, email, mobile number, and password. Once registered, you can log in to access other features.

3.2. Login

Use the "Login" button to log in to your account. Enter your registered email and password to access your account. If you haven't registered yet, click on the "Register" button to create an account.

3.3. Report Lost Item

Click on the "Report" button to report a lost item. You will be prompted to provide details about the lost item, such as its description, location, and any relevant information. This information will help in the recovery process.

3.4. Request Assistance

If you need assistance in finding a lost item, click on the "Request" button. You will be guided through the process of requesting assistance, including providing details about the lost item and your contact information.

3.5. Print Product ID

To print a unique product ID for your registered valuables, click on the "Print ProductID" button. This ID can be used for identification and tracking purposes.

3.6. Device Registration

To register your valuables, click on the "Device Registration" button. You will be guided through the process of registering your valuables, including providing details such as product ID, description, and ownership information.

3.7. Access User Manual

Click on the "Manual" button to access the user manual for detailed instructions on using Foundmate's features. The manual provides information on each feature and how to use them effectively.

4. Conclusion

Foundmate offers a user-friendly interface and a range of features to assist users in recovering lost items. By following the instructions provided in this manual, you can make the most out of Foundmate and increase the chances of recovering your lost valuables.\n\n''' )

        self.text_area.insert("end", '''Manual for Registration Page
Introduction
The registration page of the Foundmate application allows users to create a new account by providing their personal information. This manual provides an overview of the features and functionalities of the registration page.

Features
Input Fields: Users can input their name, email, mobile number, password, confirm password, and OTP (One Time Password) for registration.
Email Verification: Users receive an OTP via email for verification before completing the registration process.
Password Strength Validation: Password strength is validated to ensure it meets certain criteria (minimum length, contains digits, uppercase and lowercase letters, and special characters).
Mobile Number Validation: Validates that the mobile number is exactly 10 digits and consists only of numeric characters.
Name Validation: Validates that the name contains only alphabetic characters and spaces, with a minimum length of 2 characters and a maximum length of 50 characters.
Registration Button: Allows users to submit their registration details.
Send OTP Button: Allows users to request an OTP for email verification.
Verify OTP Button: Allows users to verify the OTP entered for email verification.
Registration Successful Message: Displays a message upon successful registration.
Usage
Name Field: Enter your full name. It must contain only alphabetic characters and spaces, with a minimum length of 2 characters and a maximum length of 50 characters.
Email Field: Enter your email address. It must be in a valid format and end with "@gmail.com".
Mobile Number Field: Enter your mobile number. It must be exactly 10 digits long and consist only of numeric characters.
Password Field: Enter your desired password. It must meet certain criteria for strength (minimum length, contain digits, uppercase and lowercase letters, and special characters).
Confirm Password Field: Re-enter your password for confirmation. It must match the password entered in the previous field.
Send OTP Button: Click this button to request an OTP for email verification.
Verify OTP Field: Enter the OTP received in your email for verification. Click the "Verify OTP" button to proceed.
Register Button: Once all fields are filled correctly and the OTP is verified, click this button to complete the registration process.
Registration Successful Message: Upon successful registration, a message will be displayed confirming the registration.
Notes
Ensure all fields are filled correctly before submitting the registration details.
Password strength and email format are validated to enhance security.
OTP is sent via email for verification purposes to ensure the validity of the provided email address.
Mobile number and name are validated to ensure accuracy in user details.
Once registered, users can log in using their email and password on the login page. \n\n''')

        self.text_area.insert("end", ''' 
Manual for User Login Page
Introduction
The user login page of the Foundmate application allows registered users to log in to their accounts using their email address and password. This manual provides an overview of the features and functionalities of the user login page.

Features
Email Input Field: Users can enter their email address in the designated text box.
Password Input Field: Users can enter their password in the password text box.
Login Button: Allows users to submit their login credentials and access their account.
Forgot Password Button: Allows users to navigate to the forgot password page to reset their password.
Registration Button: Allows new users to navigate to the registration page to create a new account.
Usage
Email Input: Enter your registered email address in the provided text box.
Password Input: Enter your password in the password text box.
Login: Click the "Login" button to submit your login credentials and access your account.
Forgot Password: If you have forgotten your password, click the "Forgot Password" button to navigate to the password reset page.
Registration: If you are a new user, click the "Register" button to navigate to the registration page and create a new account.
Error Handling
Invalid Credentials: If the entered email address or password is incorrect, an error message will be displayed.
Empty Fields: If any of the fields are left empty, an error message will prompt the user to fill in all required fields.
Security
Password Encryption: User passwords are securely encrypted using the bcrypt hashing algorithm to ensure data security.
Database Access: User login credentials are verified against the database records stored securely on the server.
Navigation
Forgot Password Page: Clicking the "Forgot Password" button navigates the user to the forgot password page where they can reset their password.
Registration Page: Clicking the "Register" button navigates new users to the registration page where they can create a new account.
Compatibility
Browser Compatibility: The user login page is compatible with all modern web browsers, including Chrome, Firefox, Safari, and Edge.
Device Compatibility: The user login page is responsive and compatible with various devices, including desktops, laptops, tablets, and smartphones.
Troubleshooting
If you encounter any issues while logging in, please ensure:

Your email address and password are entered correctly.
Caps Lock is turned off as passwords are case-sensitive.
You have a stable internet connection.
You are using a compatible web browser.
If you forgot your password, use the "Forgot Password" feature to reset it.
For further assistance or inquiries, please contact our support team at support@foundmate.com.\n\n''')


    def showRequestss(self):
        self.master.wait_window(self.master)

if __name__ == "__main__":
    master = Tk()
    app = requestsspage(master)
    master.resizable(False, False)
    master.mainloop()
