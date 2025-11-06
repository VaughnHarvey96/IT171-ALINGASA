player_x = 0
player_y = 0
treasure_x = 5
treasure_y = 3
game_running = True
print(f"Find the treasure at ({treasure_x}, {treasure_y})!")
while game_running:
move = input("Enter move (up/down/left/right): ")
# TODO: update player_x and player_y based on move
print(f"Player position: ({player_x}, {player_y})")
# TODO: check if player has reached the treasure
