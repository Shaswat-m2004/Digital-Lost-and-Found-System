# from pathlib import Path
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage , Toplevel,Menu,Menubutton,StringVar
# from tkinter import ttk
# from MysqlCode import Database

# class othersCategory:
#     OUTPUT_PATH = Path(__file__).parent
#     ASSETS_PATH = OUTPUT_PATH / Path(r"OthersCategory\assets\frame0")
#     # ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\OthersCategory\assets\frame0")

#     def relative_to_assets(self, path: str) -> Path:
#         file_path = self.ASSETS_PATH / Path(path)
#         if file_path.exists():
#             return file_path
#         else:
#             print(f"Warning: File not found: {file_path}")
#             return file_path 

#     def __init__(self , parentApp):
#         self.parentApp = parentApp
#         self.master = Toplevel()
#         self.master.geometry("479x516")
#         self.userId = 20
#         self.db = Database()
#         self.setup_ui()

#     def setup_ui(self):
#         self.canvas = Canvas(
#             self.master,
#             bg = "#FFFFFF",
#             height = 479,
#             width = 516,
#             bd = 0,
#             highlightthickness = 0,
#             relief = "ridge"
#         )

#         self.canvas.place(x = 0, y = 0)
#         self.canvas.create_rectangle(
#             0.0,
#             0.0,
#             516.0,
#             479.03399658203125,
#             fill="#D9D9D9",
#             outline="")
#         image_details = [
#             {"file": "image_1.png", "position": (240.88037109375, 252.50222778320312)},
#             {"file": "image_2.png", "position": (143.0, 156.0)},
#             {"file": "image_3.png", "position": (143.0, 98.0)},
#             {"file": "image_4.png", "position": (248.434326171875, 214.500732421875)},
#         ]

#         self.image_objects = {}
#         for idx, details in enumerate(image_details):
#             image_path = self.relative_to_assets(details["file"])
#             self.image_objects[idx] = PhotoImage(file=image_path)
#             canvas_image = self.canvas.create_image(
#                 details["position"][0],
#                 details["position"][1],
#                 image=self.image_objects[idx]
#             ) 

#         self.submit_button = Button(
#             self.master,
#             text="Submit",
#             bg="#5C4D4D",
#             fg="#FFFFFF",
#             font=("InknutAntiqua Regular", 16),
#             command=self.putdata,
#             relief="raised", 
#             bd=5,  
#             padx=10, 
#             pady=5,  
#             activebackground="#7F6E6E",
#             activeforeground="#000000",
#             highlightthickness=0 
#         )
#         self.submit_button.place(
#             x=179.494873046875,
#             y=382.236328125,
#             width=129.46466064453125,
#             height=39.252586364746094
#         )

#         self.canvas.create_text(
#             160.32470703125,
#             20.18475341796875,
#             anchor="nw",
#             text="OTHERS",
#             fill="#3E3333",
#             font=("InknutAntiqua Regular", 33 * -1,'bold')
#         )

#         self.description_textbox = Text(
#             self.master,
#             bd=5,
#             bg="#FFFFFF",
#             fg="#000716",
#             highlightthickness=0,
#             font=("InknutAntiqua Regular", 10)
#         )
#         self.description_textbox.place(
#             x=90,
#             y=253,
#             width=305,
#             height=120
#         )

#         self.create_others_color_menu()
#         self.create_catagory_menu()

#     def create_catagory_menu(self):
#         catagory_options = ["Laptop", "Mobile phone", "Calculator", "USB flash drive", "Headphones","Books", "Stationery (pens, pencils, erasers, etc.)", "ID card", "Keys (room keys, locker keys, etc.)","Water bottle", "Wallet or purse", "Jacket or coat", "Sunglasses", "Umbrella","Charger (phone charger, laptop charger, etc.)", "Sports equipment", "Lab equipment or tools","Glasses or sunglasses", "Backpack or bag", "Lunch box or food container"]
#         self.selected_category_option=StringVar(self.master)
#         self.selected_category_option.set(catagory_options[0])

#         self.create_menu_button(self.canvas,x=220, y=75, width=170,height=40,options=catagory_options,var=self.selected_category_option) 

#     def create_others_color_menu(self):
#         laptop_colors = ["None","red", "green", "blue", "yellow", "magenta", "cyan", "maroon", "green2", "navy", "olive", "purple", "teal", "orange", "gray", "white", "black"]

#         self.selected_mobile_color=StringVar(self.master)
#         self.selected_mobile_color.set(laptop_colors[0])

#         self.create_menu_button(self.canvas,x=220,y=136, width=170, height=40,options=laptop_colors,var=self.selected_mobile_color)           

#     def create_menu_button(self, master, x, y, width, height, options, var):
#         menubutton = Menubutton(
#             master,
#             textvariable=var,
#             font=("Helvetica", 12, "bold"),
#             indicatoron=True,
#             borderwidth=1,
#             relief="ridge",
#             bd=5,
#             bg="#5C4D4D",
#             fg="#DBDBDB"
#         )
#         menubutton.place(x=x, y=y, width=width, height=height)

#         menu = Menu(menubutton, tearoff=False)
#         menubutton["menu"] = menu

#         for option in options:
#             menu.add_command(label=option, command=lambda o=option: var.set(o))

#         return menu        

#     def show_others(self):
#         self.master.wait_window(self.master)
    
