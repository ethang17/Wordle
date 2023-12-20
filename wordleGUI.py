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

def setError(errorText):
    errorLabel.configure(text=errorText)

def getInput():
    global win
    global guessed

    setError("")
    #while win == False:
    print("---")
    typed = guessEntry.get()
    print(guessEntry.get())
    print("TYPED: "+typed)
    if len(typed) != 5:
        setError("Error: Your guess should be five letters.")
        print("1")
    elif not typed.isalpha():
        setError("Error: Your guess should only include letters.")
        print("2")
    elif not inCombined(typed.lower()):
        setError("Error: Your guess is not in the word list.")
        print("3")
    else:
        guessed = typed.upper()
        print("4")
    guessEntry.delete(0,"end" )
        

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

#Window
    root = TK.Tk()
    root.geometry("500x800")
    root.title("Wordle Remake")
    root.configure(bg = "#4D4D4D", borderwidth=0)

#Banner
    load = Image.open("wordleBanner.jpeg")
    render = ImageTk.PhotoImage(load)
    banner = TK.Label(root, image=render,bg="#dddddd", border=0 )
    banner.pack()
#Guess System
    #Guess Entry
    guessLine = TK.Frame(root, height = 75, width = 500, bg="#4d4d4d")
    guessLine.pack()
    guessEntry = TK.Entry(guessLine, font=("Times","18"))
    guessEntry.insert(0, "GUESS")
    guessEntry.grid(row =0, column=0)
    #Guess Button
    load2 = Image.open("guessButton.png")
    render2 = ImageTk.PhotoImage(load2)
    guessButton = TK.Button(guessLine, image = render2, command = getInput)
    guessButton.grid(row=0, column=1, padx=10)
#Error Display
    errorLabel = TK.Label(root, fg = "#FFFFFF", border = 0, font=("Times","14"), bg="#4d4d4d")
    errorLabel.pack()

#First Guess Line
    firstFrame = TK.Frame(root, border=0)
    loadFrame1 = Image.open("frames.jpeg")
    renderFrame1 = ImageTk.PhotoImage(loadFrame1)
    firstFrameLabel = TK.Label(firstFrame, image = renderFrame1, border=0)
    firstFrameLabel.pack()
    firstFrame.pack()
    #Guess Letter Labels
    l11 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l11.create_text(33, 37, text="W", fill="#FFF", font=('CourierNew 40 bold'))

    l11.place(x=56, y = 195)

#Second Guess Line
    secondFrame = TK.Frame(root, border=0)
    secondFrameLabel = TK.Label(secondFrame, image = renderFrame1, border=0)
    secondFrameLabel.pack()
    secondFrame.pack()

#Third Guess Line
    thirdFrame = TK.Frame(root, border=0)
    secondFrameLabel = TK.Label(secondFrame, image = renderFrame1, border=0)
    secondFrameLabel.pack()
    secondFrame.pack()

#Fourth Guess Line
    secondFrame = TK.Frame(root, border=0)

    secondFrameLabel = TK.Label(secondFrame, image = renderFrame1, border=0)
    secondFrameLabel.pack()
    secondFrame.pack()

#Fifth Guess Line
    secondFrame = TK.Frame(root, border=0)

    secondFrameLabel = TK.Label(secondFrame, image = renderFrame1, border=0)
    secondFrameLabel.pack()
    secondFrame.pack()
    root.mainloop()
