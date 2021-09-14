import random

#Simple chat program
#Responds randomly with one of four preprogrammed responses

def generate_response(user_input):
  responses_1 = [
    "Doing quite well!",
    "Good, thank you for asking!",
    "I've been better.",
  ]
  return random.choice(responses_1)

def generate_response(user_input):
  responses_2 = [
    "Tacos!",
    "I love pizza!",
    "I like all food, no preference.",
  ]
  return random.choice(responses_2)

def init_chat():
  quit_character = 'q'

  user_input_1 = input("Hello, how are you?\n")
#   user_input_2 = input("What is your favorite food?\n")

  while user_input_1 != quit_character:
    #Ask the user for more input, then use that in your response
    user_input_1 = input(generate_response(user_input_1) + "\n")
#   while user_input_2 != quit_character:
#     #Ask the user for more input, then use that in your response
#     user_input_2 = input(generate_response(user_input_2) + "\n")

def init_chat():
  quit_character = 'x'

  user_input_2 = input("What is your favorite food?\n")

  while user_input_2 != quit_character:
    #Ask the user for more input, then use that in your response
    user_input_2 = input(generate_response(user_input_2) + "\n")

if __name__ == "__main__":
  init_chat()

# I am not sure why the chatbot is only asking the favorite food question, and not the how are you question too. I have been trying my best to debug it, but have not been able to do so. 
