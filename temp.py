import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter import Canvas, Entry, Text, Button, PhotoImage , Toplevel
from MysqlCode import Database

class mobileCategory:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"MobileCategory\assets\frame0")

    def relative_to_assets(self, path: str) -> Path:
        file_path = self.ASSETS_PATH / Path(path)
        if file_path.exists():
            return file_path
        else:
            print(f"Warning: File not found: {file_path}")
            return file_path 

    def __init__(self):
        self.master = Toplevel()
        self.master.geometry("444x552")
        self.userId = 21
        self.db = Database()
        self.setup_ui()

    def setup_ui(self):
        self.canvas = Canvas(
            self.master,
            bg = "#FFFFFF",
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
            outline="")

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            223.12841796875,
            299.5784912109375,
            image=self.image_image_1
        )

        self.canvas.create_text(
            137.32470703125,
            11.18475341796875,
            anchor="nw",
            text="MOBILE",
            fill="#000000",
            font=("InknutAntiqua Regular", 33 * -1)
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            122.169189453125,
            96.12225341796875,
            image=self.image_image_2
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.master,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.putdata,
            relief="flat"
        )
        self.button_1.place(
            x=164.8956298828125,
            y=486.2538146972656,
            width=104.98177337646484,
            height=30.222026824951172
        )

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            122.169189453125,
            143.84124755859375,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            122.169189453125,
            191.56024169921875,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            154.169189453125,
            239.27923583984375,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            235.93505859375,
            330.4754943847656,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            132.169189453125,
            284.8774108886719,
            image=self.image_image_7
        )

        self.entry_1 = Entry(
            self.master,
            bd=0,
            bg="#FDF9F9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=203.0706787109375,
            y=269.8774108886719,
            width=188.2248992919922,
            height=26.631393432617188
        )

        self.entry_2 = Text(
            self.master,
            bd=0,
            bg="#FDF9F9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=81,
            y=353, 
            width=281,
            height=110
        )
        #  master,
        #     textvariable=var,
        #     font=("Helvetica", 12, "bold"),
        #     indicatoron=True,
        #     borderwidth=1,
        #     relief="ridge",
        #     bd=5,
        #     bg="#5C4D4D",
        #     fg="#DBDBDB"
        
        style = ttk.Style()
        style.theme_create('CustomStyle', parent='alt', settings={
            "TCombobox": {
                "configure": {"foreground": "black", "background": "#5C4D4D" },
                "selectbackground": "#5C4D4D",
                "fieldbackground": "#5C4D4D",
                "bordercolor": "#5C4D4D"
                # "arrowcolor": "black",
                # "padding": 50s
                # "height":2000
            }
        })
        style.theme_use('CustomStyle')
                
        self.mobile_brands = ["Apple", "Samsung", "Huawei", "Xiaomi", "OnePlus", "Oppo", "Vivo", "Google (Pixel)", "Sony", "LG"]
        self.mobile_colors = ["Black", "White", "Silver", "Gold", "Blue", "Red", "Green", "Pink", "Purple", "Yellow"]
        self.operating_systems = ["iOS", "Android", "Windows Phone", "BlackBerry OS", "Symbian", "KaiOS", "Other"]

        self.brand_combo = ttk.Combobox(
            self.master, 
            values=self.mobile_brands,
            style='CustomStyle.TCombobox'
        )

        self.brand_combo.place(x=210, y=80)
        self.brand_combo.bind("<<ComboboxSelected>>", self.populate_models)
        self.brand_combo.config(width=20, height=5000)

        self.model_combo = ttk.Combobox(self.master)
        self.model_combo.place(x=210, y=130)

        self.color_combo = ttk.Combobox(self.master, values=self.mobile_colors)
        self.color_combo.place(x=210, y=180)

        self.os_combo = ttk.Combobox(self.master, values=self.operating_systems)
        self.os_combo.place(x=260, y=230)

    def populate_models(self , event):
        selected_brand = self.brand_combo.get()
        models = {
            "Apple": ["iPhone 13", "iPhone 12", "iPhone SE", "iPhone 11", "iPhone XR"],
            "Samsung": ["Galaxy S21", "Galaxy Note 20", "Galaxy A52", "Galaxy Z Fold", "Galaxy S20"],
            "Huawei": ["P40 Pro", "Mate 40", "Nova 7", "P30 Pro", "Mate Xs"],
            "Xiaomi": ["Mi 11", "Redmi Note 10", "Mi 10T", "Redmi K40", "POCO X3"],
            "OnePlus": ["OnePlus 9 Pro", "OnePlus 8T", "OnePlus Nord", "OnePlus 8 Pro", "OnePlus 7T"],
            "Oppo": ["Find X3 Pro", "Reno 5 Pro", "A74", "Reno 4 Pro", "F19 Pro"],
            "Vivo": ["X60 Pro", "V21 5G", "Y73", "X50 Pro", "V20 Pro"],
            "Google (Pixel)": ["Pixel 5", "Pixel 4a", "Pixel 4", "Pixel 3a", "Pixel 3"],
            "Sony": ["Xperia 1 III", "Xperia 5 III", "Xperia 10 III", "Xperia 1 II", "Xperia 5 II"],
            "LG": ["Wing", "V60 ThinQ", "G8 ThinQ", "V50 ThinQ", "G7 ThinQ"]
        }
        self.model_combo['values'] = models.get(selected_brand, [])

    def show_mobile(self):
        self.master.wait_window(self.master)

    def putdata(self):
        print(self.brand_combo.get())
        print(self.model_combo.get())
        print(self.os_combo.get())
        print(self.color_combo.get())
        self.db.insert_mobile_data(
        userId=self.userId,
        Brand=self.brand_combo.get(),
        model=self.model_combo.get(),
        color=self.color_combo.get(),
        operating_system=self.os_combo.get(),
        imei_number=self.entry_1.get(),
        unique_identification=self.entry_2.get("1.0", "end-1c")
    )

if __name__=="__main__":
    master = tk.Tk()
    app = mobileCategory()
    master.mainloop()
