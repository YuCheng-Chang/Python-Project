try:
    with open("highscore.txt", "r") as f:
        highscore = f.read()
        highscore = int(highscore)
        print("The highest score previously was ")
        print(highscore)
except FileNotFoundError:
    with open("highscore.txt", 'w') as f:
        highscore=0
        print("The highest score previously was \n0")
        f.write(str(0))
c=True
while c:
    score=0
    print("Welcome to the Maths Quiz")
    print("Can you answer three questions and score maximum points?")
    print("Question 1: What is the product of 2x2x2?")
    answer = int(input(""))
    if answer == 8:
        print("Correct")
        score = score + 1
        print("Your score is ", score)
    else:
        print("Incorrect, the answer is 8")
        print("Your score is ", score)
    print("Question 2: What is the product of 2+2+2?")
    answer = int(input(""))
    if answer == 6:
        print("Correct")
        score = score + 1
        print("Your score is ", score)
    else:
        print("Incorrect, the answer is 6")
        print("Your score is ", score)
    print("Question 3: What is the product of 1x1x1?")
    answer = int(input(""))
    if answer == 1:
        print("Correct")
        score = score + 1
        print("Your score is ", score)
    else:
        print("Incorrect, the answer is 1")
        print("Your score is ", score)
    if score >= highscore:
        highscore = score
        with open("highscore.txt",'w') as f:
            f.write(str(highscore))
    print("The highscore is " + str(highscore))
    print("Continue or not?(y/n)")
    if(input("") == 'y'):
        c=True
    else:
        c=False