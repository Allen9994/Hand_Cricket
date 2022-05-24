import random
g = int(input("ODD OR EVEN?\n Odd : 1 Even : 2\t"))
g = g%2
flag = 0
while flag == 0:
    m = input("Toss")
    if len(m) == 0:
        print("Try again")
    elif ord(m)>54 or ord(m)<49:
        print("Not a choice fool")
    else:
        n = int(m)
        num = random.randint(1,6)
        n = n + num
        flag = 1
if n % 2 == g:
    print("Your toss won",n-num," ",num)
    g = int(input("Batting or bowling?\n Batting : 1 Bowling : 2\t"))
    h = g%2
    if h == 1:
        print("You chose batting first")
    else:
        print("You chose bowling first")
else:
    print("PC's toss won!",n-num," ",num)
    h = random.randint(0,1)
    if h == 0:
        print("PC chose to bat first")
    else:
        print("PC chose to bowl first")
flag = 0
score1 = 0
score2 = 0
while flag == 0:
    m = input()
    if len(m) == 0:
        print("Try again")
    elif ord(m)>54 or ord(m)<49:
        print("Not a choice fool")
    else:
        n = int(m)
        num = random.randint(1,6)
        print(n," ",num)
        if n == num:
            flag = 1
            if h == 1:
                print("Out! Your turn to bowl. Your runs: " ,score1)
            else:
                print("Out! Your turn to bat. PC's runs: ",score2)
            break
        else:
            if h == 1:
                score1 = score1 + n
            else:
                score2 = score2 + num
flag = 0
while flag == 0:
    m = input()
    if len(m) == 0:
        print("Try again")
    elif ord(m)>54 or ord(m)<49:
        print("Not a choice fool")
    else:
        n = int(m)
        num = random.randint(1,6)
        print(n," ",num)
        if n == num:
            flag = 1
        else:
            if h == 1:
                score2 = score2 + num
                if score1<score2:
                    break
            else:
                score1 = score1 + n
                if score2<score1:
                    break
        
if score1>score2:
    print("Game Over! YOU WIN!!!! Your score:",score1,"  Pc score: ",score2)
else:
    print("Game Over! YOU LOST!!!! Your score:",score1,"  Pc score: ",score2)
input("Press any key to exit!")