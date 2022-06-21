import random
g = int(input("ODD OR EVEN?\nPress 1 : Odd & 2 : Even\t"))
g = g%2
while 1:
    m = input("Toss")
    if len(m) == 0:
        print("Try again")
    elif ord(m)>54 or ord(m)<49:
        print("Not a choice !")
    else:
        n = int(m)
        num = random.randint(1,6)
        n = n + num
        break
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
score1 = 0
score2 = 0
while 1:
    m = input()
    if len(m) == 0:
        print("Try again")
    elif ord(m)>54 or ord(m)<49:
        print("Not a choice fool")
    else:
        n = int(m)
        num = random.randint(1,6)
        print("YOU  PC")
        print(n," ",num)
        if n == num:
            if h == 1:
                print("Out! You scored ", score1, "runs. Your turn to bowl")
            else:
                print("Out! PC scored ", score2, "runs. Your turn to bat")
            break
        else:
            if h == 1:
                score1 = score1 + n
            else:
                score2 = score2 + num
flag = 0
while 1:
    m = input()
    if len(m) == 0:
        print("Try again")
    elif ord(m)>54 or ord(m)<49:
        print("Not a choice !")
    else:
        n = int(m)
        num = random.randint(1,6)
        print("YOU  PC")
        print(n," ",num)
        if n == num:
            break
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
