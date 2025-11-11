player_dudut = 0
player_harvey = 0

treasure_x = 1
treasure_y = 3
game_running = True

print("github version")
print("Welcome to Alingasa’s Maze")

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
  move = print(input("w to move up, s to move down, a to move left, d to move right")).lower()
  
  if move == "w":
    player_harvey += 1
  if move == "s":
    player_harvey -= 1
  if move == "a":
    player_dudut -= 1
  if move == "d":
     player_dudut += 1
  if move == "q":
    print("Maybe next time=(")
    break
  else:
    print("invalid move!") 

  print(f"Player position: ({player_dudut}, {player_harvey})")
          
  if player_x == treasure_x and player_y == treasure_y:
    print("You Found the treasure!")
    game_running = False
