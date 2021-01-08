from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
reverse = {'n': 's', 'e': 'w', 's':'n', 'w': 'e'}
visited = {}
queue = {}
prev = [None]

def check_directions(room):
    directions = []
    if 'n' in room_graph[room][1].keys():
        directions.append('n')
    if 'e' in room_graph[room][1].keys():
        directions.append('e')
    if 'w' in room_graph[room][1].keys():
        directions.append('w')
    if 's' in room_graph[room][1].keys():
        directions.append('s')
    return directions

while len(visited) < len(room_graph):
    current_room = player.current_room.id
    
    if current_room not in queue:
        visited[current_room] = current_room
        queue[current_room] = check_directions(current_room)
    
    if len(queue[current_room]) < 1:
        prev_dir = prev.pop()
        traversal_path.append(prev_dir)
        player.travel(prev_dir)
    else:
        next_dir = queue[current_room].pop()
        traversal_path.append(next_dir)
        prev.append(reverse[next_dir])
        player.travel(next_dir)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
