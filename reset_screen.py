def reset_screen():
  clear_screen()
  move_to_home()

def clear_screen():
  print(chr(27) + "[2J")

# play with this and make it return the cursor to the top left
def move_to_home():
  print("\033[6;3BBegin the new game.")