from reportLaptop import reportLaptopPage
from reportMobile import reportMobilePage
from reportOthers import reportOthersPage
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Toplevel,Menu,Menubutton,StringVar
from chooseReport import chooseReportPage
from reportWithId import reportWithID


class reportType:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"ChooseReport\assets\frame0")

    def relative_to_assets(self, path: str) -> Path:
        file_path = self.ASSETS_PATH / Path(path)
        if file_path.exists():
            return file_path
        else:
            print(f"Warning: File not found: {file_path}")
            return file_path 
        
    def __init__(self,master,userId,pid):
        self.master = master
        self.master=Toplevel()
        self.master.geometry("495x355")
        self.master.configure(bg = "#FFFFFF")
        self.userId=userId
        self.product_id = pid
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
            100.0,
            16.0,
            anchor="nw",
            text="MAKE A REPORT",
            fill="#000000",
            font=("InknutAntiqua Regular", 33 * -1,'bold')
        )

        self.canvas.create_text(
            130.0,
            95.0,
            anchor="nw",
            text="TYPE OF REPORT",
            fill="#000000",
            font=("InknutAntiqua Medium", 25 * -1,'bold')
        ) 

        self.create_report_type()

    def create_report_type(self):
        report_options = ["None", "ReportWith ID", "Report Without ID"]
        self.selected_report_option=StringVar(self.master)
        self.selected_report_option.set(report_options[0])

        self.create_menu_button(self.canvas,x=160,y=140, width=170, height=40,options=report_options,var=self.selected_report_option)   


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
        selected_category=self.selected_report_option.get()
        self.master.destroy()

        if selected_category == "ReportWith ID":
            self.show_reportWithId()
            print("Selected ReportWith ID")

        elif selected_category == "Report Without ID":
            self.show_report()
        else:
            print("Invalid Category Selected")
            self.master.destroy()



    def showReportType(self):
        self.master.wait_window(self.master)

    def show_report(self):
        start_report = chooseReportPage(self.master , self.userId)
        start_report.showChooseReport()

    def show_reportWithId(self):
        start_report = reportWithID(self.master , self.product_id)
        start_report.showReportWithId()

if __name__=="__main__":
    master = Tk()
    master.resizable(False, False)
    app=reportType(master,2)
    master.mainloop()
