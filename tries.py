def lives(word):
  lst = []
  for letter in word:
    lst.append(letter)
  print(lst)
  for letter in lst:
    guess = input("Guess a letter: ")
    if guess == lst:
      print("nice")
    elif guess != lst:
      print("wrong letter")
  print("you ran out lives")
  
def game(word):
  blank_lst = []
  for a in word:
    blank_lst.append("_")
  print(blank_lst)


