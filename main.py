# Course: CS 30
# Period: 1
# Date created: 21/02/28
# Date last modified: 21/03/01
# Name: Kira Gray
# Description: RPG game with classes

global dest
global ask

class player:
    def __init__(self):
        self.name = ''
        self.won = False
        self.location = 'start'
myPlayer = player()

def print_map():
    print("""╔════════════╦════════════╦═════════════╦════════════╗
             ║   Latter   ║ Cargo Left ║ Cargo Right ║ Hyperdrive ║
             ║ (2nd  lvl) ║  (*start)  ║  (and map)  ║    Room    ║
             ╠════════════╬════════════╬═════════════╬════════════╣
             ║    Crew    ║   Latter   ║ Living Area ║   Latter   ║
             ║  Quarters  ║ (to start) ║             ║ (3rd  lvl) ║
             ╠════════════╬════════════╬═════════════╬════════════╣
             ║  Captains  ║   Latter   ║ Locked Room ║  Cockpit   ║
             ║  Quarters  ║ (2nd  lvl) ║             ║            ║
             ╚════════════╩════════════╩═════════════╩════════════╝
          """)

ZONENAME = ''
DESCRIPTION = 'description'
SEARCH = 'search'
SOLVED = False
UP = 'up', 'north',
DOWN = 'down', 'south',
LEFT = 'left', 'west',
RIGHT = 'right', 'east',

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 }

zonemap = {
    'a1': {
        ZONENAME: 'Latter up',
        DESCRIPTION: 'There is a latter going up.',
        SEARCH: 'The start is to the right.',
        UP: 'b2',
        DOWN: '',
        LEFT: '',
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: 'Cargo left',
        DESCRIPTION: """This is the start. cargo containers are piled high
        """,
        SEARCH: """There is more cargo on the right and a latter going up on the left
        """,
        UP: '',
        DOWN: '',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: 'Cargo right',
        DESCRIPTION: 'More cargo containers',
        SEARCH: """Theres a door to the right and the other side of the cargo hold on the left
        """,
        UP: '',
        DOWN: '',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: 'Hyperdrive room',
        DESCRIPTION: 'locked',
        SEARCH: 'the only way is to the cargo hold on the left',
        UP: '',
        DOWN:'',
        LEFT: 'a3',
        RIGHT: '',
    },
    'b1': {
        ZONENAME: 'Crew Quarters',
        DESCRIPTION: """there is a table and beds. There are two pirates""",
        SEARCH: 'the only way is right to the latter going down',
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: 'Latter down',
        DESCRIPTION: 'Latter that goes down',
        SEARCH: """Crew Quarters are to the left and the living area
        to the right""",
        UP: '',
        DOWN: 'a1',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: 'Living area',
        DESCRIPTION: """typical living arrangements. There are two pirates""",
        SEARCH: """the latter going down on the left and a latter
        going up on the right. You found a key card!""",
        UP: '',
        DOWN: '',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'b4': {
        ZONENAME: 'Latter up',
        DESCRIPTION: 'There is a latter going up.',
        SEARCH: 'The living area is to the left.',
        UP: 'c2',
        DOWN: '',
        LEFT: 'b3',
        RIGHT: '',
    },
    'c1': {
        ZONENAME: 'Captains Quarters',
        DESCRIPTION: 'locked',
        SEARCH: 'There is a latter going down to the right',
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: 'c2',
    },
    'c2': {
        ZONENAME: 'Latter down',
        DESCRIPTION: 'Latter that goes down.',
        SEARCH: """The captains quarters is on the left and a
        locked room on the right.""",
        UP: '',
        DOWN: 'b4',
        LEFT: 'c1',
        RIGHT: 'c3',
    },
    'c3': {
        ZONENAME: 'Locked room',
        DESCRIPTION: """You use the key card! There is nothing in the room, it's just a room leading to the cockpit.""",
        SEARCH: """The latter going down is on the left and the
        cockpit is to the right.""",
        UP: '',
        DOWN: '',
        LEFT: 'c2',
        RIGHT: 'c4',
    },
    'c4': {
        ZONENAME: 'Cockpit',
        DESCRIPTION: """three pirates and the captain,
        everything else is normal""",
        SEARCH: """the only way is to the left back to the locked room""",
        UP: '',
        DOWN: '',
        LEFT: 'c3',
        RIGHT: '',
    },
}

def print_location():
  print('\n' + ('#' * (4 + len(myPlayer.location))))
  print('# ' + myPlayer.location + ' #')
  print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
  print('\n' + ('#' * (4 + len(myPlayer.location))))

def continuous(ans):
  while ans:
      print("""
      Do one of the following actions:
      -> Move
      -> Explore
      -> Attack
      -> Quit
      """)
      print("What would you like to do?")
      ans = input("> ")
      if ans.lower() == "quit":
          break
      if ans.lower() == "left":
        player.move(ans.lower())
        print("You go left.")
      elif ans.lower() == "right".lower():
        player.move(ans.lower())
        print("You go right.")
      elif ans.lower() == "Explore".lower():
        player.explore(ans.lower())
        print("You look around.")
      elif ans.lower() == "attack".lower():
        player.attack(ans.lower())
        print("You attack.")
      else:
        print("Invalid imput!")



def move(myAction):
	ask = "Where would you like to "+myAction+" to?\n> "
	dest = input(ask)
	if dest == 'left':
          destination = zonemap[myPlayer.location][LEFT]
          move_player(destination)
	elif destination == 'right':
          destination = zonemap[myPlayer.location][RIGHT]
          move_player(destination)
	else:
		print("Invalid direction, try using left, or right.\n")
		move(myAction)

def move_player(destination):
	print("\nYou have moved to the " + destination + ".")
	myPlayer.location = destination
	print_location()

def play_examine(ans):
  if zonemap[myPlayer.location] == 'a1' or 'b4':
    ask = "Would you like to go up?\n> "
    dest = input(ask)
    if dest == 'yes':
      destination = zonemap[myPlayer.location][UP]
      move_player(destination)
    else:
      continuous(ans)
  elif zonemap[myPlayer.location] == 'b2' or 'c2':
    ask = "Would you like to go down?\n> "
    dest = input(ask)
    if dest == 'yes':
      destination = zonemap[myPlayer.location][DOWN]
      move_player(destination)
    else:
      continuous(ans)
  else:
    zonemap[myPlayer.location][SEARCH]

def start_game():
  return

def main_game_loop():
  