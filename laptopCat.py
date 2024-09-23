from pathlib import Path
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage , Toplevel,Menu,Menubutton,StringVar
from MysqlCode import Database

class laptopCategory:

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"LaptopCategory\assets\frame0")
    # ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\LaptopCategory\assets\frame0")

    def relative_to_assets(self, path: str) -> Path:
        file_path = self.ASSETS_PATH / Path(path)
        if file_path.exists():
            return file_path
        else:
            print(f"Warning: File not found: {file_path}")
            return file_path 
    def __init__(self,parentApp,userId):
        self.parentApp = parentApp
        self.master = Toplevel()
        self.master.geometry("445x552")
        self.userId = userId
        self.db = Database()
        self.setup_ui()

    def setup_ui(self):
        self.canvas = Canvas(
            self.master,
            bg = "#FFFFFF",
            height = 4450,
            width = 552,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            445.154541015625,
            552.381591796875,
            fill="#D9D9D9",
            outline="black")
        
        image_details = [
            {"file": "image_1.png", "position": (224.1396484375, 299.7377624511719)},
            {"file": "image_2.png", "position": (122.2197265625, 101.484130859375)},
            {"file": "image_3.png", "position": (122.2197265625, 146.583251953125)},
            {"file": "image_4.png", "position": (122.2197265625, 191.6823272705078)},
            {"file": "image_5.png", "position": (154.2197265625, 236.7814178466797)},
            {"file": "image_6.png", "position": (237.012939453125, 326.9795837402344)},#change
            {"file": "image_7.png", "position": (147.2197265625, 281.8804931640625)},
        ]

        self.image_objects = {}

        for idx, details in enumerate(image_details):
            image_path = self.relative_to_assets(details["file"])
            self.image_objects[idx] = PhotoImage(file=image_path)
            canvas_image = self.canvas.create_image(
                details["position"][0],
                details["position"][1],
                image=self.image_objects[idx]
            )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            125,
            310,
            348,
            340,
            fill="white",
            outline="black")

        self.canvas.create_text(
            135,
            315,
            anchor="nw",
            text="SECURITY QUESTIONS",
            fill="#000000",
            font=("InknutAntiqua Regular", 18 * -1,'bold')
        )

        self.canvas.create_text(
            137.419677734375,
            11.1925048828125,
            anchor="nw",
            text="LAPTOP",
            fill="#000000",
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
            x=165.009521484375,
            y=486.5899963378906,
            width=105.05435180664062,
            height=30.242919921875
        )

        self.serial_textBox = Text(
            self.master,
            bd=5,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("InknutAntiqua Regular", 10)
        )
        self.serial_textBox.place(
            x=229.20947265625,
            y=265.941650390625,
            width=163.41787719726562,
            height=30.651187896728516
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

        self.create_brand_menu()
        self.create_model_menu()
        self.create_color_menu()
        self.create_os_menu()
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

    def create_brand_menu(self):
        self.brand_options = ['None', 'Dell', 'HP', 'Lenovo', 'Asus', 'Acer', 'Apple', 'Microsoft', 'Samsung', 'MSI', 'Razer', 'Toshiba', 'LG', 'Huawei', 'Google (Pixelbook)', 'Fujitsu']


        self.selected_brand=StringVar(self.master)
        self.selected_brand.set(self.brand_options[0])
        self.selected_brand.trace_add("write",self.update_model_options)

        self.create_menu_button(self.canvas,x=210,y=85,width=150,height=30,options=self.brand_options,var=self.selected_brand)

    def create_model_menu(self):
        self.model_options= {
            "Dell": ['None',"XPS 13", "Inspiron 15", "Latitude 14", "Precision 15", "Alienware 17"],
            "HP": ['None',"HP Pavilion", "HP Envy", "HP Spectre", "HP EliteBook", "HP Omen"],
            "Lenovo": ['None',"ThinkPad X1 Carbon", "Yoga C940", "Ideapad 330", "Legion Y540", "ThinkBook 14"],
            "Asus": ['None',"ZenBook 14", "ROG Zephyrus G14", "VivoBook S15", "TUF Gaming A15", "Chromebook Flip C434"],
            "Acer": ['None',"Aspire 5", "Predator Helios 300", "Swift 3", "Chromebook Spin 713", "Nitro 5"],
            "Apple": ['None',"MacBook Air", "MacBook Pro"],
            "Microsoft": ['None',"Surface Laptop", "Surface Book", "Surface Pro", "Surface Go"],
            "Samsung": ['None',"Galaxy Book S", "Galaxy Book Flex", "Notebook 9 Pro"],
            "MSI": ['None',"GS66 Stealth", "Prestige 15", "GE75 Raider", "Alpha 15"],
            "Razer": ['None',"Razer Blade 15", "Razer Blade Stealth"],
            "Toshiba": ['None',"Portégé X30", "Satellite Radius 12"],
            "LG": ['None',"Gram 14"],
            "Huawei": ['None',"MateBook X Pro", "MateBook D"],
            "Google (Pixelbook)": ['None',"Pixelbook Go", "Pixelbook"],
            "Fujitsu": ['None',"LifeBook U Series", "Stylistic Q Series"]
        }

        self.selected_model=StringVar(self.master)
        brand=self.selected_brand.get()

        if brand in self.model_options:
            self.selected_model.set(self.model_options.get(brand, ['None'])[0])
        else:
            self.selected_model.set("None")

        self.menu_model=self.create_menu_button(self.canvas,x=210,y=130,width=150,height=30,options=self.model_options.get(brand,['None']),var=self.selected_model)

    def update_model_options(self, *args):
        selected_brand = self.selected_brand.get()
        new_model_options = self.model_options.get(selected_brand, ["None"])

        # Set the selected floor to "None" when building option changes
        self.selected_model.set("None")

        # Update the floor options in the menu
        self.menu_model.delete(0, "end")

        for floor in new_model_options:
            self.menu_model.add_command(label=floor, command=lambda f=floor: self.selected_model.set(f)) 

    def create_color_menu(self):
        laptop_colors = ['None','Black', 'Silver', 'Gray', 'White','Aluminum', 'Titanium', 'Brushed metal','Blue', 'Red', 'Green', 'Gold', 'Rose Gold','Limited edition colors', 'Collaboration designs', 'Artistic patterns','Various colors on the RGB spectrum','Different colors on the lid, keyboard area, and base','Carbon fiber finish', 'Soft-touch materials', 'Textured surfaces']

        self.selected_laptop_color=StringVar(self.master)
        self.selected_laptop_color.set(laptop_colors[0])

        self.create_menu_button(self.canvas,x=210,y=175, width=150, height=30,options=laptop_colors,var=self.selected_laptop_color)   

    def create_os_menu(self):
        os_options = ['None','Windows 10', 'Windows 8.1', 'Windows 7','macOS Monterey', 'macOS Big Sur', 'macOS Catalina','Ubuntu', 'Fedora', 'Debian', 'CentOS', 'Arch Linux', 'openSUSE','FreeBSD', 'OpenBSD','Chrome OS','Solaris', 'AIX','Haiku', 'ReactOS']

        self.selected_os_option=StringVar(self.master)
        self.selected_os_option.set(os_options[0])

        self.create_menu_button(self.canvas,x=245,y=225, width=150, height=30,options=os_options,var=self.selected_os_option)   

               
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

    def show_laptop(self):
        self.master.wait_window(self.master)
    
    def putdata(self):
            c = self.db.insert_laptop_data(
                userId=self.userId,
                Brand=self.selected_brand.get(),
                model=self.selected_model.get(),
                color=self.selected_laptop_color.get(), 
                operating_system=self.selected_os_option.get(),
                serial_number=self.serial_textBox.get("1.0", "end-1c"),
                security_qustion1=self.selected_question1.get(),
                security_answer1=self.question1_textBox.get("1.0", "end-1c"),
                security_qustion2=self.selected_question2.get(),
                security_answer2=self.question2_textBox.get("1.0", "end-1c")
            )
            if c is True:
                # self.parentApp.label1.place(x=120, y=250, height=40, width=80)
                self.master.destroy()


if __name__=="__main__":
    master = Tk()
    app=laptopCategory(master,2)
    master.mainloop()
