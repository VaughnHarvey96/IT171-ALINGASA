player_dudut = 0
player_harvey = 0

treasure_x = 5
treasure_y = 3
game_running = True

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
  move = input("Enter move (up/down/left/right): ")
  
  if move == "up":
    player_harvey += 1
  if move == "down":
    player_harvey -= 1
  if move == "left":
    player_dudut -= 1
  if move == "right":
    player_dudut += 1
  if move == "quit":
    print("Maybe next time=(")
    break
  else:
    print("invalid move!) 
    
  print(f"Player position: ({player_dudut}, {player_harvey})")
          
  if player_x == treasure_x and player_y == treasure_y:
    print("You Found the treasure!")
    game_running = False
