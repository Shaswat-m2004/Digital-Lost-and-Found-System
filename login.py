
import mymsgBox as messagebox
import register 
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Toplevel
import mysql.connector
import bcrypt
from MysqlCode import Database
import forgotPassword as fp

class LoginPage:
    OUTPUT_PATH = Path(__file__).parent
    # ASSETS_PATH = OUTPUT_PATH / Path(r"Login/assets/frame0")
    ASSETS_PATH = OUTPUT_PATH / Path(r"Login/assets/frame0")

    def relative_to_assets(self, path: str) -> Path:
        file_path = self.ASSETS_PATH / Path(path)
        if file_path.exists():
            return file_path
        else:
            print(f"Warning: File not found: {file_path}")
            return file_path  # You can return the path even if it doesn't exist

    def __init__(self,parent_app):
        self.msg=messagebox.Rmsg()
        self.master=Toplevel()
        self.parent_app = parent_app
        self.master.geometry("604x570")
        self.master.configure(bg="#FFFFFF")
        self.master.title("Registration")
        self.db = Database()
        # self.callback=callback
        self.userId = None
        self.setup_ui()

    def setup_ui(self):
        self.canvas = Canvas(
        self.master,
        bg = "#FFFFFF",
        height = 670,
        width = 603,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.canvas.create_text(
            180.0,
            10.0,
            anchor="nw",
            text="USER LOGIN",
            fill="#000000",
            font=("Arial", 25, "bold")
        )
        self.canvas.create_rectangle(50.0,60.0,550.0,520.0,fill="#D9D9D9",outline="black")

        self.canvas.create_text(
            225.0,
            410.0,
            anchor="nw",
            text="New here?",
            fill="#000000",
            font=("Arial", 22, "bold")
        )

        self.Register_button = Button(
            self.master,
            text="Register",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 16),
            command=self.show_register,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0  
        )
        self.Register_button.place(
            x=202,
            y=450,
            width=178,
            height=53
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
            x=210,
            y=300,
            width=165,
            height=40
        )

        self.canvas.create_text(
            170.0,
            90.0,
            anchor="nw",
            text="Enter Your Email Id",
            fill="#000000",
            font=("InknutAntiqua Regular", 20)
        )
        self.Email_TextBox = Text(
            self.master,
            bd=5,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("InknutAntiqua Regular", 18)
        )
        self.Email_TextBox.place(
            x=100.02630615234375,
            y=130.7519226074219,
            width=400.47369384765625,
            height=50.91130447387695
        )

        self.canvas.create_text(
            170.0,
            200.0,
            anchor="nw",
            text="Enter Your Password",
            fill="#000000",
            font=("InknutAntiqua Regular", 20)
        )

        self.Password_TextBox = Entry(
            self.master,
            bd=5,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("InknutAntiqua Regular", 18),
            show='*'
        )
        self.Password_TextBox.place(
            x=100.26318359375,
            y=240.5992431640625,
            width=400.47369384765625,
            height=50.91130447387695
        )

        self.Login = Button(
                self.master,
            text="Login",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 16),
            command=self.login,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0   
        )
        self.Login.place(
            x=100,
            y=350,
            width=178,
            height=53
        )

        self.forgot_password = Button(
            self.master,
            text="Forgot Password",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 16),
            command=self.show_forgotpass,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0  
        )
        self.forgot_password.place(
            x=300.0,
            y=350.0,
            width=200.0,
            height=53.0
        )

    def login(self):
        email = self.Email_TextBox.get("1.0", "end-1c")
        password = self.Password_TextBox.get()
        result = self.db.login(email,password)
        self.userId = result
        self.parent_app.userId = self.userId
        # self.parent_app.reporter_product_id = result[1]
        if self.userId is not None:
            data = self.db.getMydata((self.userId,))
            self.parent_app.reporter_product_id = data[5]
            self.master.destroy()

    def toggle_password_visibility(self):
        # Check if the password is currently hidden
        if self.Password_TextBox.cget('show') == '':
            # If hidden, show the password
            self.Password_TextBox.config(show='*')
        else:
            # If visible, hide the password
            self.Password_TextBox.config(show='')


    def showLogin(self):
        self.master.wait_window(self.master)
        
    def show_forgotpass(self):
        start_wallet=fp.forgotPasswordPage(self.master)
        start_wallet.showForgotPass()

    def show_register(self):
        start_register=register.Registration(self.master)
        start_register.showRegister()
        self.master.destroy()


if __name__=="__main__":
    master = Tk()
    app=LoginPage(master)
    master.mainloop()
