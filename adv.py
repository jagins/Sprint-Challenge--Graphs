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
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
#keep track of the rooms that we encounter
room_map = {}
for room in world.rooms:
    room_map[room] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
visted = set()
#need a stack to put the path and next path on
stack = []
# room_path = [player.current_room.id]
stack.append([player.current_room.id])
my_travseal = []

while len(stack) > 0:
    path = stack.pop()
    print(path)
    current_room = path[-1]
    if current_room not in visted:
        visted.add(current_room)
        exits = player.current_room.get_exits()
        # for room in room_map[current_room]:
        #     # if room in exits and room_map[current_room][room] == '?':
        #     #     my_travseal.append(room)
        #     print(room)
    
    for next_room in room_graph[current_room][1].items():
        direction = next_room[0]
        room = next_room[1]
        #check if the next room is not visited yet
        if room not in visted:
            # make a copy of the room_path
            new_room_path = list(path)
            #append the next room to the copy of the room_path
            new_room_path.append(room)
            #append the copy path to the stack
            stack.append(new_room_path)
            traversal_path.append(direction)
            player.travel(traversal_path[-1])
print(visted)
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
