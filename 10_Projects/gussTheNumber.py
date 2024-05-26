import random

randomNumber = random.randint(1,5)
count = 0
flag = True
while flag :
    if(count < 3) : 
        count +=1
        num = int(input('Enter Number between 1 to 5 : '))
        if(randomNumber == num) :
            print('Voila you won the game')
            flag = False
        else :
            print('Try Again')
    else :
        print('Better Luck Next time')
        flag = False