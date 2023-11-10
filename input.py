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
    resultsG = scoreG(guess, answer)
    print(resultsG)
    print("G^")
    resultsY = scoreY(guess, answer)
    resultsYNoMult = removeMultiples(answer, resultsY)
    resultsAll = merge(resultsG, resultsYNoMult, guess)
    return resultsAll

def scoreG(guess, answer):
    resultsG=["","","","",""]
    for x in range(5):
        if guess[x] == answer[x]:
            resultsG[x] = guess[x]+"(G)" 
        else:
            resultsG[x] = guess[x]
    return resultsG

def scoreY(guess,answer):
    resultsY=["","","","",""]
    for x in range(5):
        if guess[x] == answer[0] or guess[x]==answer[1]or guess[x]==answer[2]or guess[x]==answer[3]or guess[x]==answer[4]:
            resultsY[x] = guess[x] +"(Y)"
        else:
            resultsY[x] = guess[x]
    return resultsY

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

if __name__ == "__main__":
    answer = getAnswer()
    print(answer)
    guessed = ""
    guessList=[]

    print("Welcome to Wordle!\nWhat is your first guess?")
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
            guessed = typed
    guessList.append(score(guessed, answer))
    print(guessList)
