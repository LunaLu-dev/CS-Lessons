#1 (lists)
animals_in_pen = []

for i in range(0, 5):
  print("What is a cute animal?")
  user_animal = input()
  animals_in_pen.append(user_animal)
  print(f"The cute zoo now has a new member {user_animal} meet {animals_in_pen[0:i]}!")
print()
print("Yay you have now filled the cute Zoo with all the animals it can fit, sooo cute")
print(f"Sooo the zoo now has {animals_in_pen}, thank you")
print()
print(f"But sadly enoght its time for {animals_in_pen[len(animals_in_pen) - 1]} to get to sleep")
animals_in_pen.pop()
print(f"The remaing animals in the zoo is {animals_in_pen}!")

#2 (dictionary)

animals = {
  "Lightening Whisker": "Black and White",
  "Shadow Spark": "Black and White",
  "Black Paw": "Black",
  "Snow Drop": "White"
}

for i in range(0, 5):
  print("Please Enter an animal")
  user_input = input()

  if(user_input in animals):
    print(f"Oh I know that animal, it's the {animals[user_input]} one!")
  else:
    print("Oh I don't know this animal, would you tell me what color this animal is?")
    user_input_color = input()
    animals[user_input] = user_input_color
    print("Thank you for teaching me a new animal ^^")
print()
print("Thank you for teaching me all these new animals")
print(f"I have now learned the color of all {animals.keys()}")
print("--- Memory corruption... xP ---")
del animals['Snow Drop']
print(f"I have now learned the color of all {animals.keys()}")
  


#3 (sets)

shorks_found = set()
shorks = ["pink","purple","pink","red","white","yellow","white","purple","white","blue","black","pink","red","white","purple","purple","red","blue","black","purple","red","blue","red","pink","pink","blue","purple","white","white","red","blue","white","purple","black","black","black","white","pink","pink","blue","pink","black","black","blue","pink","pink","black","yellow","white","yellow","blue","pink","white","white","red","purple","black","blue","pink","black","red","yellow","magenta","pink","blue","purple","white","yellow","red","black","purple","pink","purple","white","pink","white","red","pink","white","pink","black","black","red","white","red","red","blue","white","hazel","yellow","blue","purple","white","red","red","yellow","yellow","yellow","yellow","black","pink","yellow","purple","blue","red","black","white","red","pink","blue","red","yellow","yellow","red","purple","purple","white","blue","blue","purple"]

for shork in shorks:
  
  shorks_found.add(shork)


for shork in shorks_found:
  print(f"{shork} shork is a real shork, be careful out there")
  print(f"{shork} shork has ben added to your inventory 🦈")

#4

from random import randint

sharks = ["green", "red", "blue", "pink", "purple", "yellow", "orange", "white", "black", 'GOLD']

wallet = 500

unice_sharks_collated = set()

inventory = []

item_shop = [
  {
    'name': "Bow of Luck",
    'description': "This Bow will help you hit every target with a 100 crit change for 3 seconds from equeiped",
    'attack_points': 3,
    'durability': 5,
    'price': 10,
    'type': "weapon_range"
  },
  {
    'name': "Sword of Doom",
    'description': "This is the great and powerfull sword of a glorius gladiator, suffering a tragic fate",
    'attack_points': 50,
    'durability': 500,
    'price': 200,
    'type': "weapon_mele"
  },
  {
    'name': "Health Potion",
    'description': "When you use this you will instantly heal up to full health",
    'attack_points': 0,
    'durability': 1,
    'price': 10,
    'type': "heal_full"
  },
  {
    'name': "Thunder Stone",
    'description': "When you use this item nerby enemies will be struck by lighning and not able to move for 3 seconds",
    'attack_points': 5,
    'durability': 100,
    'price': 25,
    'type': "specialItem_thunder"
  }
]

print("Welcome to the... Hph hph")
print("ITEM SHOP!")
print("With soo many diffrent items, tell me traveler what would you like to buy?")
print()

while(wallet > 1):
  index_counter = 0
  #Prints all the items in the store
  for item in item_shop:
    print("-----------")
    print(f"Index: {index_counter}")
    print(item['name'])
    print(f"Description: {item['description']}")
    print(f"Cost: {item['price']} gold")
    print(f"Attack: {item['attack_points']}")
    print(f"Durability: {item['durability']}")
    print("-----------")
    index_counter = index_counter + 1
  print()
  print("Your Found Sharks")
  print(unice_sharks_collated)
  print(f"You got {wallet} gold left")
  print("Your current inventory")
  for item in range(0, len(inventory)):
      print(inventory[item])
      print()
  print("What would you like to buy? (Please insert the index of the item you would like to buy)")
  user_purchase = input()
  if user_purchase.isnumeric():
    if(item_shop[int(user_purchase)]['price'] <= wallet):

        #Bonus Shark Calculator
        value = randint(0, 100)
        if value % 10 == 0:
            print("You Found a bonus shark")
            print(f"You found a {sharks[int(value/10)]} shark")
            unice_sharks_collated.add(sharks[int(value/10)])

        wallet = wallet - item_shop[int(user_purchase)]['price']
        print(f"You hasve pushased the {item_shop[int(user_purchase)]['name']} for {item_shop[int(user_purchase)]['price']} gold")
        inventory.append(item_shop[int(user_purchase)])
        for item in range(0, len(inventory)):
          print(inventory[item])
          print()
        print("Press enter to continue")
        input()
    else:
       print("You can't afford this item!")
  else:
    print("Only numbers is allowed")

print("You have spent all your money :(")

