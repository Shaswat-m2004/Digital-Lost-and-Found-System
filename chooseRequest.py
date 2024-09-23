from registeredRequest import registeredRequestpage
from normalRequest import unregisteredRequest
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Toplevel,Menu,Menubutton,StringVar

class chooseRequestPage:
    OUTPUT_PATH = Path(__file__).parent
    # ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\ChooseReport\assets\frame0")
    ASSETS_PATH = OUTPUT_PATH / Path(r"ChooseReport\assets\frame0")

    def relative_to_assets(self, path: str) -> Path:
        file_path = self.ASSETS_PATH / Path(path)
        if file_path.exists():
            return file_path
        else:
            print(f"Warning: File not found: {file_path}")
            return file_path 
        
    def __init__(self,master,userId):
        self.master=Toplevel()
        self.master.geometry("495x355")
        self.master.configure(bg = "#FFFFFF")
        self.userId = userId
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

        self.proceed_button = Button(
            self.master,
            text="Proceed",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 16),
            command=self.open_selected_page,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0  
        )
        self.proceed_button.place(
            x=157.0,
            y=241.0,
            width=177.0,
            height=42.0
        )

        self.canvas.create_text(
            60.0,
            16.0,
            anchor="nw",
            text="CHOOSE CATAGEORY",
            fill="#000000",
            font=("InknutAntiqua Regular", 33 * -1,'bold')
        )

        self.canvas.create_text(
            105.0,
            95.0,
            anchor="nw",
            text="LOST ITEM CATEGORY ",
            fill="#000000",
            font=("InknutAntiqua Medium", 25 * -1,'bold')
        ) 

        self.create_catagory_menu()

    def create_catagory_menu(self):
        catagory_options = ["None", "Registered Item", "Unregistered Item"]
        self.selected_category_option=StringVar(self.master)
        self.selected_category_option.set(catagory_options[0])

        self.create_menu_button(self.canvas,x=160,y=140, width=170, height=40,options=catagory_options,var=self.selected_category_option)   


    def create_menu_button(self, master, x, y, width, height, options, var):
        menubutton = Menubutton(
            master,
            textvariable=var,
            font=("Helvetica", 12, "bold"),
            indicatoron=True,
            borderwidth=1,
            relief="ridge",
            bd=5,
            bg="#5C4D4D",
            fg="#DBDBDB"
        )
        menubutton.place(x=x, y=y, width=width, height=height)

        menu = Menu(menubutton, tearoff=False)
        menubutton["menu"] = menu

        for option in options:
            menu.add_command(label=option, command=lambda o=option: var.set(o))

        return menu
    
    def open_selected_page(self):
        selected_category=self.selected_category_option.get()
        self.master.destroy()

        if selected_category == "Registered Item":
            self.show_requestRegisteredDevice()

        elif selected_category == "Unregistered Item":
            self.show_requestUnRegisteredDevice()

        else:
            print("Invalid Category Selected")

        self.master.destroy()


    def showChooseRequest(self):
        self.master.wait_window(self.master)

    def show_requestRegisteredDevice(self):
        start_mobile =registeredRequestpage(self.master , self.userId)
        start_mobile.showrequestRegisteredDevice()

    def show_requestUnRegisteredDevice(self):
        start_others = unregisteredRequest(self.master,self.userId)
        start_others.showrequestUnRegisteredDevice()

if __name__=="__main__":
    master = Tk()
    master.resizable(False, False)
    app=chooseRequestPage(master,2)
    master.mainloop()
