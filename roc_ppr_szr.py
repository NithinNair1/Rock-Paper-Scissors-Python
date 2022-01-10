import random

choice=0

def Play():
  maxVal=int(input("\nMaximum possible score: "))
  runCount = 0
  compCount = 0
  userCount = 0
  choicesPlay = ['r','p','s']
  while compCount!=maxVal and userCount!=maxVal:
    runCount += 1
    print("\n––––––––––––– Run",runCount,"–––––––––––––")
    userChoice = input("Rock Paper Scissors: ")
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
    print("––––––––––––––––––––––––––")

  if userCount>compCount:
    print("\nYAYY!!! You Won")
    print("You:",userCount,"\nComputer:",compCount)
    print("\n")


  else:
    print("\nUnfortunately You Lost...")
    print("You:",userCount,"\nComputer:",compCount)
    print("\n")




while choice != 4:
  print("Select an option: \n1.)Play\n2.)Highscores\n3.)Rules of Play\n4.)Exit")
  choice=input("Enter Your Choice: ")
  choice=int(choice)
  if choice==1:
    Play()
  elif choice==2:
    print("Working on that")
  elif choice==3:
    print("Working on that")
  else:
    print("Bye..")
    exit()

