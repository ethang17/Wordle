import random

possibleGuessFile = open("combined_wordlist.txt", "r")
possibleGuessList = possibleGuessFile.readlines()
possibleGuessFile.close()

possibleAnswerFile = open("shuffled_real_wordles.txt", "r")
possibleAnswerList = possibleAnswerFile.readlines()
possibleAnswerFile.close()

def inCombined(word):
    for entry in possibleGuessList:
        if word == entry.strip():
            return True
        

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
'''
def removeMultiples(answer, resultsY):
    for i in range(5):
        currentLetter = answer[i]
        currentLetterCount = 0
        for j in range(5):
            if answer[j] == currentLetter:
                currentLetterCount+=1
                print(currentLetter +": "+str(currentLetterCount))

        currentLetterYellows = 0
        for k in range(5):
            if resultsY[k] == (currentLetter + "(Y)"):
                currentLetterYellows+=1
                print(currentLetter + "(Y): "+str(currentLetterYellows))
                if currentLetterYellows > currentLetterCount:
                    resultsY[k] = currentLetter
        print(resultsY)
    return resultsY
'''
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

def getAnswer():
    answerIndex = random.randint(0, len(possibleAnswerList))
    answer = possibleAnswerList[answerIndex].strip()
    return answer

def checkWin(currentGuessResult):
    foundLetters = 0
    for x in currentGuessResult:
        found = x.find("(G)")
        if found > 0:
            foundLetters +=1
    print(foundLetters)
    if foundLetters >=5:
        return True
    else:
        return False



if __name__ == "__main__":
    answer = getAnswer().upper()
    print(answer)
    guessed = ""
    guessList=[]
    win = False
    print("Welcome to Wordle!\nWhat is your first guess?")
    while win == False:
        while guessed == "":
            print("---")
            typed = input()
            if len(typed) != 5:
                print("Error: Your guess should be five letters.")
            elif not typed.isalpha():
                print("Error: Your guess should only include letters.")
            elif not inCombined(typed):
                print("Error: Your guess is not in the word list.")
            else:
                guessed = typed.upper()
        currentGuessResult = score(guessed, answer)
        guessed=""
        win = checkWin(currentGuessResult)
        guessList.append(currentGuessResult)
        print(guessList)
