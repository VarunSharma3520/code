amount = 0
level = 1
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
        "NARMADA",
        "MAHANADI",
        "SON",
        "NEtravati"],
    [
        "Chennai",
        "Cuttack",
        "Bangalore",
        "Quilon"
    ],
    [
        "Kalidasa",
        "Charak",
        "Panini",
        "Aryabhatt"
    ],
    [
        "Alaknanda",
        "Pindar",
        "Mandakini",
        "Bhagirathi"
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
    "Hurricanes"
]
def showQuestion(pos):
    numbering = 1
    print(question[pos])
    for i in option[pos]:
        print(numbering,i)
        numbering += 1

def answerChecker(pos,answer):
    if answer in option[pos]:
        return True
    else:
        False


# first Question
print("Welcome to KBC")
print("Question for",level*1000,"inr")
print("Q:->")
showQuestion(0)
answer = input("Enter you choice number : ")
if answerChecker(0,answer) == True:
    level += 1
    # Iterates from second to ten
    for i in range(1,10):
        playChoice = int(input("""\n\n\nDo You Want To Play Again?
Press 1 for Play
Press 0 for Quit\n\n\n"""))
        if playChoice == 1:
            print("Question for",level*1000,"inr")
            print("Q:->")
            showQuestion(i)
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
else:
    print("Sorry! You entered wrong answer...")