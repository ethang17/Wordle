import random

possibleGuessFile = open("U:\\pyProjects\\pyProjects\\combined_wordlist.txt", "r")
possibleGuessList = possibleGuessFile.readlines()
possibleGuessFile.close()

possibleAnswerFile = open("u:\\pyProjects\\pyProjects\\shuffled_real_wordles.txt", "r")
possibleAnswerList = possibleAnswerFile.readlines()
possibleAnswerFile.close()

def inCombined(word):
    for entry in possibleGuessList:
        if word == entry.strip():
            return True
def score(guess, answer):
    results=["","","","",""]
    for x in range(5):
        if guess[x] == answer[x]:
            results[x] = guess[x]+"(G)" 
        elif guess[x] == answer[0] or guess[x]==answer[1]or guess[x]==answer[2]or guess[x]==answer[3]or guess[x]==answer[4]:
            results[x] = guess[x] +"(Y)"
        else:
            results[x] = guess[x]
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
