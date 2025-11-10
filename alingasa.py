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
=======
print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
  move = input("Enter move (up/down/left/right or q): ").lower()
  
  if move == "up":
    player_harvey += 1
  if move == "down":
    player_harvey -= 1
  if move == "left":
    player_dudut -= 1
  if move == "right":
>>>>>>> f80a8686ff96c35262aec400727fa349fde96a61
    player_dudut += 1
  if move == "q":
    print("Maybe next time=(")
    break
  else:
<<<<<<< HEAD
    print("invalid move!") 
=======
    print("invalid move!") 
>>>>>>> f80a8686ff96c35262aec400727fa349fde96a61
    
  print(f"Player position: ({player_dudut}, {player_harvey})")
          
  if player_x == treasure_x and player_y == treasure_y:
    print("You Found the treasure!")
    game_running = False
