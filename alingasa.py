player_x = 0
player_y = 0
treasure_x = 5
treasure_y = 3
game_running = True
print(f"Find the treasure at ({treasure_x}, {treasure_y})!")
while game_running:
  move = input("Enter move (up/down/left/right): ")
  if move == "w":
    player_y += 1
  if move == "s":
    player_y -= 1
  if move == "d":
    player_x += 1
  if move == "a":
    player_x -= 1
  else:
    print("invalid move!)  
  print(f"Player position: ({player_x}, {player_y})")
  if player_x == treasure_x and player_y == treasure_y:
    print("You Found the treasure!")
    game_running = False
