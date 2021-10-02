import random
print("This is a dice stimulator")

x="y"
while x=="y":
      num=random.randint(1,3)
      if num==1:
          print(" ______")
          print("|      |")
          print("|   O  |")
          print("|______|")
      if num==2:
          print(" ______")
          print("|      |")
          print("| O  O |")
          print("|______|")
      if num==3:
          print(" _______")
          print("|   O   |")
          print("|   O   |")
          print("|___O___|")
      if num==4:
          print(" ________")
          print("| O   O  |")
          print("|        |")
          print("|_O___O__|")
      if num==5:
          print(" ________")
          print("| O   O  |")
          print("|   O    |")
          print("|_O___O__|")
      if num==6:
          print(" ________")
          print("| O O O  |")
          print("| O O O  |")
          print("|_O_O_y"
                "O__|")


      x=input("Press y to roll again")
