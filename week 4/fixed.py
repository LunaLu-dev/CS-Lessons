# 1

class Cat:
  info = "Meow meow meow"

  def meow(self):
    print("The cat says... ", self.info)


my_weird_cat = Cat()
my_weird_cat.meow()

#2

class Blahaj:
    
  def hug():
    print("Blahaj is crawling up to you to give you a big hug")

  def spin():
    print("Blahaj is spinning, looks like Blahaj having fun")

  def comfort():
    print("Blahaj is here to tell you that everything is going to be ok")

print("Do you need a hug? y/n")
if(input() == 'y'):
  Blahaj.hug()
  Blahaj.comfort()
print("Blahaj is asking you if you wanna see a trick? y/n")
if(input() == 'y'):
  Blahaj.spin()

#3

class Player:
  health = 20
  hit_point = 3

  def attack(self, Enemy):
    Enemy.health = Enemy.health - self.hit_point
    print("Enemy has been hurt, Enemy has ", Enemy.health, " hp left")
    

class Enemy:
  health = 10
  hit_point = 1

  def attack(self, Player):
    Player.health = Player.health - self.hit_point
    print("The enemy attacked you, you have ", Player.health, " hp left, dont give up")

#4
    
while True:
  
  thePlayer = Player()
  theEnemy = Enemy()

  print("an enemy apers, what do you want to do (attack/flee)")
  if(input() == "attack"):
    # python does not seem to understand what 'self' mean and expext it to be specified
    thePlayer.attack(theEnemy)
  else:
    theEnemy.attack(thePlayer)
  if(theEnemy.health <= 0):
    print("Congratulkations you the enemy has been defeated")
    print()
    print("Do you wanna play again? (y/n)")
    if(input() == 'y'):
      theEnemy.health = 10
      thePlayer.health = 20
    else:
      print("Thanks for playing :)")
      break
  elif(thePlayer.health <= 0):
    print("Game Over, You lost")
    print("Do you want to play again? (y/n)")
    if(input() == 'y'):
      theEnemy.health = 10
      thePlayer.health = 20
    else:
      print("Thanks for playing :)")
      break