from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, Toplevel
import re
import bcrypt
import mysql.connector
from emailSender import sendEmail
import mymsgBox as messagebox
import login
import random
from MysqlCode import Database
from deviceRegisteration import deviceRegister
from createMysqlTables import MysqlTables


class Registration:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"Register\assets\frame0")
    # ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\Register\assets\frame0")

    def relative_to_assets(self, path: str) -> Path:
        file_path = self.ASSETS_PATH / Path(path)
        if file_path.exists():
            return file_path
        else:
            raise FileNotFoundError(f"File not found: {file_path}")

    def __init__(self, master):
        self.msg = messagebox.Rmsg()
        self.master = Toplevel()
        self.master.geometry("604x737")
        self.master.configure(bg="#FFFFFF")
        self.master.title("Registration")
        self.sendEmail = sendEmail
        self.db = Database()
        
        self.images = []

        self.setup_ui()
        self.random_otp = None

    def setup_ui(self):
        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=737,
            width=604,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(50.0,70.0,550.0,680.0,fill="#D9D9D9",outline="black")

        self.canvas.create_rectangle(60.0, 515.0, 540.0, 670, fill="#FFFFF0", outline="black")

        self.canvas.create_text(
            70,
            530,
            anchor="nw",
            text='''Welcome to Foundmate, where lost becomes
found!Join us on our mission to reunitelost
items with their rightful owners.
Register now and become a hero in our
community! THANKYOU''',
            fill="#000000",
            font=("InknutAntiqua Regular", 21 * -1,'bold')
        )

        
        elements = [
            {"text": "Name :-", "position": (100, 90)},
            {"text": "Email :-", "position": (100, 140)},
            {"text": "Mobile No :-", "position": (100, 190)},
            {"text": "Password :-", "position": (100, 240)},
            {"text": "Confirm Password", "position": (150, 290)},
            {"text": "Enter Otp :-", "position": (100, 420)}
        ]

        for elem in elements:
            self.canvas.create_text(
                *elem["position"],
                anchor="nw",
                text=elem["text"],
                fill="#000000",
                font=("InknutAntiqua Regular", 23 * -1)
            )

        self.Register_button = Button(
            self.master,
            text="Register",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 16),
            command=self.register,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0,  
            state="disabled"
        )
        self.Register_button.place(
            x=220,
            y=470,
            width=170,
            height=40
        )

        self.Send_otp = Button(
            self.master,
            text="Send Otp",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 16),
            command=self.send_otp_email,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0,  
            state="normal"
        )
        self.Send_otp.place(
            x=230,
            y=360,
            width=120,
            height=40
        )

        entry_elements = ["Name", "Email", "Mobile_No", "Password", "confirm_password", "Otp"]
        x_positions = [228, 228, 228, 228, 130, 230]
        y_positions = [90, 140, 190, 240, 320, 420]

        for i, elem in enumerate(entry_elements):
            bd_value = 3 if elem != "Otp" else 2
            font_size = 15 if elem == "Name" else 16
            show_value = "**" if elem in ["Password", "confirm_password"] else ""
            width = 310 if i != 5 else 100
            height = 30

            entry = Entry(
                self.master,
                bd=bd_value,
                bg="#FFFFFF",
                fg="#000716",
                highlightthickness=0,
                font=("InknutAntiqua Regular", font_size),
                show=show_value
            )
            entry.place(
                x=x_positions[i],
                y=y_positions[i],
                width=width,
                height=height
            )

            setattr(self, elem, entry)


        self.canvas.create_text(
            80,
            20,
            anchor="nw",
            text="REGISTER YOURSELF",
            fill="#000000",
            font=("InknutAntiqua Regular", 40 * -1,'bold')
        )

        self.verify_otp = Button(
            self.master,
            text="Verify Otp",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 16),
            command=self.verifed_cond,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0,  
            state="disabled"
        )
        self.verify_otp.place(
            x=350,
            y=415,
            width=150,
            height=40
        )

        self.show_hide_password_button = Button(
            self.master,
            text="Show/Hide Password",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 12),
            command=self.toggle_password_visibility,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0,  
        )
        self.show_hide_password_button.place(
            x=360,
            y=275,
            width=165,
            height=40
        )


        self.master.resizable(False, False)

    def verifed_cond(self):
        otp = self.Otp.get()
        global random_otp
        if otp == str(self.random_otp):
            self.verify_otp.config(text="Verified")
            self.Register_button.config(state="normal")
            self.Register_button.config(text="Registered")
        else:
            self.verify_otp.config(text="Not Verified")
            self.msg.ShowMsg("Incorrect Otp")

    def randomNumber(self):
        global random_otp
        random_otp = random.randint(100000, 999999)
        return random_otp


    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, email):
            if email.endswith("@gmail.com"):
                return True
            else:
                self.msg.ShowMsg('Email must end with @gmail.com')
                return False
        else:
             return False

    def check_password_strength(self, password):
   
        if len(password) < 8:
            return self.msg.ShowMsg("Password must be at least 8 characters long.")

        has_digit = any(char.isdigit() for char in password)
        has_upper = any(char.isupper() for char in password)  
        has_lower = any(char.islower() for char in password)
        has_special = any(char in '!@#$%^&*()-_=+[{]};:,.?/<>' for char in password)
        if not has_digit:
            return self.msg.ShowMsg("Passwords Must contains Atleast One  digit")
        if not has_upper:
            return self.msg.ShowMsg("Passwords Must contains Atleast One uppercase letter")
        if not has_lower:
            return self.msg.ShowMsg("Passwords Must contains Atleast One owercase letter")
        if not has_special:
            return self.msg.ShowMsg("Passwords Must contains Atleast One special character")
        return True


    def check_mobile_len(self, mobile):
        if len(mobile) != 10:
            return self.msg.ShowMsg("Mobile No must be 10 characters long.")

        if not mobile.isdigit():
            return self.msg.ShowMsg("Mobile No must be Consist of Digits only")
        
        return True
    

    def check_name_validity(self, name):

        if not name:
            return False

        if not re.match(r'^[a-zA-Z\s]+$', name):
            return self.msg.ShowMsg("Name  must contains only alphabetic characters and spaces.")

        if len(name) < 2:
            return self.msg.ShowMsg("Name  must contains at least 2 characters.")
        
        if len(name) > 50:
            return self.msg.ShowMsg("Name  must contains at most 50 characters")
        return True


    def send_otp_email(self):
        name = self.Name.get()
        email = self.Email.get()
        mobile = self.Mobile_No.get()
        password = self.Password.get()
        confirm_password_value = self.confirm_password.get()

        if not all([name, email, mobile, password, confirm_password_value]):
            self.msg.ShowMsg("All fields must be filled.")
            return
        
        if not self.check_name_validity(name):
            return

        if not self.validate_email(email):
            self.msg.ShowMsg("Invalid email format.")
            return

        if not self.check_mobile_len(mobile):
            return

        if not self.check_password_strength(password):
            return

        if password != confirm_password_value:
            self.msg.ShowMsg("Passwords do not match.")
            return
        global random_otp
        self.random_otp = self.randomNumber()
        self.sendEmail(email, "EmailVerification",
                       f"Hello {name}, the 6-digit OTP for verification is {random_otp}. This will be valid for 5 minutes.")
        self.msg.ShowMsg("Otp Has Been Sent To Your Email")
        self.verify_otp['state'] = 'normal'
        print(random_otp)

    def register(self):
        mysqlTables=MysqlTables()
        mysqlTables.create_all_table()

        name = self.Name.get()
        email = self.Email.get()
        mobile = self.Mobile_No.get()
        password = self.Password.get()
        confirm_password_value = self.confirm_password.get()

        if not all([name, email, mobile, password, confirm_password_value]):
            self.msg.ShowMsg("All fields must be filled.")
            return

        if not self.validate_email(email):
            self.msg.ShowMsg("Invalid email format.")
            return

        if not self.check_mobile_len(mobile):
            self.msg.ShowMsg("Mobile No must be 10 characters long.")
            return

        if not self.check_password_strength(password):
            self.msg.ShowMsg("Password must be at least 8 characters long.")
            return

        if password != confirm_password_value:
            self.msg.ShowMsg("Passwords do not match.")
            return
        hashed_password = self.hash_password(password)

        # Save user details to the MySQL database
        self.db.insert_user(name, email, mobile, hashed_password)

        self.msg.ShowMsg("Registration successful!")
        self.Register_button.config(text="Registered", state="disabled")
        self.master.destroy()

    def toggle_password_visibility(self):
        # Check if the password is currently hidden
        if self.Password.cget('show') == '':
            # If hidden, show the password
            self.Password.config(show='*')
            self.confirm_password.config(show='*')
        else:
            # If visible, hide the password
            self.Password.config(show='')
            self.confirm_password.config(show='')


    def showRegister(self):
        self.master.wait_window(self.master)

    def open_login_page(self):
        login_page = login.LoginPage(self.master)
        login_page.showLogin()
    

if __name__ == "__main__":
    master = Tk()
    app = Registration(master)
    master.mainloop()
