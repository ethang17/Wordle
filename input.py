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
    resultsAll = scoreY(guess, resultsG)
    return resultsAll
def scoreG(guess, answer):
    resultsG=["","","","",""]
    for x in range(5):
        if guess[x] == answer[x]:
            resultsG[x] = guess[x]+"(G)" 
        else:
            resultsG[x] = guess[x]
    return resultsG
def scoreY(guess,resultsG):
    resultsAll=["","","","",""]
    for x in range(5):
        if guess[x] == resultsG[0] or guess[x]==resultsG[1]or guess[x]==resultsG[2]or guess[x]==resultsG[3]or guess[x]==resultsG[4]:
            resultsAll[x] = guess[x] +"(Y)"
        else:
            resultsAll[x] = resultsG[x]
    return resultsAll



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
