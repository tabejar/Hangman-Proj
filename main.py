import random
from tries import game , lives

list_of_words = [
  "fortnite", "goku", "jonesy", "fishsticks", "heisenberg", "saul",
  "meowscles", "midas", "vegeta", "beerus", "bulma"]
word = random.choice(list_of_words)

print("Welcome to hangman where you have to guess the word") 
print("but if u get it wrong 6 times u die good luck.")
print("Each dashed line represents a character in the word.") 
print(word)
game(word)
lives(word)


