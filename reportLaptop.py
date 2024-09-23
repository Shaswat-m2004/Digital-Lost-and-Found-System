from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Toplevel,Menu,Menubutton,StringVar
from MysqlCode import Database
from reportInsertion import DatabaseManager
import mymsgBox as messagebox

class reportLaptopPage:
    OUTPUT_PATH = Path(__file__).parent
    # ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\ReportLaptop\assets\frame0")
    ASSETS_PATH = OUTPUT_PATH / Path(r"ReportLaptop\assets\frame0")

    def relative_to_assets(self, path: str) -> Path:
        file_path = self.ASSETS_PATH / Path(path)
        if file_path.exists():
            return file_path
        else:
            print(f"Warning: File not found: {file_path}")
            return file_path 
        
    def __init__(self,master,userId):
        self.master=Toplevel()
        self.master.geometry("445x783")
        self.master.configure(bg = "#FFFFFF")
        self.userId = userId
        self.msg = messagebox.Rmsg()
        self.ri = DatabaseManager(self.userId)
        self.db = Database()

        self.setup_ui()

    def setup_ui(self):
        self.canvas = Canvas(
            self.master,
            bg = "#FFFFFF",
            height = 783,
            width = 445,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            445.452880859375,
            783.6573486328125,
            fill="#D9D9D9",
            outline="black")
        
        image_details = [
            {"file": "image_1.png", "position": (224, 405)},
            {"file": "image_2.png", "position": (122, 96)},
            {"file": "image_3.png", "position": (142, 375)},
            {"file": "image_4.png", "position": (122, 146)},
            {"file": "image_5.png", "position": (122, 191)},
            {"file": "image_6.png", "position": (329, 375)},
            {"file": "image_7.png", "position": (225, 470)},
            {"file": "image_8.png", "position": (218, 327)},
            {"file": "image_10.png", "position": (147, 282)},
            {"file": "image_11.png", "position": (154, 239)},
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

        self.canvas.create_rectangle(60.0, 590.0, 385.0, 730, fill="#FFFFF0", outline="black")

        self.canvas.create_text(
            80,
            600,
            anchor="nw",
            text='''Be a hero! Report the found
laptop and help us reunite
it with its rightful owner.
Your contribution makes a
difference.THANKYOU''',
            fill="#000000",
            font=("InknutAntiqua Regular", 21 * -1,'bold')
        )

        self.canvas.create_text(
            85.9124755859375,
            15.742431640625,
            anchor="nw",
            text="LAPTOP REPORT",
            fill="#3E3333",
            font=("InknutAntiqua Regular", 33 * -1,'bold')
        )

        self.submit_button = Button(
            self.master,
            text="Proceed",
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
            x=172.800537109375,
            y=535.0275268554688,
            width=105.1247787475586,
            height=40.2631893157959
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
            x=229.363037109375,
            y=268.1212463378906,
            width=163.52743530273438,
            height=26.67038917541504
        )
        
        self.create_building_menu()
        self.create_floor_menu()
        self.create_room_menu()

        self.create_brand_menu()
        self.create_model_menu()
        self.create_color_menu()
        self.create_os_menu()

    def create_brand_menu(self):
        self.brand_options = ['None', 'Dell', 'HP', 'Lenovo', 'Asus', 'Acer', 'Apple', 'Microsoft', 'Samsung', 'MSI', 'Razer', 'Toshiba', 'LG', 'Huawei', 'Google (Pixelbook)', 'Fujitsu']


        self.selected_brand=StringVar(self.master)
        self.selected_brand.set(self.brand_options[0])
        self.selected_brand.trace_add("write",self.update_model_options)

        self.create_menu_button(self.canvas,x=210,y=80,width=150,height=30,options=self.brand_options,var=self.selected_brand)

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


    def create_building_menu(self):
        building_options = ["None", "New Building", "Old Building"]
        self.selected_building = StringVar(self.master)
        self.selected_building.set(building_options[0])
        self.selected_building.trace_add("write", self.update_floor_options)

        self.create_menu_button(self.canvas, x=65, y=400, width=160, height=35,options=building_options,var=self.selected_building)

    def create_floor_menu(self):
        self.floor_options = {
            "New Building": ["None", "Ground Floor" ,"1st Floor", "2nd Floor", "3rd Floor", "4th Floor", "5th Floor", "6th Floor", "7th Floor"],
            "Old Building": ["None", "Ground Floor", "1st Floor", "2nd Floor", "3rd Floor", "4th Floor", "5th Floor", "6th Floor", "7th Floor", "8th Floor", "9th Floor", "10th Floor", "11th Floor"]
        }

        self.selected_floor = StringVar(self.master)
        building = self.selected_building.get()
        
        # Check if the selected building is in floor_options dictionary
        if building in self.floor_options:
            self.selected_floor.set(self.floor_options[building][0])
        else:
            self.selected_floor.set("None")

        self.menu_floor = self.create_menu_button(self.canvas, x=230, y=400, width=150, height=35,options=self.floor_options.get(building, ["None"]),var=self.selected_floor)
                
    def update_floor_options(self, *args):
        selected_building = self.selected_building.get()
        new_floor_options = self.floor_options.get(selected_building, ["None"])

        # Set the selected floor to "None" when building option changes
        self.selected_floor.set("None")

        # Update the floor options in the menu
        self.menu_floor.delete(0, "end")

        for floor in new_floor_options:
            self.menu_floor.add_command(label=floor, command=lambda f=floor: self.selected_floor.set(f))

    def create_room_menu(self):
        catagory_room= ["None", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Ladies toilet", "Gents Toilet"]
        self.selected_room=StringVar(self.master)
        self.selected_room.set(catagory_room[0])

        self.create_menu_button(self.canvas, x=175, y=495, width=100, height=35,options=catagory_room,var=self.selected_room)

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
    
    def putdata(self):
        building_name=self.selected_building.get()
        floor=self.selected_floor.get()
        room=self.selected_room.get()
        color=self.selected_laptop_color.get()
        if self.ri.checkForRegister_Report( category = 'laptop_table', myid = self.userId, Brand = self.selected_brand.get() , model = self.selected_model.get(), color  = self.selected_laptop_color.get(), operating_system = self.selected_os_option.get(), serial_number =self.serial_textBox.get("1.0", "end-1c") ) == 'registered':
                self.master.destroy()
        else:
            category = 'laptop'
            if self.ri.location_match(myid=self.userId,building=building_name,floor=floor,room=room,color=color,category=category) == 'request':
                self.master.destroy()
            else:
                c = self.ri.insert_reported_laptop(
                    userId=self.userId,
                    Brand=self.selected_brand.get(),
                    model=self.selected_model.get(),
                    color=self.selected_laptop_color.get(),
                    operating_system=self.selected_os_option.get(),
                    serial_number=self.serial_textBox.get("1.0", "end-1c"),
                    building_name=self.selected_building.get(),
                    floor=self.selected_floor.get(),
                    room=self.selected_room.get(),
                    
                )
                self.ri.set()
                self.msg.ShowMsg("Current we don't have any match but we have saved your report\n thank you very much")
                self.master.destroy()
                
        
    # def location_match(building,floor,room,color,category):


    def showReportLaptop(self):
        self.master.wait_window(self.master)

if __name__=="__main__":
    master = Tk()
    master.resizable(False, False)
    app=reportLaptopPage(master , 3)
    master.mainloop()
