import random

#weapon check

arms = ["lazer_gun","deth_ray","null_ray"]

#Weapon power

arms_attack = {"lazer_gun":random.randint(20,40),"deth_ray":random.randint(30,55),
               "null_ray":random.randint(60,90)}
                              
             




print("Enter a number to act \n\n")

#User input for weapon choice  

user_input = abs(int(input())) % 3


x = 75

chance = (random.randint(0,100) + 1)


#Pass hit ratio and random damage run damage function if hit

#Weapon choic function

def choose_weapon(user_input):

  print("You selected the "+ str(arms[user_input]) + " you deal " + str(arms_attack[arms[user_input]]) + " to the target!\n")
  
#Hit or miss function  

def draw(x,user_input):

 

 if chance < x:
   print("\n\nBut, it missed...")
   
 else:
     
   choose_weapon(user_input)
       
   
draw(x,user_input)


