import operator
player=[{'name':'Amy' ,'score':0},
        {'name':'John','score':0},
        {'name':'Zoe' ,'score':0}
        ]
try:
    with open("score.txt", "r") as f:
        highscore = f.readline()
        highscore = int(highscore)
        for line in f:
            line = line.strip("\n")
            line = line.split(" ")
            for p in player:
                if p['name']==line[0]:
                    p['score']=int(line[1])

except FileNotFoundError:
    with open("score.txt", 'w') as f:
        highscore=0
        f.write(str(highscore)+'\n')
        for p in player:
            f.write(p['name'] + " " + str(p['score'])+'\n')
print("The highest score previously was \n"+str(highscore))
print(player)

playerCnt=0
for p in player:
    score=0
    print("Hi {""}, welcome to the Maths Quiz".format(p['name']))
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
        with open("score.txt",'w') as f:
            f.write(str(highscore))
    print("The highscore is " + str(highscore))
    p['score']=score
    print('----------------------------------------------')
player=sorted(player,key=operator.itemgetter('score'))
with open("score.txt", "w") as f:
    f.write(str(highscore)+'\n')
    for p in player:
        f.write(p['name']+" "+str(p['score'])+'\n')