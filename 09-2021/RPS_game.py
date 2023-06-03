# Rock paper scissor game
import random


ls = ['rock', 'paper', 'scissors']

User_pick = ''

#How many times you want to play
times = True
count = 0
while times:
    U_times = input("give a number how many times you want to play or type 'exit': ")

    if U_times == 'exit':
        print("The game will now exit")
        times = False
    else:
        U_times = int(U_times)

        for count in range(U_times):
            
            Comp_Pick = random.choice(ls)
            User_pick = input("Choose between 'rock', 'paper' or 'scissors' or 'exit' if you want to quit: ")

            if User_pick == "exit":
                print("The game will now exit")
                times = False
                break

            while User_pick not in ls:
                User_pick = input("Choose between 'rock', 'paper' or 'scissors' or 'exit' if you want to quit: ")
            
            if User_pick == "exit":
                print("The game will now exit")
                times = False
                break

            else:    
                if User_pick == 'rock' and Comp_Pick == 'scissors':
                    print(f"COM1 choice: {Comp_Pick}\nYou win!!!")
                    count += 1
                elif User_pick == 'rock' and Comp_Pick == 'paper':
                    print(f"COM1 choice: {Comp_Pick}\nYou lose!!!")
                    count += 1
                elif User_pick == 'rock' and Comp_Pick == 'rock':
                    print(f"COM1 choice: {Comp_Pick}\nIts a tie!!!")
                    count += 1
                elif User_pick == 'paper' and Comp_Pick == 'rock':
                    print(f"COM1 choice: {Comp_Pick}\nYou lose!!!")
                    count += 1
                elif User_pick == 'paper' and Comp_Pick == 'scissors':
                    print(f"COM1 choice: {Comp_Pick}\nYou lose!!!")
                    count += 1
                elif User_pick == 'paper' and Comp_Pick == 'paper':
                    print(f"COM1 choice: {Comp_Pick}\nIts a tie!!!")
                    count += 1
                elif User_pick == 'scissors' and Comp_Pick == 'rock':
                    print(f"COM1 choice: {Comp_Pick}\nYou lose!!!")
                    count += 1
                elif User_pick == 'scissors' and Comp_Pick == 'paper':
                    print(f"COM1 choice: {Comp_Pick}\nYou win!!!")
                    count += 1
                elif User_pick == 'scissors' and Comp_Pick == 'scissors':
                    print(f"COM1 choice: {Comp_Pick}\nIts a tie!!!")
                    count += 1
                print(f"You have played {count} times.")
            



