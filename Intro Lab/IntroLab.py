import time, random

def solveExpression(e):
    # This function returns the solution of a string expression.
    return eval(e)

def makeExpression(i, j, op):
    # This function returns the string representing the expression.
    return str(i) + op + str(j)

def makeOp():
    # This function returns a character representing math operators: + (addition), - (subtraction), or * multiplication.
    index = random.randint(0,2)
    x = ['+', '-', '*']
    return x[index]

def checkGuess(guess, soln, score):
    # This function return true if guess == soln; false otherwise.
    if guess == soln:
        score += 1
        print("Correct!\n")
    else:
        print("Incorrect.\n")
    return score

def printExpression(arg1, arg2, op):
    # This function prints the expression where arg1 & arg2 are integers and op is a string operator:
    # "+", "-", or "*".
    print("\t", arg1)
    print(op, "\t", arg2)
    print("---------")

def startTimer():
    # This function returns the current time.
    return time.time()

def stopTimer(startTime):
    # This function takes the start time and returns the current time minus the start time.
    return time.time() - startTime

# score is a variable that will store number of correct guesses
# we initialize this to zero
score = 0

# variable "runs" hold the number of times the expression will be presented to user
runs = 5

# The startTimer() function returns the current time in seconds
# we store that value in the variable startTime
startTime = startTimer()

print("**********************************"
      "* Flash Cards *"
      "**********************************")

# Everything inside this for statement (we can tell by the indentation)
# will be executed "runs" times
for i in range(runs):
    arg1 = random.randint(1,10)
    arg2 = random.randint(1,10)
    op = makeOp()

    # makes expression of type: string
    exp = makeExpression(arg1, arg2, op)
    printExpression(arg1, arg2, op)

    # stores solution in variable: soln
    soln = solveExpression(exp)

    # gets guess from user
    guess = int(input("=\t"))

    # the checkGuess() function checks the user's guess and
    # updates the score
    # the score holds the amount of correct guesses
    score = checkGuess(guess, soln, score)

totalTime = stopTimer(startTime)
# totalTime variable now holds the amount of time since the game started

print("**********************************"
      "* Game Over *"
      "**********************************")
print("Your score:")
print(score, "/ 5")
print("In", totalTime, "seconds.")
print("**********************************")
