import tkinter as TK
from PIL import Image, ImageTk
import random

possibleGuessFile = open("combined_wordlist.txt", "r")
possibleGuessList = possibleGuessFile.readlines()
possibleGuessFile.close()

possibleAnswerFile = open("shuffled_real_wordles.txt", "r")
possibleAnswerList = possibleAnswerFile.readlines()
possibleAnswerFile.close()

answer = ""
win = False
guessed = ""


def getInput():
    global win
    global guessed

    setError("")
    #while win == False:
    while guessed == "":
        print("---")
        typed = guessEntry.get()
        print(typed)
        if len(typed) != 5:
            setError("Error: Your guess should be five letters.")
        elif not typed.isalpha():
            setError("Error: Your guess should only include letters.")
        elif not inCombined(typed.lower()):
            setError("Error: Your guess is not in the word list.")
        else:
            guessed = typed.upper()
def setError(errorText):
    errorLabel.configure(text=errorText)
def getAnswer():
    global answer
    answerIndex = random.randint(0, len(possibleAnswerList))
    answer = possibleAnswerList[answerIndex].strip()
def inCombined(word):
    for entry in possibleGuessList:
        if word == entry.strip():
            return True





if __name__ == "__main__":
    getAnswer()

    root = TK.Tk()
    root.geometry("500x1000")
    root.title("Wordle Remake")
    root.configure(bg = "#4D4D4D", borderwidth=0)

    load = Image.open("wordleBanner.jpeg")
    render = ImageTk.PhotoImage(load)
    banner = TK.Label(root, image=render,bg="#dddddd", border=0 )
    banner.pack()

    guessLine = TK.Frame(root, height = 75, width = 500, bg="#4d4d4d")
    guessLine.pack()
    guessEntry = TK.Entry(guessLine, font=("Times","18"))
    guessEntry.insert(0, "GUESS")
    guessEntry.grid(row =0, column=0)


    load2 = Image.open("guessButton.png")
    render2 = ImageTk.PhotoImage(load2)
    guessButton = TK.Button(guessLine, image = render2, command = getInput)
    guessButton.grid(row=0, column=1, padx=10)

    errorLabel = TK.Label(root, fg = "#FFFFFF", border = 0, font=("Times","14"))
    errorLabel.pack()


    root.mainloop()
