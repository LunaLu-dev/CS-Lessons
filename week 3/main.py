# 1
x = 5
if x > 4:
  print(x)
else:
  print("Meow")

# 2
  
def indedtifyBlahaj(input: str) -> bool:
  if (input.__contains__('blahaj')):
    return True
  else:
    return False
  
user_input = input()
print(indedtifyBlahaj(user_input))


# 3
def sum_numbers(numbers):
  sum = 0

  for i in range(len(numbers)):
    print(f'{sum} + {numbers[i]} = {sum + numbers[i]}')
    sum = sum + numbers[i]

  print(sum)
  print('---------')


sum_numbers([2, 3, 4])

sum_numbers([
    35, 27, 81, 7, 69, 96, 43, 50, 27, 31, 12, 70, 25, 36, 23, 64, 58, 2, 100,
    53, 5, 31, 12, 15, 35, 59, 84, 64, 31, 25, 31, 25, 60, 80, 22, 23, 53, 13,
    13, 68, 77, 75, 32, 11, 97, 70, 5, 24, 18, 57, 12, 73, 46, 76, 57, 23, 71,
    49, 83, 44, 23, 41, 37, 86, 37, 58, 81, 33, 19, 81, 87, 22, 32, 50, 90, 25,
    99, 63, 64, 14, 56, 5, 11, 26, 7, 24, 60, 40, 36, 84, 38, 87, 73, 43, 66,
    62, 88, 58, 33, 93
])

# 4
from random import randint

fortyTwoCounter = 0

while(fortyTwoCounter < 6):
  value = randint(0, 100)
  print(value)
  if value == 42:
    print("The number 42 has been discoverd ⛏️")
    print("Your total 42 counter is", fortyTwoCounter)
    fortyTwoCounter = fortyTwoCounter + 1

print("The number 42 has been founf a total of 6 times")

# 5

def LowerHigher():

  value = randint(1, 100)
  lives = 10

  while(lives > 0):
    print("please guess a number between 1 and 100")
    user_input = input()
    if user_input.isnumeric():
      if int(user_input) > value:
        print("The value you are seeking is higher")
        lives = lives - 1
        print("You got ", lives, "left")
      elif int(user_input) < value:
        print("The Value you are seeking is lower")
        lives = lives - 1
        print("You got ", lives, "left")
      elif int(user_input) == value:
        print("Congratulation Yuo won, You Found the number 👑")
    else:
      print("Please Only input numbers")
      continue

  if(lives == 0):
    print("The number was ", value)
    print("You Lost, Wanna try again? y/n")
    awnser = input()
    if awnser == 'y' or awnser == 'yes':
      LowerHigher()
    else:
      print("Thanks for playing")

LowerHigher()


