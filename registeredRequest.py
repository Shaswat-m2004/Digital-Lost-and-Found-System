import mysql.connector
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Toplevel,StringVar,Menu,Menubutton
import mymsgBox as messagebox
import login
from MysqlCode import Database
import emailSender
class registeredRequestpage:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"Request\assets\frame0")
    # ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\Request\assets\frame0")

    def relative_to_assets(self, path: str) -> Path:
        file_path = self.ASSETS_PATH / Path(path)
        if file_path.exists():
            return file_path
        else:
            raise FileNotFoundError(f"File not found: {file_path}") 
        
    def __init__(self,master,userId):
        self.msg=messagebox.Rmsg()
        self.userId = userId
        self.db = Database()
        self.master=Toplevel()
        self.master.geometry("536x562")
        self.master.configure(bg = "#DBDBDB")
        self.master.title("Registration")
        self.myData = (self.db.getMydata((self.userId,)))

        self.setup_ui()


    def setup_ui(self):
            
        self.canvas = Canvas(
            self.master,
            bg = "#DBDBDB",
            height = 562,
            width = 536,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            274.0,
            281.0,
            image=self.image_image_1
        )

        text="Select Lost Registered Item"
        x1_position = 90.62469482421875
        y1_position = 96.22653198242188

        text1_width = 260  
        text1_height = 30
        self.canvas.create_rectangle(
            x1_position,
            y1_position,
            x1_position + text1_width,
            y1_position + text1_height,
            fill="white",
            outline=""
        )


        border1_size = 2
        self.canvas.create_text(
            x1_position + border1_size,
            y1_position + border1_size,
            anchor="nw",
            text=text,
            fill="black",
            font=("Arial", 20, "bold")
        )

        text = "Lost Item Location"
        x_position = 135.9683837890625
        y_position = 215.27755737304688

        text_width = 260  
        text_height = 30
        self.canvas.create_rectangle(
            x_position,
            y_position,
            x_position + text_width,
            y_position + text_height,
            fill="white",
            outline=""
        )

        border_size = 2
        self.canvas.create_text(
            x_position + border_size,
            y_position + border_size,
            anchor="nw",
            text=text,
            fill="black",
            font=("Arial", 20, "bold")
        )

        self.canvas.create_text(
            70.9124755859375,
            30.742431640625,
            anchor="nw",
            text="REGISTERED REQUEST",
            fill="#3E3333",
            font=("InknutAntiqua Regular", 35 * -1,'bold')
        )

        self.canvas.create_text(
            90.42889404296875,
            255.62759399414062,
            anchor="nw",
            text="Building Name",
            fill="#000000",
            font=("Arial", 16, "bold")
        )


        self.canvas.create_text(
            340.42889404296875,
            255.62759399414062,
            anchor="nw",
            text="Floor",
            fill="#000000",
            font=("Arial", 16, "bold")
        )

        self.canvas.create_text(
            240.42889404296875,
            340.62759399414062,
            anchor="nw",
            text="Room",
            fill="#000000",
            font=("Arial", 16, "bold")
        )

        self.request_button = Button(
            self.master,
            text="Submit",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 16),
            command=self.match_request,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0 
        )
        self.request_button.place(
            x=180.988525390625,
            y=415.7139587402344,
            width=200.40274047851562,
            height=49.06178665161133
        )
        self.create_building_menu()
        self.create_floor_menu()
        self.create_room_menu()
        self.create_catagory_menu()
    def create_catagory_menu(self):
        catagory_options = ["Laptop", "Mobile phone", "Calculator", "USB flash drive", "Headphones","Books", "Stationery (pens, pencils, erasers, etc.)", "ID card", "Keys (room keys, locker keys, etc.)","Water bottle", "Wallet or purse", "Jacket or coat", "Sunglasses", "Umbrella","Charger (phone charger, laptop charger, etc.)", "Sports equipment", "Lab equipment or tools","Glasses or sunglasses", "Backpack or bag", "Lunch box or food container"]
        self.selected_category_option=StringVar(self.master)
        self.selected_category_option.set(catagory_options[0])

        self.create_menu_button(self.canvas,x=160,y=140, width=170, height=40,options=catagory_options,var=self.selected_category_option)   

    def create_building_menu(self):
        building_options = ["None", "New Building", "Old Building"]
        self.selected_building = StringVar(self.master)
        self.selected_building.set(building_options[0])
        self.selected_building.trace_add("write", self.update_floor_options)

        self.create_menu_button(self.canvas, x=90, y=290, width=150, height=30,
                                options=building_options,
                                var=self.selected_building)
        

    def create_room_menu(self):
        catagory_room= ["None", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Ladies toilet", "Gents Toilet"]
        self.selected_room=StringVar(self.master)
        self.selected_room.set(catagory_room[0])

        self.create_menu_button(self.canvas, x=195, y=370, width=150, height=30,
                        options=catagory_room,
                        var=self.selected_room)

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

        self.menu_floor = self.create_menu_button(self.canvas, x=300, y=290, width=150, height=30,
                                                options=self.floor_options.get(building, ["None"]),
                                                var=self.selected_floor)
        

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

    def update_floor_options(self, *args):
        selected_building = self.selected_building.get()
        new_floor_options = self.floor_options.get(selected_building, ["None"])

        self.selected_floor.set("None")
        self.menu_floor.delete(0, "end")

        for floor in new_floor_options:
            self.menu_floor.add_command(label=floor, command=lambda f=floor: self.selected_floor.set(f))

    def match_request(self):
            category = self.selected_category_option.get()  
            building = self.selected_building.get()
            floor = self.selected_floor.get()
            room = self.selected_room.get()

            result = self.db.checkRequest(self.userId,category, building, floor, room)  
            if result is not False and result is not None:   
                reporter = self.db.getMydata((result,))
                subject = f"{reporter[1]}, we have received a request for the lost item you found"  # Updated subject message for clarity
                content = f'''
                {self.myData[1]} has requested
                Contact Details:
                Email: {self.myData[2]}
                Mobile No: {self.myData[3]}
                Please contact {self.myData[1]} for item recovery
                '''
                emailSender.sendEmail(reporter[2], subject, content)
                self.master.destroy()

               
    def showrequestRegisteredDevice(self):
        self.master.wait_window(self.master)
                

    
if __name__=="__main__":
    master = Tk()
    app=registeredRequestpage(master,4)
    master.resizable(False, False)
    master.mainloop()
