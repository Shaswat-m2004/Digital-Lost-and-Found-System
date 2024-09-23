from pathlib import Path
from tkinter import Tk, Canvas, Text, Button, Toplevel
import mysql.connector
import mymsgBox 
import emailSender
import random
from MysqlCode import Database
import bcrypt

class forgotPasswordPage:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"ForgotPassword\assets\frame0")
    # ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\ForgotPassword\assets\frame0")

    def relative_to_assets(self, path: str) -> Path:
        file_path = self.ASSETS_PATH / Path(path)
        if file_path.exists():
            return file_path
        else:
            print(f"Warning: File not found: {file_path}")
            return file_path

    def __init__(self, master):
        self.master = Toplevel()
        self.msg = mymsgBox.Rmsg()
        self.master.geometry("1001x519")
        self.master.configure(bg="#DBDBDB")
        self.master.title("Login")
        self.db = Database()
        self.verified = False
        self.setup_ui()

    def setup_ui(self):
        self.random_otp = None

        self.canvas = Canvas(
            self.master,
            bg="#DBDBDB",
            height=519,
            width=1001,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        elements = [
            {"type": "text", "text": "Forgotten Password", "position": (240.98147583007812, 0.0), "font": ("InknutAntiqua Regular", 49)},
            {"type": "text", "text": "New Password", "position": (692.0494384765625, 108.1326904296875), "font": ("InknutAntiqua Regular", 27)},
            {"type": "text", "text": "Email", "position": (37.0740966796875, 108.1326904296875), "font": ("InknutAntiqua Regular", 27)},
            {"type": "text", "text": "Confirm Password", "position": (664.243896484375, 234.802490234375), "font": ("InknutAntiqua Regular", 27)},
        ]

        for element in elements:
            self.canvas.create_text(*element["position"], anchor="nw", text=element["text"], fill="#000000", font=element["font"])

        self.textboxes = []

        textbox_positions = [
            (661.1543579101562, 159.19134521484375),
            (145.20684814453125, 100.31173706054688),
            (661.1543579101562, 305.861083984375),
            (60.20758056640625, 320.3531188964844)
        ]

        for position in textbox_positions:
            textbox = Text(
                self.master,
                bd=5,
                bg="#FFFFFF",
                fg="#000716",
                highlightthickness=0,
                font=("InknutAntiqua Regular", 24),
            )
            textbox.place(x=position[0], y=position[1], width=284.23455810546875, height=56.70062255859375)
            self.textboxes.append(textbox)

        self.verify_button = Button(
            self.master,
            text="Verify",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 20,'bold'),
            command=self.verify_email,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0  
        )
        self.verify_button.place(x=253.33941650390625, y=170.81790161132812, width=197.72837829589844, height=74.14814758300781)

        self.verifyOtp_button = Button(
              self.master,
            text="Verify Otp",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 20,'bold'),
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
        self.verifyOtp_button.place(x=110.7839660644531, y=390.63580322265625, width=169.92283630371094, height=60.23765563964844)

        self.Submit_button = Button(
            self.master,
            text="Submit",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 20,'bold'),
            command=self.update_password,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0, 
            state="disabled"
        )
        self.Submit_button.place(x=475.7839660644531, y=401.63580322265625, width=169.92283630371094, height=77.23765563964844)

    def verify_email(self):
        email = self.textboxes[1].get("1.0", "end-1c")
        if  self.db.checkMail(email):
            self.random_otp = random.randint(100000, 999999)
            subject = '''
                    Verification Email from Foundmate
                '''
            
            content = f'''
                    This Mail is regarding change password on Foundmate Platform
                    the ONE TIME PASSWORD for changing the password is {self.random_otp}
                '''
            
            emailSender.sendEmail(to_whom = email, subject = subject, content = content)
            self.verifyOtp_button.config(state="normal")

    def verifed_cond(self):
        entered_otp = self.textboxes[3].get("1.0", "end-1c")
        print(entered_otp , self.random_otp)

        if int(entered_otp) == int(self.random_otp):
            self.msg.ShowMsg("OTP verified \n Enter New Password")
            self.Submit_button.config(state="normal")
            self.verify_button.config(state="disabled")
            self.verifyOtp_button.config(state="disabled")


    def update_password(self):
        new_password = self.textboxes[2].get("1.0", "end-1c")
        email = self.textboxes[1].get("1.0", "end-1c")
        if self.db.changePassword(email , new_password):
            self.Submit_button.config(text="Submited")
            self.master.destroy()
        

    def showForgotPass(self):
        self.master.wait_window(self.master)

if __name__ == "__main__":
    master = Tk()
    master.resizable(False, False)
    db = Database()
    app = forgotPasswordPage(master)
    master.mainloop()
    db.close_connection()
