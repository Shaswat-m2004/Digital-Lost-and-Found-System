
from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage, StringVar, Menubutton, Menu, Toplevel, Button, Text, filedialog
import mymsgBox as messagebox
import mysql.connector
from PIL import Image, ImageTk
import io
from MysqlCode import Database
import emailSender

class reportPage:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"Report/assets/frame0")
    # ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\Report\assets\frame0")

    def relative_to_assets(self, path: str) -> Path:
        file_path = self.ASSETS_PATH / Path(path)
        if file_path.exists():
            return file_path
        else:
            print(f"Warning: File not found: {file_path}")
            return file_path

    # def __init__(self, master , proId):
    def __init__(self, master , userId ):
        self.msg = messagebox.Rmsg()
        self.master = master
        self.master = Toplevel()
        # self.proId = proId
        # self.proId = ('MFL0255',)
        self.userId = userId
        self.master.geometry("432x792")
        self.master.configure(bg="#D9D9D9")
        self.master.title("Registration")
        # self.image_path = None
        self.image_data = None
        self.db = Database()
        self.myData = (self.db.getMydata((self.userId,)))

        self.setup_ui()

    def setup_ui(self):
        self.canvas = Canvas(
            self.master,
            bg="#D9D9D9",
            height=792,
            width=432,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
                file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
                216.6407470703125,
                406.1710205078125,
                image=self.image_image_1,
            )

        # Elements properties
        elements = [
            {"type": "text", "text": "Lost Item Category", "position": (48.45654296875, 109.1710205078125), "font": ("Arial", 12, "bold")},
            {"type": "text", "text": "Lost Item Name", "position": (130.42889404296875, 149.62759399414062), "font": ("Arial", 16, "bold")},
            {"type": "rectangle", "position": (80.9683837890625, 215.27755737304688), "size": (260, 30), "fill": "white"},
            {"type": "text", "text": "Lost Item Location", "position": (80.9683837890625 + 2, 215.27755737304688 + 2), "font": ("Arial", 20, "bold")},
            {"type": "text", "text": "Building Name", "position": (50.42889404296875, 275.62759399414062), "font": ("Arial", 16, "bold")},
            {"type": "text", "text": "Floor", "position": (275.42889404296875, 275.62759399414062), "font": ("Arial", 16, "bold")},
            {"type": "text", "text": "Room", "position": (185.42889404296875, 340.62759399414062), "font": ("Arial", 16, "bold")}
        ]

        for element in elements:
            if element["type"] == "text":
                self.canvas.create_text(*element["position"], anchor="nw", text=element["text"], fill="#000000", font=element["font"])
            elif element["type"] == "rectangle":
                x, y = element["position"]
                width, height = element["size"]
                self.canvas.create_rectangle(x, y, x + width, y + height, fill=element.get("fill", "white"), outline="")

        self.entry_1 = Text(
            self.master,
            bd=5,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("InknutAntiqua Regular", 12)
        )
        self.entry_1.place(
            x=90.1578369140625,
            y=180.59994506835938,
            width=250.45254516601562,
            height=30.723670959472656
        )

        self.canvas.create_rectangle(
            87.189453125,
            468.29718017578125,
            334.88670349121094,
            666.4549865722656,
            fill="#FFFFFF",
            outline="black",
            width=2
        )

        self.image_canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.image_canvas.place(
            x=87.189453125,
            y=468.29718017578125,
            width=247.69725036621094,
            height=198.15780639648438
        )

        self.upload_image = Button(
            self.master,
            text="Upload Image",
            bg="#5C4D4D",
            fg="#DBDBDB",
            font=("InknutAntiqua Regular", 16),
            command=self.upload_image_clicked,
            relief="ridge",
            bd=5,
        )
        self.upload_image.place(
            x=120.6920166015625,
            y=420.7853698730469,
            width=168.4341278076172,
            height=36.16380310058594
        )

        self.Report_button = Button(
            self.master,
            text="Report",
            bg="#5C4D4D",
            fg="#DBDBDB",
            font=("InknutAntiqua Regular", 16),
            command=self.Report_button_clicked,  # Use the method directly
            relief="ridge",
            bd=5,
        )

        self.Report_button.place(
            x=126.7288818359375,
            y=680.0404663085938,
            width=168.4341278076172,
            height=35.66840362548828
        )

        self.canvas.create_text(
            149.609130859375,
            0.0,
            anchor="nw",
            text="Report",
            fill="#000000",
            font=("InknutAntiqua Regular", 34 * -1)
        )

        self.create_building_menu()
        self.create_floor_menu()
        self.create_catagory_menu()
        self.create_room_menu()

    def create_menu(self, master, x, y, width, height, options, var):
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

    def create_building_menu(self):
        building_options = ["None", "New Building", "Old Building"]
        self.selected_building = StringVar(self.master)
        self.selected_building.set(building_options[0])
        self.selected_building.trace_add("write", self.update_floor_options)

        self.create_menu(self.canvas, x=50, y=300, width=150, height=30,
                         options=building_options,
                         var=self.selected_building)

    def create_catagory_menu(self):
        catagory_options = ["None", "Bag", "Bottle", "Mobile", "Laptop", "Stationary"]
        self.selected_catagory = StringVar(self.master)
        self.selected_catagory.set(catagory_options[0])

        self.create_menu(self.canvas, x=200, y=100, width=180, height=30,
                         options=catagory_options,
                         var=self.selected_catagory)

    def create_room_menu(self):
        catagory_room = ["None", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Ladies toilet", "Gents Toilet"]
        self.selected_room = StringVar(self.master)
        self.selected_room.set(catagory_room[0])

        self.create_menu(self.canvas, x=135, y=370, width=150, height=30,
                         options=catagory_room,
                         var=self.selected_room)

    def create_floor_menu(self):
        self.floor_options = {
            "New Building": ["None", "Ground Floor", "1st Floor", "2nd Floor", "3rd Floor", "4th Floor", "5th Floor", "6th Floor", "7th Floor"],
            "Old Building": ["None", "Ground Floor", "1st Floor", "2nd Floor", "3rd Floor", "4th Floor", "5th Floor", "6th Floor", "7th Floor", "8th Floor", "9th Floor", "10th Floor", "11th Floor"]
        }

        self.selected_floor = StringVar(self.master)
        building = self.selected_building.get()

        # Check if the selected building is in floor_options dictionary
        if building in self.floor_options:
            self.selected_floor.set(self.floor_options[building][0])
        else:
            self.selected_floor.set("None")

        self.menu_floor = self.create_menu(self.canvas, x=225, y=300, width=150, height=30,
                                           options=self.floor_options.get(building, ["None"]),
                                           var=self.selected_floor)

    def update_floor_options(self, *args):
        selected_building = self.selected_building.get()
        new_floor_options = self.floor_options.get(selected_building, ["None"])

        self.selected_floor.set("None")

        self.menu_floor.delete(0, "end")

        for floor in new_floor_options:
            self.menu_floor.add_command(label=floor, command=lambda f=floor: self.selected_floor.set(f))

    def upload_image_clicked(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            # Load the image using Pillow
            img = Image.open(file_path)
            img = img.resize((247, 198), Image.BICUBIC)  # Resize the image to fit the rectangle

            image_bytes = io.BytesIO()
            img.save(image_bytes, format="PNG")  # You can change the format if needed

            self.image_data = image_bytes.getvalue()

            self.photo = ImageTk.PhotoImage(img)

            # Display the image in the rectangle
            self.image_canvas.create_image(0, 0, anchor="nw", image=self.photo)
            self.image_canvas.image = self.photo 

            print(f"Selected Image: {file_path}")

    def Report_button_clicked(self):
    
        if any(value is None or value.strip() == "" for value in [self.selected_catagory.get(),self.entry_1.get("1.0", "end-1c"),self.selected_building.get(),self.selected_floor.get(),self.selected_room.get(),self.image_data]):
            self.msg.ShowMsg("All Field must be Filled")
            return
        else:
            next = self.db.checkReport(self.userId ,self.selected_catagory.get(),self.entry_1.get("1.0", "end-1c"),self.selected_building.get(),self.selected_floor.get(),self.selected_room.get(),self.image_data)
            if next is not False:
                next = self.db.getMydata((next,))
                subject = f"{next[1]} , we have received a report of your lost Item"
                content = f'''
                {self.myData[1]} has found your belonging
                Contact Details:
                Email : {self.myData[2]}
                Mobile No : {self.myData[3]}
                Please Contact {self.myData[1]} for your lost item recovery
                '''
                emailSender.sendEmail(next[2] , subject , content)
                self.master.destroy()


if __name__ == "__main__":
    master = Tk()
    master.resizable(False, False)
    app = reportPage(master , 19)
    master.mainloop()
