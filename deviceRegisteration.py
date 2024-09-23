from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Toplevel , Label
# import mymsgBox as messagebox
from laptopCat import laptopCategory
from othersCat import othersCategory
from mobileCat import mobileCategory
from MysqlCode import Database


class deviceRegister:

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"DeviceRegisteration\assets\frame0")
    # ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\DeviceRegisteration\assets\frame0")

    def relative_to_assets(self, path: str) -> Path:
        file_path = self.ASSETS_PATH / Path(path)
        if file_path.exists():
            return file_path
        else:
            print(f"Warning: File not found: {file_path}")
            return file_path 
        
    def __init__(self,userId):
        # self.msg=messagebox.Rmsg()
        self.master = Toplevel()
        self.master.geometry("706x416")
        self.master.configure(bg = "#FFFFFF")
        self.master.title("Registration")
        self.db = Database()

        self.userId = userId
       
        self.setup_ui()

    def setup_ui(self):
        self.canvas = Canvas(
            self.master,
            bg = "#FFFFFF",
            height = 416,
            width = 706,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            706.0,
            416,
            fill="#D9D9D9",
            outline="black")

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            352,
            228,
            image=self.image_image_1
        )

        button_details = [
            {"text": "Laptop", "command": self.show_laptop, "x": 87},
            {"text": "Mobile", "command": self.show_mobile, "x": 286},
            {"text": "Others", "command": self.show_others, "x": 484},
        ]

        for button_detail in button_details:
            btn = Button(
                self.master, 
                text=button_detail["text"],
                bg="#5C4D4D",
                fg="#FFFFFF",
                font=("InknutAntiqua Regular", 16),
                command=button_detail["command"],
                relief="raised", 
                bd=5,  
                padx=10, 
                pady=5,  
                activebackground="#7F6E6E",
                activeforeground="#000000",
                highlightthickness=0 
            )
            btn.place(
                x=button_detail["x"],
                y=196,
                width=142,
                height=48
            )


        self.canvas.create_text(
            140,
            25,
            anchor="nw",
            text="DEVICE REGISTRATION",
            fill="#3E3333",
            font=("InknutAntiqua Regular", 37 * -1, 'bold')
        )

        # self.label1 = Label(
        #     self.master,
        #     text = "Done",
        #     # bg = "#5C4D4D",
        #     fg = "#5C4D4D",
        #     font=("InknutAntiqua Regular", 12, "bold")
        # )
        # self.label2 = Label(
        #     self.master,
        #     text = "Done",
        #     # bg = "#5C4D4D",
        #     fg = "#5C4D4D",
        #     font=("InknutAntiqua Regular", 12, "bold")
        # )
        # self.label3 = Label(
        #     self.master,
        #     text = "Done",
        #     # bg = "#5C4D4D",
        #     fg = "#5C4D4D",
        #     font=("InknutAntiqua Regular", 12, "bold")
        # )       
 
    def show_laptop(self):
        name = 'laptop'
        if self.db.check_already(self.userId,name):
            self.laptop = laptopCategory(self,self.userId)
            self.laptop.userId = self.userId
            self.master.destroy()
            self.laptop.show_laptop()

    def show_mobile(self):
        name = 'mobile'
        if self.db.check_already(self.userId,name):
            self.mobile = mobileCategory(self)
            self.mobile.userId = self.userId
            self.master.destroy()
            self.mobile.show_mobile()

    def show_others(self):
        name = 'other'
        if self.db.check_already(self.userId,name):
            self.other = othersCategory(self,self.userId)
            self.other.userId = self.userId
            self.master.destroy()
            self.other.show_others()

    def show_DR(self):
        self.master.wait_window(self.master)
        print("from dr" , self.userId)
        
if __name__=="__main__":
    master = Tk()
    master.resizable(False, False)
    app=deviceRegister(1)
    master.mainloop()
