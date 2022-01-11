import random

choice=0

gameLogic = {'r':'p','p':'s','s':'r'}
gameDifficulty = 1
gameDifficultyWords = {1:'Easy',2:'Difficult',3:'Impossible'}
def Play(n):
  maxVal=int(input("\nMaximum possible score: "))
  runCount = 0
  compCount = 0
  userCount = 0
  choicesPlay = ['r','p','s']
  while compCount!=maxVal and userCount!=maxVal:
    choicesPlay = ['r','p','s']
    print(type(choicesPlay))
    runCount += 1
    print("\n––––––––––––– Run",runCount,"–––––––––––––")
    userChoice = input("Rock Paper Scissors: ")
    if n==1:
      choicesPlay = ['r','p','s']
    elif n==2:
      choicesPlay = choicesPlay+list(gameLogic[userChoice])
    elif n==3:
      choicesPlay = choicesPlay+list(gameLogic[userChoice])+list(gameLogic[userChoice])+list(gameLogic[userChoice])

    compChoice = random.choice(choicesPlay)
    if userChoice == compChoice:
      print(userChoice,"vs",compChoice)
      print("No Result")
      continue
    elif userChoice == 'r' and compChoice == 'p':
      print(userChoice,"vs",compChoice)
      print("Paper (Computer) Wins")
      compCount+=1
      print("You:",userCount,"\nComputer:",compCount)


    elif userChoice == 'p' and compChoice == 'r':
      print(userChoice,"vs",compChoice)
      print("Paper (User) Wins")
      userCount+=1
      print("You:",userCount,"\nComputer:",compCount)


    elif userChoice == 'r' and compChoice == 's':
      print(userChoice,"vs",compChoice)
      print("Rock (User) Wins")
      userCount+=1
      print("You:",userCount,"\nComputer:",compCount)

    elif userChoice == 's' and compChoice == 'r':
      print(userChoice,"vs",compChoice)
      print("Scissors (Computer) Wins")
      compCount+=1
      print("You:",userCount,"\nComputer:",compCount)

    # Rock both done

    elif userChoice == 's' and compChoice == 'p':
      print(userChoice,"vs",compChoice)
      print("Paper (User) Wins")
      userCount+=1
      print("You:",userCount,"\nComputer:",compCount)

    # Paper both done

    elif userChoice == 'p' and compChoice == 's':
      print(userChoice,"vs",compChoice)
      print("Paper (Computer) Wins")
      compCount+=1
      print("You:",userCount,"\nComputer:",compCount)

    # Scissors both done

    else:
      print("ERROR! u:",userChoice,"c:",compChoice)
    print("––––––––––––––––––––––––––––––––––")

  if userCount>compCount:
    print("\nYAYY!!! You Won")
    print("You:",userCount,"\nComputer:",compCount)
    print("\n")


  else:
    print("\nUnfortunately You Lost...")
    print("You:",userCount,"\nComputer:",compCount)
    print("\n")


def Rules():
  print("––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
  print("Welcome to Rock Paper Scissors.")
  print("Rock == r \nPaper == p \nScissors == s")
  print("Puter will ask you Maximum Number of Score to win the Game.")
  print("––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")


while choice != 5:
  gameMode=1
  print("Select an option: \n1.)Play\n2.)Highscores\n3.)Game Difficulty\n4.)Rules of Play\n5.)Exit")
  choice=input("Enter Your Choice: ")
  choice=int(choice)
  if choice==1:

    Play(gameDifficulty)
  elif choice==2:
    print("Working on that")
  elif choice==3:
    print("\n––––––––––––––––––––––––––––––––––––––––––")
    print("Game Difficulty:\n1.)Easy\n2.)Difficult\n3.)Impossible")
    gameDifficulty=int(input("Enter Game Difficulty: "))
    print("Game Difficulty set to",str(gameDifficultyWords[gameDifficulty]))
    print("––––––––––––––––––––––––––––––––––––––––––\n")

  elif choice==4:
    Rules()
  else:
    print("Bye..")
    exit()

