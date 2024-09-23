from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Toplevel,Menu,Menubutton,StringVar
from MysqlCode import Database
from reportInsertion import DatabaseManager
import mymsgBox as messagebox


class reportMobilePage:
    OUTPUT_PATH = Path(__file__).parent
    # ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\ReportMobile\assets\frame0")
    ASSETS_PATH = OUTPUT_PATH / Path(r"ReportMobile\assets\frame0")

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
        self.ri = DatabaseManager(self.userId)
        self.db = Database()
        self.msg = messagebox.Rmsg()

        self.setup_ui()

    def setup_ui(self):
        print(self.userId,'from report_mobile')

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
            445.07928466796875,
            783.0,
            fill="#D9D9D9",
            outline="black")
        
        image_details = [
            {"file": "image_1.png", "position": (224, 405)},
            {"file": "image_2.png", "position": (225, 470)},
            {"file": "image_3.png", "position": (329, 375)},
            {"file": "image_4.png", "position": (142, 375)},
            {"file": "image_5.png", "position": (220, 327)},
            {"file": "image_6.png", "position": (122, 96)},
            {"file": "image_7.png", "position": (122, 146)},
            {"file": "image_8.png", "position": (122, 191)},
            {"file": "image_9.png", "position": (154, 239)},
            {"file": "image_11.png", "position": (135, 282)},
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
Mobile and help us reunite
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
            text="MOBILE REPORT",
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

        self.imei_textBox = Text(
            self.master,
            bd=5,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("InknutAntiqua Regular", 10)
        )
        self.imei_textBox.place(
            x=203.1767578125,
            y=267.018310546875,
            width=188.32318115234375,
            height=30.64634132385254
        )

        self.create_building_menu()
        self.create_floor_menu()
        self.create_room_menu()

        self.create_mobile_brand_menu()
        self.create_mobile_model_menu()
        self.create_mobile_color_menu()
        self.create_mobile_os_menu()        

    def create_mobile_brand_menu(self):
        self.brand_options =  ["None","Apple", "Samsung", "Huawei", "Xiaomi", "OnePlus", "Oppo", "Vivo", "Google (Pixel)", "Sony", "LG"]


        self.selected_mobile_brand=StringVar(self.master)
        self.selected_mobile_brand.set(self.brand_options[0])
        self.selected_mobile_brand.trace_add("write",self.udate_mobile_model_options)

        self.create_menu_button(self.canvas,x=210,y=80,width=150,height=30,options=self.brand_options,var=self.selected_mobile_brand)

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

        self.menu_floor = self.create_menu_button(self.canvas, x=280, y=400, width=100, height=35,options=self.floor_options.get(building, ["None"]),var=self.selected_floor)
                
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
        # if self.ri.checkForRegister_Report('mobile_table', self.userId , self.selected_mobile_brand.get() , self.selected_mobile_model.get() , self.selected_mobile_color.get() , self.selected_mobile_os_option.get(),  self.imei_textBox.get("1.0", "end-1c")):
        #     self.ri.insert_reported_mobile(
        #         userId=self.userId,
        #         Brand=self.selected_mobile_brand.get(),
        #         model=self.selected_mobile_model.get(),
        #         color=self.selected_mobile_color.get(),
        #         operating_system=self.selected_mobile_os_option.get(),
        #         imei_number=self.imei_textBox.get("1.0", "end-1c"),
        #         # unique_identification=self.unique_identification_textBox.get("1.0", "end-1c"),
        #         building_name=self.selected_building.get(),
        #         floor=self.selected_floor.get(),
        #         room=self.selected_room.get()
        #     )
        #     self.ri.set()
        #     print("insertion done")

        building_name=self.selected_building.get()
        floor=self.selected_floor.get()
        room=self.selected_room.get()
        color=self.selected_mobile_color.get()
        if self.ri.checkForRegister_Report('mobile_table', self.userId , self.selected_mobile_brand.get() , self.selected_mobile_model.get() , self.selected_mobile_color.get() , self.selected_mobile_os_option.get(),  self.imei_textBox.get("1.0", "end-1c")):
                self.master.destroy()
        else:
            category = 'mobile'
            if self.ri.location_match(myid=self.userId,building=building_name,floor=floor,room=room,color=color,category=category) == 'request':
                self.master.destroy()
            else:
                c = self.ri.insert_reported_mobile(
                    userId=self.userId,
                Brand=self.selected_mobile_brand.get(),
                model=self.selected_mobile_model.get(),
                color=self.selected_mobile_color.get(),
                operating_system=self.selected_mobile_os_option.get(),
                imei_number=self.imei_textBox.get("1.0", "end-1c"),
                building_name=self.selected_building.get(),
                floor=self.selected_floor.get(),
                room=self.selected_room.get()
                    
                )
                self.ri.set()
                self.msg.ShowMsg("Current we don't have any match but we have saved your report\n thank you very much")
                self.master.destroy()


    def showReportMobile(self):
        self.master.wait_window(self.master)

if __name__=="__main__":
    master = Tk()
    master.resizable(False, False)
    app=reportMobilePage(master , 3)
    master.mainloop()
