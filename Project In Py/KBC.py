level = 1213211
question = [
    "Which one of the following river flows between Vindhyan and Satpura ranges?",
    "The Central Rice Research Station is situated in?",
    "Who among the following wrote Sanskrit grammar?",
    "Which among the following headstreams meets the Ganges in last?",
    "The metal whose salts are sensitive to light is?",
    "Patanjali is well known for the compilation of –",
    "River Luni originates near Pushkar and drains into which one of the following?",
    "Which one of the following rivers originates in Brahmagiri range of Western Ghats?",
    "The country that has the highest in Barley Production?",
    "Tsunamis are not caused by"
    ]
option = [
    [
        "Narmada",
        "Mahanadi",
        "Son",
        "Netravati"],
    [
        "Chennai",
        "Cuttack",
        "Bangalore",
        "Quilon"
    ],
    [
        "Kalidasa",
        "Panini",
        "Charak",
        "Aryabhatt"
    ],
    [
        "Alaknanda",
        "Bhagirathi",
        "Mandakini",
        "Pindar"
    ],
    [
        "Zinc",
        "Silver",
        "Copper",
        "Aluminum"
    ],
    [
        "Yoga Sutra",
        "Panchatantra",
        "Brahma Sutra",
        "Ayurveda"
    ],
    [
        "Rann of Kachchh",
        "Arabian Sea",
        "Gulf of Cambay",
        "Lake Sambhar"
    ],
    [
        "Pennar",
        "Cauvery",
        "Krishna",
        "Tapti"
    ],
    [
        "China",
        "India",
        "Russia",
        "France"
    ]
    ]
answer = [
    "Narmada",
    "Cuttack",
    "Panini",
    "Bhagirathi",
    "Silver",
    "Yoga Sutra",
    "Rann of Kachchh",
    "Cauvery",
    "Russia",
    "Hurricanes",
    "narmada",
    "cuttack",
    "panini",
    "bhagirathi",
    "silver",
    "Yoga Sutra",
    "yoga sutra",
    "Yoga sutra",
    "yoga Sutra",
    "rann of Kachchh",
    "rann Of Kachchh",
    "rann of kachchh",
    "cauvery",
    "russia",
    "hurricanes"
]
def showQuestion(pos):
    numbering = 1
    print(question[pos])
    for i in option[pos]:
        print(numbering,i)
        numbering += 1
    input("Press Enter To Move A head...")

def answerChecker(pos,ans):
    if ans in answer:
        return True
    else:
        False

def showLifeLine(pos):
    lifeLineChoice = eval(input("""Press 1 for flip the Question
Press 2 for 50 - 50"""))
    if lifeLineChoice == 1:
        showQuestion(i+1)
    elif lifeLineChoice == 2:
        print("\n***Option 3 and 4 are incorrect***\n")
        showQuestion(pos)
        answer = input("Enter You choice : ")
        if answerChecker(answer,ans) == True:
            print("You answer is correct...")
            level += 1
        else:
            if level > 4:
                print("You will get 4000 inr only")
            else:
                print("You will not get any money")
            print("Sorry! You entered wrong answer...")
    else:
        print("You entered wrong choice...")
    
        
# first Question
print("Welcome to KBC")
print("Question for",level*1000,"inr")
print("Q:->")
showQuestion(0)
ans = input("Enter you choice number : ")
if answerChecker(0,ans) == True:
    level += 1
    print("You Enter Correct Answer....")
    # Iterates from second to ten
    for i in range(1,10):
        print("Question for",level*1000,"inr")
        print("Q:->")
        showQuestion(i)
        playChoice = int(input("""\n\n\nDo You Want To Play Again?
Press 1 for Play
Press 2 for Life Line
Press 0 for Quit\n\n\n"""))
        if playChoice == 1:
            answer = input("Enter you choice : ")
            if answerChecker(i,answer) == True:
                print("You answer is correct...")
                level += 1
            else:
                if level > 4:
                    print("You will get 4000 inr only")
                else:
                    print("You will not get any money")
                print("Sorry! You entered wrong answer...")
                break
        elif playChoice == 0:
            print("Thank You! Hope you enjoyed this game...")
        elif playChoice == 2:
            showLifeLine(i)
else:
    print("Sorry! You entered wrong answer...")
