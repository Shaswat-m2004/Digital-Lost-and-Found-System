import mymsgBox as messagebox
from tkinter import Tk, Canvas, Button, Toplevel, Label, filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

class downloadID:

    def __init__(self, parent_app,reporter_product_id):
        self.msg = messagebox.Rmsg()
        self.master = Toplevel()
        self.parent_app = parent_app
        self.product_id=reporter_product_id
        self.master.geometry("600x500")
        self.master.configure(bg="#FFFFFF")
        self.master.title("Registration")

        self.setup_ui()

    def setup_ui(self):
        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=470,
            width=593,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            593.0,
            470.0,
            fill="#D9D9D9",
            outline="black"
        )

        self.canvas.create_rectangle(
            50.0,
            70.0,
            545.0,
            425.0,
            fill="white",
            outline="black"
        )

        self.canvas.create_rectangle(
            60.0,
            80.0,
            535.0,
            300.0,
            fill="#D9D9D9",
            outline="black"
        )

        self.download_button = Button(
            self.master,
            text="Download",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 16),
            command=self.download_image,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0 
        )
        self.download_button.place(
            x=235,
            y=350,
            width=109.02468872070312,
            height=40.05535888671875
        )

        self.canvas.create_text(
            90.419677734375,
            11.1925048828125,
            anchor="nw",
            text="DOWNLOAD PRODUCT ID",
            fill="#000000",
            font=("InknutAntiqua Regular", 33 * -1,'bold')
        )
 

        self.modifyImg()

    def modifyImg(self):
        text =str(self.product_id )
        print(self.product_id)
        # image_path = r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\DownloadPID\sourceimg\logoFoundmate.jpg"
        image_path = r"DownloadPID\sourceimg\logoFoundmate.jpg"
        # image_path = r"DownloadPID\sourceimg\logoFoundmate.jpg"
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        font_size = 125
        # font_path = r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\DownloadPID\orbitron-font\OrbitronBlack-n6dV.ttf"
        font_path = r"DownloadPID\orbitron-font\OrbitronBlack-n6dV.ttf"
        font = ImageFont.truetype(font_path, font_size)
        shadow_offset = (5, 5)
        shadow_color = "gray"
        shadow_position = (1765 + shadow_offset[0], 640 + shadow_offset[1])
        draw.text(shadow_position, text, fill=shadow_color, font=font)
        stroke_color = "gray"
        stroke_width = 2
        for dx in range(-stroke_width, stroke_width + 1):
            for dy in range(-stroke_width, stroke_width + 1):
                if abs(dx) + abs(dy) > 0:
                    draw.text((1765 + dx, 640 + dy), text, fill=stroke_color, font=font)
        main_text_color = "black"
        draw.text((1765, 640), text, fill=main_text_color, font=font)
        # modified_image_path = r"C:\Users\admin\OneDrive\VS-CODE\SEM4_MiniProject\Foundmate_3.1\DownloadPID\resultImg\NewlogoFoundmate.png"
        modified_image_path = r"C:DownloadPID\resultImg\NewlogoFoundmate.png"
        image.save(modified_image_path)
        print(f"Text with shadow and stroke added to the image and saved as {modified_image_path}")

        self.result_image = Image.open(modified_image_path)
        width, height = 468, 214
        self.result_image = self.result_image.resize((width, height))
        self.result_image_tk = ImageTk.PhotoImage(self.result_image)
        self.image_label = Label(self.master, image=self.result_image_tk)
        self.image_label.place(x=64, y=82)

    def download_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.result_image.save(file_path)
            print(f"Image downloaded successfully at {file_path}")
            self.master.destroy()


    def showDownloadPID(self):
        self.master.wait_window(self.master)

if __name__ == "__main__":
    master = Tk()
    app = downloadID(master,'ABC1234')
    master.mainloop()
