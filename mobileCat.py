import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter import Canvas, Entry, Text, Button, PhotoImage , Toplevel , Label,Menu,Menubutton,StringVar
from MysqlCode import Database

class mobileCategory:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"MobileCategory\assets\frame0")
    # ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\MobileCategory\assets\frame0")

    def relative_to_assets(self, path: str) -> Path:
        file_path = self.ASSETS_PATH / Path(path)
        if file_path.exists():
            return file_path
        else:
            print(f"Warning: File not found: {file_path}")
            return file_path 

    def __init__(self , parentApp):
        self.master = Toplevel()
        self.master.geometry("444x552")
        self.userId = 1
        self.db = Database()
        self.parentApp = parentApp
        self.setup_ui()

    def setup_ui(self):
        self.canvas = Canvas(
            self.master,
            bg = "#5C4D4D",
            height = 552,
            width = 444,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            444.8470153808594,
            552.0,
            fill="#D9D9D9",
            outline="#5C4D4D")

        image_details = [
            {"file": "image_1.png", "position": (224.1396484375, 299.7377624511719)},
            {"file": "image_2.png", "position": (122.2197265625, 101.484130859375)},
            {"file": "image_3.png", "position": (122.2197265625, 146.583251953125)},
            {"file": "image_4.png", "position": (122.2197265625, 191.6823272705078)},
            {"file": "image_5.png", "position": (154.2197265625, 236.7814178466797)},
            {"file": "image_6.png", "position": (225.012939453125, 326.9795837402344)},
            {"file": "image_7.png", "position": (147.2197265625, 281.8804931640625)},
        ]

        self.image_objects = {}

        for idx, details in enumerate(image_details):
            image_path = self.relative_to_assets(details["file"])
            self.image_objects[idx] = PhotoImage(file=image_path)
            canvas_image = self.canvas.create_image(
                details["position"][0],
                details["position"][1],
                image=self.image_objects[idx],
            )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            115,
            310,
            338,
            340,
            fill="white",
            outline="black")
        

        self.canvas.create_text(
            125,
            315,
            anchor="nw",
            text="SECURITY QUESTIONS",
            fill="#000000",
            font=("InknutAntiqua Regular", 18 * -1,'bold')
        )

        self.canvas.create_text(
            150.32470703125,
            20.18475341796875,
            anchor="nw",
            text="MOBILE",
            fill="#3E3333",
            font=("InknutAntiqua Regular", 33 * -1,'bold')
        )

        self.submit_button = Button(
            self.master,
            text="Submit",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 16),
            command=self.putdata,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0 
        )
        self.submit_button.place(
            x=164.8956298828125,
            y=486.2538146972656,
            width=104.98177337646484,
            height=30.222026824951172
        )

        self.imeiNo_textBox = Entry(
            self.master,
            bd=5,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("InknutAntiqua Regular", 10)
        )
        self.imeiNo_textBox.place(
            x=215.0706787109375,
            y=265.8774108886719,
            width=175.2248992919922,
            height=30.631393432617188
        )

        self.question1_textBox = Text(
            self.master,
            bd=5,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("InknutAntiqua Regular", 10)
        )
        self.question1_textBox.place(
            x=60,
            y=385,
            width=330,
            height=30
        )
        self.question2_textBox = Text(
            self.master,
            bd=5,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("InknutAntiqua Regular", 10)
        )
        self.question2_textBox.place(
            x=60,
            y=455,
            width=330,
            height=30
        )

        self.create_mobile_brand_menu()
        self.create_mobile_model_menu()
        self.create_mobile_color_menu()
        self.create_mobile_os_menu() 
        self.security_question1()
        self.security_question2()

    def security_question1(self):
        self.questions=["What is the name of your first pet?","What is the maiden name of your mother?","In what city were you born?","What is the name of your favorite teacher?","What is the make and model of your first car?"]
        
        self.selected_question1=StringVar(self.master)
        self.selected_question1.set(self.questions[0])

        self.create_menu_button(self.canvas,x=50,y=350,width=345,height=30,options=self.questions,var=self.selected_question1)

    def security_question2(self):
        self.questions= ["What is your favorite book or movie?","What was the name of your childhood best friend?","What is the name of the street you grew up on?","What is the name of your favorite fictional character?","What is your favorite food?"]
        
        self.selected_question2=StringVar(self.master)
        self.selected_question2.set(self.questions[0])

        self.create_menu_button(self.canvas,x=50,y=420,width=345,height=30,options=self.questions,var=self.selected_question2)       

    def create_mobile_brand_menu(self):
        self.brand_options =  ["None","Apple", "Samsung", "Huawei", "Xiaomi", "OnePlus", "Oppo", "Vivo", "Google (Pixel)", "Sony", "LG"]


        self.selected_mobile_brand=StringVar(self.master)
        self.selected_mobile_brand.set(self.brand_options[0])
        self.selected_mobile_brand.trace_add("write",self.udate_mobile_model_options)

        self.create_menu_button(self.canvas,x=210,y=85,width=150,height=30,options=self.brand_options,var=self.selected_mobile_brand)

    def create_mobile_model_menu(self):
        self.model_options= {
            "Apple": ["None","iPhone 13", "iPhone 12", "iPhone SE", "iPhone 11", "iPhone XR"],
            "Samsung": ["None","Galaxy S21", "Galaxy Note 20", "Galaxy A52", "Galaxy Z Fold", "Galaxy S20"],
            "Huawei": ["None","P40 Pro", "Mate 40", "Nova 7", "P30 Pro", "Mate Xs"],
            "Xiaomi": ["None","Mi 11", "Redmi Note 10", "Mi 10T", "Redmi K40", "POCO X3"],
            "OnePlus": ["None","OnePlus 9 Pro", "OnePlus 8T", "OnePlus Nord", "OnePlus 8 Pro", "OnePlus 7T"],
            "Oppo": ["None","Find X3 Pro", "Reno 5 Pro", "A74", "Reno 4 Pro", "F19 Pro"],
            "Vivo": ["None","X60 Pro", "V21 5G", "Y73", "X50 Pro", "V20 Pro"],
            "Google (Pixel)": ["None","Pixel 5", "Pixel 4a", "Pixel 4", "Pixel 3a", "Pixel 3"],
            "Sony": ["None","Xperia 1 III", "Xperia 5 III", "Xperia 10 III", "Xperia 1 II", "Xperia 5 II"],
            "LG": ["None","Wing", "V60 ThinQ", "G8 ThinQ", "V50 ThinQ", "G7 ThinQ"]
        }

        self.selected_mobile_model=StringVar(self.master)
        brand=self.selected_mobile_brand.get()

        if brand in self.model_options:
            self.selected_mobile_model.set(self.model_options.get(brand, ['None'])[0])
        else:
            self.selected_mobile_model.set("None")

        self.menu_model=self.create_menu_button(self.canvas,x=210,y=130,width=150,height=30,options=self.model_options.get(brand,['None']),var=self.selected_mobile_model)

    def udate_mobile_model_options(self, *args):
        selected_mobile_brand = self.selected_mobile_brand.get()
        new_model_options = self.model_options.get(selected_mobile_brand, ["None"])

        # Set the selected floor to "None" when building option changes
        self.selected_mobile_model.set("None")

        # Update the floor options in the menu
        self.menu_model.delete(0, "end")

        for floor in new_model_options:
            self.menu_model.add_command(label=floor, command=lambda f=floor: self.selected_mobile_model.set(f)) 

    def create_mobile_color_menu(self):
        laptop_colors = ["None","Black", "White", "Silver/Gray", "Gold", "Blue", "Red", "Green", "Pink/Rose Gold", "Purple", "Gradient/Color-shifting"]

        self.selected_mobile_color=StringVar(self.master)
        self.selected_mobile_color.set(laptop_colors[0])

        self.create_menu_button(self.canvas,x=210,y=175, width=150, height=30,options=laptop_colors,var=self.selected_mobile_color)   

    def create_mobile_os_menu(self):
        os_options = ["None","Android", "iOS", "HarmonyOS (Huawei)", "MIUI (Xiaomi)", "OxygenOS (OnePlus)", 
             "ColorOS (Oppo)", "Funtouch OS (Vivo)", "Realme UI (Realme)", "Stock Android", 
             "One UI (Samsung)", "LG UX (LG)", "Xperia UI (Sony)"]

        self.selected_mobile_os_option=StringVar(self.master)
        self.selected_mobile_os_option.set(os_options[0])

        self.create_menu_button(self.canvas,x=245,y=225, width=150, height=30,options=os_options,var=self.selected_mobile_os_option)   

               
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

    def show_mobile(self):
        self.master.wait_window(self.master)
    
    def putdata(self):
        c = self.db.insert_mobile_data(
            userId=self.userId,
            Brand=self.selected_mobile_brand.get(),
            model=self.selected_mobile_model.get(),
            color=self.selected_mobile_color.get(),
            operating_system=self.selected_mobile_os_option.get(),
            imei_number=self.imeiNo_textBox.get(),
            security_qustion1=self.selected_question1.get(),
            security_answer1=self.question1_textBox.get("1.0", "end-1c"),
            security_qustion2=self.selected_question2.get(),
            security_answer2=self.question2_textBox.get("1.0", "end-1c")
        )
        if c is True:
            # self.parentApp.label2.place(x=120, y=250, height=40, width=80)
            self.master.destroy()

if __name__=="__main__":
    master = tk.Tk()
    app = mobileCategory(master)
    master.mainloop()
