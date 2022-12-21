def lives(word):
  blank_lst = []
  for a in word:
    blank_lst.append("_")
  print(blank_lst)
  lst = []
  for letter in word:
    lst.append(letter)
  hp = 6
  while hp > 0:
    guess = input("Guess a letter: ").lower()
    if guess in lst:
      print("nice")
      place = lst.index(guess)
      blank_lst.insert(place,guess)
      blank_lst.remove("_")
      print(blank_lst)
    if guess not in lst:
      hp = hp - 1
      print("wrong guess")
    if hp == 0:
      print("you ran out of lives")
