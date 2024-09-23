import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Emoji Display")

    # Unicode characters for emojis
    emoji_list = ["\U0001F600", "\U0001F604", "\U0001F609", "\U0001F60D", "\U0001F618"]

    # Create labels to display emojis
    for i, emoji in enumerate(emoji_list):
        label = tk.Label(root, text=emoji, font=("Arial", 20))
        label.grid(row=0, column=i, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
