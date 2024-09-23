import mysql.connector
from pathlib import Path
import mymsgBox as msgbox
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, messagebox
import register 
import login 
from report import reportPage , Database
from chooseRequest import chooseRequestPage
import manual
from MysqlCode import Database
from deviceRegisteration import deviceRegister
from chooseReport import chooseReportPage

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Toplevel,Menu,Menubutton,StringVar

class reportWithID:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"ChooseReport\assets\frame0")

    def relative_to_assets(self, path: str) -> Path:
        file_path = self.ASSETS_PATH / Path(path)
        if file_path.exists():
            return file_path
        else:
            print(f"Warning: File not found: {file_path}")
            return file_path 
        
    def __init__(self,master,reported_id):
        self.master=Toplevel()
        self.master.geometry("495x355")
        self.master.configure(bg = "#FFFFFF")
        self.id = reported_id
        self.msg = msgbox.Rmsg()
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
            self.master,
            bg = "#FFFFFF",
            height = 355,
            width = 495,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            495.0,
            355.0,
            fill="#DBDBDB",
            outline="")

        self.canvas.create_rectangle(
            70.0,
            81.0,
            422.0,
            326.0,
            fill="#FFFFFF",
            outline="")

        self.submit_button = Button(
            self.master,
            text="Proceed",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 16),
            command=self.findUser,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0  ,  
        )
        self.submit_button.place(
            x=157.0,
            y=241.0,
            width=177.0,
            height=42.0
        )

        self.canvas.create_text(
            30.0,
            16.0,
            anchor="nw",
            text="REPORT WITH PRODUCT ID",
            fill="#000000",
            font=("InknutAntiqua Regular", 33 * -1,'bold')
        )

        self.canvas.create_text(
            115.0,
            95.0,
            anchor="nw",
            text='''ENTER PRODUCT ID 
            BELOW''',
            fill="#000000",
            font=("InknutAntiqua Medium", 25 * -1,'bold')
        ) 

        self.productId_textBox = Text(
            self.master,
            bd=5,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("InknutAntiqua Regular", 15)
        )
        self.productId_textBox.place(
            x=115,
            y=180,
            width=250,
            height=40
        )

    def findUser(self):
        victim_product_id = self.productId_textBox.get("1.0", "end-1c")
        reporter_product_id = self.id

        # if not reporter_product_id:
        #     self.msg.ShowMsg("Please Login First Before Submission")
        #     self.show_Login()
        #     return
        if not victim_product_id:
                self.msg.ShowMsg("Please Insert Victim Product Id To Process Further")
                return

        self.db.reportUsingId(victim_product_id , reporter_product_id )
        self.master.destroy()



    def showReportWithId(self):
        self.master.wait_window(self.master)

if __name__=="__main__":
    master = Tk()
    master.resizable(False, False)
    app=reportWithID(master,2)
    master.mainloop()

