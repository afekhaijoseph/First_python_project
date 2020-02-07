import random
from stories import *
def personal_story():
   return [input("Add a female name : "), input(" Input a phone brand : "), input("Input a country : "), input("Input a bank name: ")]
def official_story():
    return [input("input an occupation : "), input("What is your favourite snack : ")]
def food_story():
    return[input("What is  your name : "), input("How old are : ")]

def command():
    random_questions=["personal_story", "official_story", "food_story"]
    random_question=random.choice(random_questions)
    if random_question == "personal_story":
       first_story = personal_story()
       print(first_story[0] + story_1 + first_story[1] + story_2 + first_story[2] + story_3 + first_story[3] + story_4 + first_story[0] + story_5
       + first_story[0] + story_6 + first_story[0] + story_7 + first_story[0] + story_8 + first_story[0] + story_9 + first_story[0] + story_10 + first_story[0] + story_11
       + first_story[0] + story_12 + first_story[0] + story_13 + first_story[0] + story_14 + first_story[0] + story_15 + first_story[0] + story_16)
   
    elif random_question=="official_story":
      occupation_snack = official_story()
      print(snack_1 + occupation_snack[0] + snack_2 + occupation_snack[1] + snack_3 + occupation_snack[1] + snack_4 + occupation_snack[1] + snack_5)
    else:
      name_age = food_story()
      print(name_1 + name_age[0] + name_2 + name_age[1] + name_3 + name_age[0] + name_3 + name_age[0] + name_4 + name_age[0]
      + name_5 + name_age[0] + name_6 + name_age[0] + name_7 + name_age[0] + name_8 + name_age[0] + name_9 + name_age[0] + name_10 + name_age[0]
      + name_11 + name_age[0] + name_12 + name_age[0] + name_13 + name_age[0] + name_14 + name_age[0] + name_15 + name_age[0] + name_16 + name_age[0]
      + name_17 + name_age[0] + name_18 + name_age[0] + name_19 + name_age[0] + name_20 + name_age[0] + name_21 + name_age[0] + name_22 + name_age[0])
command()
ask = input("Do you want to play again [Y/n] : ")
if ask == "y":
    command() 
else:
    print("End of story.")