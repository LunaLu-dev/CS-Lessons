import time
# Problem 1
# Call the following function 3 times with valid arguments.


def easy_sub(a, b) -> None:
  print(f"{a} - {b} = {a - b}")


x = 5.2
y = float("5.5")
z = 50

easy_sub(z, x)
easy_sub(y, z)
easy_sub(x, y)

# Problem 2
#   Receive 2 different numbers from the user.
#   Then call the function within problem 1 with those 2 numbers.

first_number = float(input())
print("First Number selected ", first_number)
second_number = float(input())
print("Second Number selected ", second_number)

easy_sub(first_number, second_number)

# Problem 3


def AskUserForNumber() -> None:
  user_input = int(input())
  WriteSillyStatement(user_input)


def WriteSillyStatement(input: int) -> None:
  print(f"A total of {input} trans fems is approaching your location")
  time.sleep(1)
  print("Start Running")


AskUserForNumber()

# Problem 4 (Challenge)

# You've been provided a couple of lists from Lucia, we've snuck these
# lists out of a super secret trans academy database. We need you to
# figure out a way of using internal python functions to sort the
# lists. Using libraries is okay as well.

top_bosses = ['Tizzy', 'Shay', '1b', 'Jaime', 'Brie', 'Ru', 'fluffy']

secret_codes = [1823, 9201, 8192, 1802, 9999, -2814, 6017]

passwords = [
  'password',
  'password123',
  'supersecret',
  'hunter882',
  'himomhimom',
  '12345678',
  'qwertyuio',
]

passwords.sort()
secret_codes.sort()
top_bosses.sort()

print("Database Status:")
time.sleep(0.5)
print("Hacked \n")

print("Lists:")
time.sleep(0.5)
print("Sorted \n")

print("Bosses:")
print(top_bosses, "\n\n")

time.sleep(0.5)

print("Super Secret Codes: ")
print(secret_codes, "\n\n")

time.sleep(0.5)

print("Passwords: ")
print(passwords, "\n\n")
