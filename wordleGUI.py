import tkinter as TK
from PIL import Image, ImageTk
import random

possibleGuessFile = open("combined_wordlist.txt", "r")
possibleGuessList = possibleGuessFile.readlines()
possibleGuessFile.close()

possibleAnswerFile = open("shuffled_real_wordles.txt", "r")
possibleAnswerList = possibleAnswerFile.readlines()
possibleAnswerFile.close()

guessNumber = 0
guessList = []
canvasList = []

answer = ""
win = False
guessed = ""

def setError(errorText):
    errorLabel.configure(text=errorText)

def score(guess, answer):
    answerList = list(answer)
    resultsG = scoreG(guess, answerList)[0]
    answersList = scoreG(guess, answerList)[1]
    resultsY = scoreY(guess, answersList)
    resultsAll = merge(resultsG, resultsY, guess)
    return resultsAll


def scoreG(guess, answer):
    resultsG=["","","","",""]
    for x in range(5):
        if guess[x] == answer[x]:
            resultsG[x] = guess[x]+"(G)" 
            answer[x] = ""
        else:
            resultsG[x] = guess[x]
    return [resultsG, answer]

def scoreY(guess,answer):
    resultsY=["","","","",""]
    for x in range(5):
        if guess[x] == answer[0] or guess[x]==answer[1]or guess[x]==answer[2]or guess[x]==answer[3]or guess[x]==answer[4]:
            resultsY[x] = guess[x] +"(Y)"
            answer[x] = ""
        else:
            resultsY[x] = guess[x]
    return resultsY

def merge(g, y, guess):
    results = ["","","","",""]
    for i in range(5):
        if "(G)" in g[i]:
            results[i] = g[i]
        elif "(Y)" in y[i]:
            results[i] = y[i]
        else:
            results[i] = guess[i]
    return results

def getInput():
    global win
    global guessed
    global guessNumber
    global guessList
    if win==True:
        print("win")
        return
    elif guessNumber>=5:
        print("lose")
        return

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
        guessed = score(guessed, answer)
        guessList.append(guessed)
        displayList()
    guessEntry.delete(0,"end" )
    

def displayList():
    global guessNumber
    global guessed
    global canvasList

    for j in range(len(guessList[guessNumber])):
        canvasList[guessNumber][j].create_text(33, 37, text=guessed[j], fill="#FFF", font=('CourierNew 40 bold'))
    guessNumber += 1
        

def getAnswer():
    global answer
    answerIndex = random.randint(0, len(possibleAnswerList))
    answer = possibleAnswerList[answerIndex].strip()
    answer = answer.upper()
    print(answer)

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
    firstCanvas=[]
    l11 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l11.place(x=56, y = 195)
    firstCanvas.append(l11)

    l12 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l12.place(x=136, y = 195)
    firstCanvas.append(l12)

    l13 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l13.place(x=216, y = 195)
    firstCanvas.append(l13)

    l14 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l14.place(x=296, y = 195)
    firstCanvas.append(l14)

    l15 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l15.place(x=376, y = 195)
    firstCanvas.append(l15)

    canvasList.append(firstCanvas)

#Second Guess Line
    secondFrame = TK.Frame(root, border=0)
    secondFrameLabel = TK.Label(secondFrame, image = renderFrame1, border=0)
    secondFrameLabel.pack()
    secondFrame.pack()
    #Guess Letter Labels
    secondCanvas=[]
    l21 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l21.place(x=56, y = 295)
    secondCanvas.append(l21)

    l22 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l22.place(x=136, y = 295)
    secondCanvas.append(l22)

    l23 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l23.place(x=216, y = 295)
    secondCanvas.append(l23)

    l24 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l24.place(x=296, y = 295)
    secondCanvas.append(l24)

    l25 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l25.place(x=376, y = 295)
    secondCanvas.append(l25)

    canvasList.append(secondCanvas)

#Third Guess Line
    thirdFrame = TK.Frame(root, border=0)
    thirdFrameLabel = TK.Label(secondFrame, image = renderFrame1, border=0)
    thirdFrameLabel.pack()
    thirdFrame.pack()
    #Guess Letter Labels
    thirdCanvas=[]
    l31 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l31.place(x=56, y = 395)
    thirdCanvas.append(l31)

    l32 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l32.place(x=136, y = 395)
    thirdCanvas.append(l32)

    l33 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l33.place(x=216, y = 395)
    thirdCanvas.append(l33)

    l34 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l34.place(x=296, y = 395)
    thirdCanvas.append(l34)

    l35 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l35.place(x=376, y = 395)
    thirdCanvas.append(l35)

    canvasList.append(thirdCanvas)
#Fourth Guess Line
    fourthFrame = TK.Frame(root, border=0)
    fourthFrameLabel = TK.Label(secondFrame, image = renderFrame1, border=0)
    fourthFrameLabel.pack()
    fourthFrame.pack()
    #Guess Letter Labels
    fourthCanvas=[]
    l41 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l41.place(x=56, y = 495)
    fourthCanvas.append(l41)

    l42 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l42.place(x=136, y = 495)
    fourthCanvas.append(l42)

    l43 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l43.place(x=216, y = 495)
    fourthCanvas.append(l43)

    l44 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l44.place(x=296, y = 495)
    fourthCanvas.append(l44)

    l45 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l45.place(x=376, y = 495)
    fourthCanvas.append(l45)

    canvasList.append(fourthCanvas)

#Fifth Guess Line
    fifthFrame = TK.Frame(root, border=0)

    fifthFrameLabel = TK.Label(secondFrame, image = renderFrame1, border=0)
    fifthFrameLabel.pack()
    fifthFrame.pack()
    #Guess Letter Labels
    fifthCanvas=[]
    l51 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l51.place(x=56, y = 595)
    fifthCanvas.append(l51)

    l52 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l52.place(x=136, y = 595)
    fifthCanvas.append(l52)

    l53 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l53.place(x=216, y = 595)
    fifthCanvas.append(l53)

    l54 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l54.place(x=296, y = 595)
    fifthCanvas.append(l54)

    l55 = TK.Canvas(root, height= 68, width = 68, bg = "#4d4d4d", highlightthickness=0)
    l55.place(x=376, y = 595)
    fifthCanvas.append(l55)

    canvasList.append(fifthCanvas)
    root.mainloop()
