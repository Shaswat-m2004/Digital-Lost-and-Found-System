import mysql.connector
from pathlib import Path
import mymsgBox as msgbox
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, messagebox,Frame
import register 
import login 
from report import reportPage , Database
from chooseRequest import chooseRequestPage
import manual
from MysqlCode import Database
from deviceRegisteration import deviceRegister
from chooseReport import chooseReportPage
from downloadPID import downloadID
from reporttypes import reportType

class Foundmate:
    ASSETS_PATH = Path(r"HomePage\assets\frame0")
    # ASSETS_PATH = Path(r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\HomePage\assets\frame0")

    def relative_to_assets(self, path: str) -> Path:
        file_path = self.ASSETS_PATH / Path(path)
        if file_path.exists():
            return file_path
        else:
            print(f"Warning: File not found: {file_path}")
            return file_path
        
    def __init__(self, window):
        self.msg = msgbox.Rmsg()
        self.window = window
        self.logged_in = False
        self.victim_name = None
        self.victim_email = None
        self.reporter_name = None
        self.reporter_mobile = None
        self.reporter_product_id = None
        self.userId = None
        self.db = Database()
        self.images = []
        
        self.setup_ui()


    def setup_ui(self):
        self.canvas = Canvas(
            self.window,
            bg="#ECECEC",
            height=708,
            width=996,
            bd=5,
            highlightthickness=5,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        buttons_info = [
            ("Manual", self.show_requestss, 371, 610),
            ("Report", self.show_reportType, 371, 480),
            ("Request", self.show_request, 15, 510),
            ("Print ProductID", self.show_downloadPID, 650, 300)
        ]

        for text, command, x, y in buttons_info:
            btn = Button(
                text=text,
                bg="#5C4D4D",
                fg="#FFFFFF",
                font=("InknutAntiqua Regular", 16),
                command=command,
                relief="raised", 
                bd=5,  
                padx=10, 
                pady=5,  
                activebackground="#7F6E6E",
                activeforeground="#000000",
                highlightthickness=0 
            )

            btn.place(x=x, y=y, width=218, height=57)
    

        self.canvas.create_rectangle(0.0, 0.0, 996.0, 379, fill="#ECECEC", outline="black")

        images_info = [
            ("image_1.png", 117, 635),
            # ("image_2.png", 480, 543),
            ("image_3.png", 274, 186),
            ("image_4.png", 755, 188),
            ("image_5.png", 875, 542)
        ]

        for image_path, x, y in images_info:
            image = PhotoImage(file=self.relative_to_assets(image_path))
            self.images.append(image)  
            self.canvas.create_image(x, y, image=image)

        self.Login = Button(
            text="Login",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 16),
            command=self.show_Login,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0 
        )
        self.Login.place(x=730, y=520, width=120, height=45)

        self.Register = Button(
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
        self.Register.place(x=860, y=520, width=120, height=45)

        frame = Frame(self.window, highlightbackground="black", highlightthickness=2)
        frame.place(x=20, y=20, width=110, height=30)

        self.unique_id_label = Label(
            frame,
            text="",
            font=("InknutAntiqua Regular", 14),
            bg="#FFFFFF",
            fg="#000000",
        )
        self.unique_id_label.pack(fill="both", expand=True)

        self.DeviceRegister_button = Button(
            # self.master,
            text="Device Registration",
             bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 16),
            command=self.openDR,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0 
        )
        self.DeviceRegister_button.place(
            x=200,
            y=20,
            width=250,
            height=32
        )
        self.canvas.create_rectangle(710.0, 385.0, 250.0, 700, fill="#FFFFF0", outline="black")
        self.canvas.create_rectangle(650.0, 180.0, 870.0, 280, fill="#FFFFF0", outline="black")
        self.canvas.create_rectangle(730.0, 400.0, 990.0, 500, fill="#FFFFF0", outline="black")
        self.canvas.create_rectangle(150.0, 60.0, 500.0, 150, fill="#FFFFF0", outline="black")
        self.canvas.create_rectangle(20.0, 385.0, 240.0, 500, fill="#FFFFF0", outline="black")

        self.canvas.create_text(
            30,
            395,
            anchor="nw",
            text='''Reclaim lost items
            now!
    Tap below to 
      REQUEST''',
            fill="#000000",
            font=("InknutAntiqua Regular", 21 * -1,'bold')
        )

        self.canvas.create_text(
            170,
            70,
            anchor="nw",
            text=''' Secure your valuables ahead!
        Tap the button above
        to register them now.''',
            fill="#000000",
            font=("InknutAntiqua Regular", 21 * -1,'bold')
        )

        self.canvas.create_text(
            770,
            410,
            anchor="nw",
            text=''' Guidance awaits!
Tap below to login
      or register
            ''',
            fill="#000000",
            font=("InknutAntiqua Regular", 21 * -1,'bold')
        )

        self.canvas.create_text(
            670,
            200,
            anchor="nw",
            text='''Discover your ID!
    Click to print.
            ⇩''',
            fill="#000000",
            font=("InknutAntiqua Regular", 22 * -1,'bold')
        )

        self.canvas.create_text(
            290,
            406,
            anchor="nw",
            text='''IF YOU WANT TO REPORT A LOST ITEM 
THEN CLICK THE BUTTON BELOW''',
            fill="#000000",
            font=("InknutAntiqua Regular", 20 * -1,'bold')
        )

        self.canvas.create_text(
            270,
            550,
            anchor="nw",
            text='''CLICK THE BUTTON BELOW TO ACCESS
THE MANUAL FOR DETAILED INSTRUCTIONS''',
            fill="#000000",
            font=("InknutAntiqua Regular", 20 * -1,'bold')
        )    

    def show_register(self):
        start_register = register.Registration(self.window)
        start_register.showRegister()

    def show_Login(self):

        start_login = login.LoginPage(self)
        start_login.showLogin()


        if  self.userId is None:
            
            return
        else:
            self.unique_id_label.config(text = self.reporter_product_id)
            print(self.userId)

    def show_report(self):
        if self.userId is not None:
            start_report = chooseReportPage(self.window , self.userId)
            start_report.showChooseReport()
        else:
            messagebox.showwarning("title", "Please Login First")
            self.show_Login()
            return

    def show_request(self):
        if self.userId is not None:
            start_request = chooseRequestPage(self.window , userId=self.userId)
            start_request.showChooseRequest()
        
        else:
            messagebox.showwarning("title", "Please Login First")
            self.show_Login()
            return

    def show_requestss(self):
        if self.userId is not None:
            start_requestss = manual.requestsspage(self.window)
            start_requestss.showRequestss()
        else:
            messagebox.showwarning("title", "Please Login First")
            self.show_Login()
            return
        
    def show_reportType(self):
        if self.userId is not None:
            start_showReport = reportType(self.window, self.userId ,self.unique_id_label.cget('text'))
            start_showReport.showReportType()
        else:
            messagebox.showwarning("title", "Please Login First")
            self.show_Login()
            return
        
    # def findUser(self):
    #         victim_product_id = self.id_textBox.get()
    #         reporter_product_id = self.unique_id_label.cget('text')

    #         if not reporter_product_id:
    #             self.msg.ShowMsg("Please Login First Before Submission")
    #             self.show_Login()
    #             return
    #         if not victim_product_id:
    #                 self.msg.ShowMsg("Please Insert Victim Product Id To Process Further")
    #                 return

    #         self.db.reportUsingId(victim_product_id , reporter_product_id )







    def show_downloadPID(self):
        if self.userId is not None:
            start_download = downloadID(self.window,self.reporter_product_id)
            start_download.showDownloadPID()
        else:
            messagebox.showwarning("title", "Please Login First")
            self.show_Login()
            return

    def openDR(self):
        if self.userId is not None:
            self.DR = deviceRegister(self.userId)
            self.DR.userId = self.userId
            self.DR.show_DR()
        else:
            messagebox.showwarning("title", "Please Login First")
            self.show_Login()
            return

if __name__ == "__main__":

    window = Tk()
    window.geometry("996x708")
    window.configure(bg="#FFFFFF")
    window.resizable(True, True)
    foundmate_instance = Foundmate(window)
    window.mainloop()
