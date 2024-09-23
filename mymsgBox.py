from tkinter import Toplevel, Label, Button

class Rmsg:
    def ShowMsg(self, msgtext):
        msg = Toplevel()
        msg.geometry('400x200')
        msg.title('Message')

        msgL = Label(
            msg,
            text=msgtext,
            wraplength=380,
            justify="left",
            padx=20,
            pady=20,
            font=("Helvetica", 14),
            bg="#F0F0F0",
            fg="#333333"
        )
        msgL.pack()

        b = Button(
            msg,
            text="OK",
            bg="#5C4D4D",
            fg="#FFFFFF",
            font=("InknutAntiqua Regular", 16),
            command=msg.destroy,
            relief="raised", 
            bd=5,  
            padx=10, 
            pady=5,  
            activebackground="#7F6E6E",
            activeforeground="#000000",
            highlightthickness=0 
        )
        b.pack(pady=10)

if __name__ == "__main__":
    Rmsg().ShowMsg("Hello, this is a long message. " * 20)