#     def putdata(self):
#         c = self.db.insert_other_data(
#             userId=self.userId,
#             name=self.name_textbox.get("1.0", "end-1c"),
#             color=self.selected_mobile_color.get(),
#             description=self.description_textbox.get("1.0", "end-1c")
#         )
#         if c is True:
#             self.parentApp.label3.place(x=510, y=250, height=40, width=80)
#             self.master.destroy()


# if __name__=="__main__":
#     master = Tk()
#     app=othersCategory(master)
#     master.mainloop()


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage , Toplevel,Menu,Menubutton,StringVar
from tkinter import ttk
from MysqlCode import Database

class othersCategory:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"OthersCategory\assets\frame0")
    # ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\OthersCategory\assets\frame0")

    def relative_to_assets(self, path: str) -> Path:
        file_path = self.ASSETS_PATH / Path(path)
        if file_path.exists():
            return file_path
        else:
            print(f"Warning: File not found: {file_path}")
            return file_path 

    def __init__(self , parentApp,userId):
        self.parentApp = parentApp
        self.master = Toplevel()
        self.master.geometry("479x516")
        self.userId = userId
        self.db = Database()
        self.setup_ui()

    def setup_ui(self):
        self.canvas = Canvas(
            self.master,
            bg = "#FFFFFF",
            height = 479,
            width = 516,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            516.0,
            479.03399658203125,
            fill="#D9D9D9",
            outline="")
        image_details = [
            {"file": "image_1.png", "position": (240.88037109375, 252.50222778320312)},
            {"file": "image_2.png", "position": (143.0, 156.0)},
            {"file": "image_3.png", "position": (143.0, 98.0)},
            {"file": "image_4.png", "position": (248.434326171875, 214.500732421875)},
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

        self.canvas.create_rectangle(125,195,352,235,fill="white",outline="black")

        self.canvas.create_text(
            135,
            205,
            anchor="nw",
            text="SECURITY QUESTIONS",
            fill="#000000",
            font=("InknutAntiqua Regular", 18 * -1,'bold')
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
            x=179.494873046875,
            y=390.236328125,
            width=129.46466064453125,
            height=39.252586364746094
        )

        self.canvas.create_text(
            160.32470703125,
            20.18475341796875,
            anchor="nw",
            text="OTHERS",
            fill="#3E3333",
            font=("InknutAntiqua Regular", 33 * -1,'bold')
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
            y=285,
            width=365,
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
            y=355,
            width=365,
            height=30
        )

        self.create_others_color_menu()
        self.create_catagory_menu()

        self.security_question1()
        self.security_question2()

    def security_question1(self):
        self.questions=["What is the name of your first pet?","What is the maiden name of your mother?","In what city were you born?","What is the name of your favorite teacher?","What is the make and model of your first car?"]
        
        self.selected_question1=StringVar(self.master)
        self.selected_question1.set(self.questions[0])

        self.create_menu_button(self.canvas,x=55,y=250,width=370,height=30,options=self.questions,var=self.selected_question1)

    def security_question2(self):
        self.questions= ["What is your favorite book or movie?","What was the name of your childhood best friend?","What is the name of the street you grew up on?","What is the name of your favorite fictional character?","What is your favorite food?"]
        
        self.selected_question2=StringVar(self.master)
        self.selected_question2.set(self.questions[0])  

        self.create_menu_button(self.canvas,x=55,y=320,width=370,height=30,options=self.questions,var=self.selected_question2)


    def create_catagory_menu(self):
        catagory_options = ["Laptop", "Mobile phone", "Calculator", "USB flash drive", "Headphones","Books", "Stationery (pens, pencils, erasers, etc.)", "ID card", "Keys (room keys, locker keys, etc.)","Water bottle", "Wallet or purse", "Jacket or coat", "Sunglasses", "Umbrella","Charger (phone charger, laptop charger, etc.)", "Sports equipment", "Lab equipment or tools","Glasses or sunglasses", "Backpack or bag", "Lunch box or food container"]
        self.selected_category_option=StringVar(self.master)
        self.selected_category_option.set(catagory_options[0])

        self.create_menu_button(self.canvas,x=220, y=75, width=170,height=40,options=catagory_options,var=self.selected_category_option) 

    def create_others_color_menu(self):
        laptop_colors = ["None","red", "green", "blue", "yellow", "magenta", "cyan", "maroon", "green2", "navy", "olive", "purple", "teal", "orange", "gray", "white", "black"]

        self.selected_mobile_color=StringVar(self.master)
        self.selected_mobile_color.set(laptop_colors[0])

        self.create_menu_button(self.canvas,x=220,y=136, width=170, height=40,options=laptop_colors,var=self.selected_mobile_color)           

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

    def show_others(self):
        self.master.wait_window(self.master)
    
    def putdata(self):
        c = self.db.insert_other_data(
            userId=self.userId,
            name=self.selected_category_option.get(), 
            color=self.selected_mobile_color.get(),   
            security_qustion1=self.selected_question1.get(), 
            security_answer1=self.question1_textBox.get("1.0", "end-1c"),
            security_qustion2=self.selected_question2.get(), 
            security_answer2=self.question2_textBox.get("1.0", "end-1c")
        )
        if c is True:
            # self.parentApp.label3.place(x=510, y=250, height=40, width=80)
            self.master.destroy()



if __name__=="__main__":
    master = Tk()
    app=othersCategory(master,3)
    master.mainloop()