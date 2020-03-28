letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
###
letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
#print(letter_to_points)
###
player_to_words = {"player1": ["blue", "tennis", "exit"], "wordNerd": ["earth", "eyes", "machine"], "Lexi Con": ["eraser", "belly", "husky"], "Prof Reader": ["zap", "coma", "period"]}
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

  print(player_to_points)
###  
def play_word(player, word):
  if player in player_to_words.keys():
    player_to_words[player].append(word)
  else:
    player_to_words[player] = word

### call functions ###
update_points()  
play_word("player2", ["green", "yellow", "banana"])
update_points()
play_word("player1", "woman")
play_word("wordNerd", "black")
play_word("Lexi Con", "student")
play_word("Prof Reader", "profesor")
play_word("player2", 'robot')
update_points()


    
    
    
    
    
    
    
    
                  