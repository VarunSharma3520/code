import random
result = [0,0]
# result[you,cpu]
def play(result):
    print("""Press 1 for rock
Press 2 for paper
Press 3 for scissor""")
    user_input = int(input("Enter Your input"))
    cpu = random.choices([1,2,3], k=1)[0]
    
    # for draw
    if user_input == cpu:
        if user_input == 1:
            print("Match Draw you and cpu choosen rock")
        elif user_input == 2:
            print("Match Draw you and cpu choosen paper")
        else:
            print("Match Draw you and cpu choosen scissor")


    if user_input == 1:
        print("you: rock")
        if cpu == 2:
            print("cpu: paper")
            print("You loose")
            result[1] += 1 
            input("Press Enter Key....")
        else:
            print("cpu: scissor")
            print("You won")
            result[0] += 1
            input("Press Enter Key....")

            
    elif user_input == 2:
        print("you: paper")
        if cpu == 1:
            print("cpu: rock")
            print("You win")
            result[0] += 1
            input("Press Enter Key....")

        else:
            print("cpu: scissor")
            print("You loose")
            result[1] += 1 
            input("Press Enter Key....")

    else:
        print("you: scissor")
        if cpu == 1:
            print("cpu: rock")
            print("You loose")
            result[1] += 1
            input("Press Enter Key....")

        else:
            print("cpu: paper")
            print("You win")
            result[0] += 1
            input("Press Enter Key....")

    return result
while True:
    print("""Press 1 to play
Press 0 for Quit""")
    user_input = int(input("Enter your choice..."))
    if user_input == 1:
        result = play(result)
    elif user_input == 0:
        print("Your Score:",result[0])
        print("CPU Score:",result[1])
        input("Press Enter Key....")

        if result[0] > result[1]:
            print("You Won")
            input("Press Enter Key....")

        elif result[0] < result[1]:
            print("You loose")
            input("Press Enter Key....")

        else:
            print("Match Draw")
            input("Press Enter Key....")

        break
if result != [0,0]:
    print("Thank You For Playing")