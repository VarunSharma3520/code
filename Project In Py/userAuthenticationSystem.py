userData = []
def signIn(userData):
  userName = input("Enter User Name: ")
  password = input("Enter password: ")
  logState = True
  userData.append([userName,password,logState])
  print("You Signed In Successfully")
  return userData
def signUp(userData):
  userName = input("Enter User Name: ")
  for i in range(len(userData)):
    if userData[i][0] == userName and userData[i][2] == True:
      print("Hi",userData[i][0])
    elif userData[i][0] == userName and userData[i][2] == False:
      print("Please Log In Again")
      signIn(userData)
    else:                   #userData[i][0] != userName:
      print("Your are missing")
      print("Please sign up again")
      signIn(userData)
  print("You Signed Up Successfully")
  return userData
def logOut(userData):
  userName = input("Enter User Name: ")
  for i in range(len(userData)):
    if userData[i][0] == userName:
      userData[i][2] == False
      print("You Logged Succesfully")
    else:
      print("You are missing")
  return userData
while True:
    print("""Press 1 for signIn
Press 2 for signUp
Press 3 for logOut
Press 4 for Quit""")
    userChoice = int(input("Enter your choice..."))
    if userChoice == 1:
      print("Fill Sign In Form")
      userData = signIn(userData)
    elif userChoice == 2:
        print("Fill Sign Up Form")
        userData = signUp(userData)
    elif userChoice == 3:
        userData = logOut(userData)
    elif userChoice == 4:
        print("Thank You for visiting")
        print("Hope You Liked Our service")
        break
    else:
        print("You Entered Wrong choice...")