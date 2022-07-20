from art import logo, vs
from random import randint
from game_data import data
import os

def compare_answers(a_followers, b_followers, score):
  if answer == "a":
    if a_followers > b_followers:
      print(f"You're right! Current score: {score + 1}.")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      return 0
  elif answer == "b":
    if b_followers > a_followers:
      print(f"You're right! Current score: {score + 1}.")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      return 0
  else:
    print(f"That wasn't a valid choice. Your final score was {score}. Start over.")
    return 0

should_continue = True
score = 0

print(logo)

while should_continue:
  a = data[randint(1,len(data))]
  a_name = a["name"]
  a_description = a["description"]
  a_country = a["country"]
  a_followers = int(a["follower_count"])
  print(f"Compare A: {a_name}, a {a_description}, from {a_country}.")

  print(vs)

  b = data[randint(1,len(data))]
  b_name = b["name"]
  b_description = b["description"]
  b_country = b["country"]
  b_followers = int(b["follower_count"])
  print(f"Against B: {b_name}, a {b_description}, from {b_country}.")
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()

  os.system("cls-")
  print(logo)

  comparison = compare_answers(a_followers, b_followers, score)
  if comparison == 0:
    should_continue = False
  else:
    score += 1