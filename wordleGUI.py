import tkinter as TK
from PIL import Image, ImageTk












if __name__ == "__main__":
    root = TK.Tk()
    root.geometry("500x1000")
    root.title("Wordle Remake")
    root.configure(bg = "#4D4D4D", borderwidth=0)

    load = Image.open("wordleBanner.jpeg")
    render = ImageTk.PhotoImage(load)
    banner = TK.Label(root, image=render,bg="#dddddd", border=0 )
    banner.pack()

    guessLine = TK.Frame(root, height = 75, width = 500)
    guessLine.pack()
    guessEntry = TK.Entry(guessLine, font=("Times","18"))
    guessEntry.insert(0, "GUESS")
    guessEntry.grid(row =0, column=0)



    root.mainloop()
