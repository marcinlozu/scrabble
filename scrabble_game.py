letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
###
letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
#print(letter_to_points)
###
player_to_words = {}
player_to_points = {}
### functions ###
def score_word(word):
  point_total = 0
  for a in word.upper():
    point_total += letter_to_points.get(a, 0)
    
  return point_total
###
def update_points():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
      player_to_points[player] = player_points
      #print(player_points)

  #print(player_to_points)
  for key, value in player_to_points.items():
    print(f"{key} have {value} points.")
###  
def play_word(player, word):
  if player in player_to_words.keys():
    player_to_words[player].append(word)
  else:
    player_to_words[player] = word
###
def player_name():
  print("Hello, what's your name?")
  player = input()
  player_to_words[player] = []

def another_player():
  print("Add another player? (y/n)")
  ans = input()
  if ans.lower() in ['y', 'yes']:
    player_name()
    another_player()
  else:
    print("Today players: ")
    for players in player_to_words:
      print("- ",players)

def player_add_word():
  for player in player_to_words:
    print(f"{player} add a word:")
    word = input()
    play_word(player, word)
    #player_to_words[player].append(word)

### call functions ###
player_name()
another_player()
print("--------")
player_add_word()
player_add_word()
print("--------")
update_points()

    
    
    
    
    
    
    
    
                  