import random
from stories import *
def personal_story():
   return [input("what is your name : "), input(" old are you : ")]
def official_story():
    return [input("what is your occupation : "), input("What is your position at your place of work : ")]
def food_story():
    return[input("What is  your favourite food : "), input("what is your favourite restaurant : ")]

random_questions=["personal_story", "official_story", "food_story"]
random_question=random.choice(random_questions)

if random_question == "personal_story":
    name_age = personal_story()
    print(name_1 + name_age[0]+ name_2 + name_age[1] + name_3 + name_age[0] + name_4 + name_age[0] + name_5 + name_age[0] +
    name_6 + name_age[0] + name_7 + name_age[0] + name_7 + name_age[0] + name_8 + name_age[0] +
    name_9 + name_age[0] + name_10 + name_age[0] + name_11 + name_age[0] + name_12 + name_age[0] + name_13 + name_age[0] +
    name_14 + name_age[0] + name_15 + name_age[0] + name_16 + name_age[0] + name_17 + name_age[0] +
    name_18 + name_age[0] + name_19 + name_age[0] + name_20 + name_age[0] + name_21 + name_age[0] + name_22 + name_age[0]
    )
   
elif random_question=="official_story":
    occupation_position = official_story()
    print(job_1 + occupation_position[0] + job_2 + occupation_position[0] + job_3 + occupation_position[1]
     + job_4 + occupation_position[0] + job_5 + occupation_position[0] + job_6 + occupation_position[0] + job_7 + occupation_position[0]
     + job_8 + occupation_position[0] + job_9 + occupation_position[1] + job_10 + occupation_position[0] + job_11 + occupation_position[0]
     + job_12 + occupation_position[1] + job_13 + occupation_position[0] + job_14 + occupation_position[0] + job_15 + occupation_position[0]
     + job_16 + occupation_position[0] + job_17 + occupation_position[1]  + job_18 + occupation_position[0] + job_19 + occupation_position[1])
else:
    food_restaurant = food_story()
    print(food_1 + food_restaurant[0] + food_2 + food_restaurant[0] + food_3 + food_restaurant[1] + food_4 + food_restaurant[0] + food_5 + food_restaurant[0]
    + food_6 + food_restaurant[1] + food_7 + food_restaurant[0] + food_8 + food_restaurant[0] + food_9 + food_restaurant[1] + food_10 + food_restaurant[0] + food_11 + food_restaurant[0]
    + food_12 + food_restaurant[0] + food_13 + food_restaurant[1] + food_14 + food_restaurant[0] + food_15 + food_restaurant[0] + food_16 + food_restaurant[0] + food_17 + food_restaurant[0]
    + food_18 + food_restaurant[0])
