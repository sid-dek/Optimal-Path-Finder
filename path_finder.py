## Created by Siddharth Dekhane ##
## Language : Python3 ##
## Project : Artificial Intelligence HW-1 ##

import sys, queue, math

#Initialize all data structures
cost = 0
expansion_queue = queue.Queue()
priority_queue = queue.PriorityQueue()
matrix=[]
visited_dict = {}
targets_op = []
targets_dict = {}
method = ""
max_z = 0
matrix_width = 0
matrix_height = 0
root_node = 0   

"""
Class: Node (parent_node, x-coordinate , y-coordiate, cost_till_node, heuristic_val)

Methods :
    #1 Initialisation
    #2 node_to_root : Prints path from root_node to node
"""
class Node:
    def __init__ (self, parent, x, y, cost, heuristic):
        self.parent = parent
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = heuristic

    def node_to_root(self):
        string_new = ""
        while (self.parent != 'null'):
            string_new = str(self.y) + "," + str(self.x) + " " + string_new
            self = self.parent
        string_new = str(root_node.y) + "," + str(root_node.x) + " " + string_new
        return (string_new).strip()

    def eq(self, second):  
        if second == None:
            return False
        if((self.x == second.x) and (self.y == second.y)):
            return True
        return False

    def __lt__(self, second):
        return ( int(self.cost + self.heuristic) < int(second.cost + second.heuristic) )

## Take input and store variables locally for all tree methods
def parse_input():
    global method, matrix, cost, max_z
    global targets_dict, targets_op
    global expansion_queue, visited_dict
    global matrix, matrix_width, matrix_height
    global root_node

    i=1
    ## Parse input to local variables
    file = open("input.txt" , "r")
    for line in file:
        if i==1:
            method = ( line.strip() ).upper()
            i+=1

        elif i==2:
            matrix_width = int(line.split()[0])
            matrix_height = int(line.split()[1])
            i+=1

        elif i==3:
            initial_y = int(line.split()[0])
            initial_x = int(line.split()[1])
            root_node = Node('null', initial_x, initial_y, 0, 0)
            i+=1

        elif i==4:
            max_z = int(line)
            i+=1

        elif i==5:
            no_of_targets = int(line)
            i+=1

        elif (i<=no_of_targets+5):
            target_string = str(str(line.split()[1])+","+str(line.split()[0]))

            if target_string in targets_dict:
                targets_dict[target_string].append(i-6)
            else:
                targets_dict[target_string] = [i-6]
            targets_op.append("FAIL")
            i+=1

        else:
            row = [int(j) for j in line.split()]
            matrix.append(row)

    file.close()


"""
Type: BFS Tree
   
Methods Used:
    #1 Check_if_visited_bfs() : Check if node already in visited
    #2 Direction_search_bfs() : Evaluate all valid neighbors
    #3 Check_direction_bfs() : Check z_elevation condition
    #4 Evaluate BFS Tree
"""
## BFS: Check if already visited, if not add to queues
def check_if_visited_bfs(new_node):
    check_string = str(new_node.x) + "," + str(new_node.y)
    if check_string not in visited_dict:
        expansion_queue.put(new_node)
        visited_dict[check_string] = new_node 

## BFS: Evaluate valid neighbors
def direction_search_bfs(parent, x, y):

    ## North West
    if ((x-1)>=0 and (y-1)>=0):
        check_direction_bfs(parent, x, y, (x-1), (y-1), 1)
            
    ## North East
    if ((x-1)>=0 and (y+1)<=(matrix_width-1)):
        check_direction_bfs(parent, x, y, (x-1), (y+1), 1)

    ## North
    if ((x-1)>=0 and (y)>=0):
        check_direction_bfs(parent, x, y, (x-1), (y), 1)

    ## East
    if ((x)>=0 and (y+1)<=(matrix_width-1)):
        check_direction_bfs(parent, x, y, (x), (y+1), 1)

    ## West
    if ((x)>=0 and (y-1)>=0):
        check_direction_bfs(parent, x, y, (x), (y-1), 1)

    ## South West
    if ((x+1)<=(matrix_height-1) and (y-1)>0):
        check_direction_bfs(parent, x, y, (x+1), (y-1), 1)

    ## South East
    if ((x+1)<=(matrix_height-1) and (y+1)<=(matrix_width-1)):
        check_direction_bfs(parent, x, y, (x+1), (y+1), 1)

    ## South
    if ((x+1)<=(matrix_height-1) and (y)>=0):
        check_direction_bfs(parent, x, y, (x+1), (y), 1)

## BFS: Check direction and max_elevation condition
def check_direction_bfs(parent , old_x, old_y, x , y , cost):
    if ( abs(matrix[x][y] - matrix[old_x][old_y] ) <= max_z ):
        new_node = Node(parent, x, y, (parent.cost + cost), 0)
        check_if_visited_bfs(new_node)

## BFS: Compute BFS Tree
def compute_bfs_tree():

    expansion_queue.put(root_node)
    visited_dict[ str(root_node.x) + "," + str(root_node.y) ] = root_node

    while (True):
        ## Expansion node empty condition
        if (expansion_queue.empty()):
            return

        ## Extract node from top
        working_node = expansion_queue.get()

        ## Check if target in target_array
        check_target(working_node)

        ## Check valid neighbouring node
        direction_search_bfs (working_node, working_node.x , working_node.y)      


"""
Type: UCS Tree
   
Methods Used:
    #1 Direction_search_ucs() : Evaluate all valid neighbors
    #2 Check_direction_ucs() : Check z_elevation condition
    #3 Check_if_visited_ucs() : Check if node already in visited
    #3 Evaluate UCS Tree
"""

## UCS: Evaluate valid neighbors
def direction_search_ucs(parent, x, y):

    ## North West
    if ((x-1)>=0 and (y-1)>=0):
        check_direction_ucs(parent, x, y, (x-1), (y-1), 14)
        
    ## North East
    if ((x-1)>=0 and (y+1)<=(matrix_width-1)):
        check_direction_ucs(parent, x, y, (x-1), (y+1), 14)

    ## North
    if ((x-1)>=0 and (y)>=0):
        check_direction_ucs(parent, x, y, (x-1), (y), 10)

    ## East
    if ((x)>=0 and (y+1)<=(matrix_width-1)):
        check_direction_ucs(parent, x, y, (x), (y+1), 10)

    ## West
    if ((x)>=0 and (y-1)>=0):
        check_direction_ucs(parent, x, y, (x), (y-1), 10)

    ## South West
    if ((x+1)<=(matrix_height-1) and (y-1)>0):
        check_direction_ucs(parent, x, y, (x+1), (y-1), 14)

    ## South East
    if ((x+1)<=(matrix_height-1) and (y+1)<=(matrix_width-1)):
        check_direction_ucs(parent, x, y, (x+1), (y+1), 14)

    ## South
    if ((x+1)<=(matrix_height-1) and (y)>=0):
        check_direction_ucs(parent, x, y, (x+1), (y), 10)

## UCS: Check directions
def check_direction_ucs(parent , old_x, old_y, x , y , cost):
    if ( abs(matrix[x][y] - matrix[old_x][old_y] ) <= max_z ):
        new_node = Node(parent, x, y, (cost + parent.cost), 0)
        check_if_visited_ucs(new_node)

## UCS: Check if visited
def check_if_visited_ucs(new_node):
    check_string = str(new_node.x) + "," + str(new_node.y)
    if check_string not in visited_dict:
        priority_queue.put(new_node)
        visited_dict[check_string] = new_node

## UCS: Compute UCS Tree
def compute_ucs_tree():

    priority_queue.put(root_node)
    visited_dict[ str(root_node.x) + "," + str(root_node.y) ] = root_node

    while (True):

        ## Expansion node empty condition
        if (priority_queue.empty()):
            return

        ## Extract node from top
        working_node = priority_queue.get()

        ## Check if target in target_array
        check_target(working_node)

        ## Check valid neighbouring node
        direction_search_ucs (working_node, working_node.x , working_node.y)  


"""
Type: A* Tree
   
Methods Used:
    #1 --None--
    #2 Compute_Heuristic()
    #3 Check_Target() : Evaluate A* for all targets
    #4 Direction_search_astar() : Evaluate all valid neighbors
    #5 Check_direction_astar() : Check z_elevation condition
    #6 Check_if_visited_astar()
    #6 Evaluate A* Tree
"""

## Calculate Heuristic for A*
def compute_heuristic(x1, y1, x2, y2):
    return ( int( ( ( (int(x2)-int(x1))**2 ) + ( (int(y2)-int(y1))**2 ) )** 0.5 ) )

## Astar: For all target, append op[] accordingly
def check_target_astar(x, y, node):
    current_target = str(x) + "," + str(y)
    target_search = str(node.x) + "," + str(node.y)
    if (current_target == target_search):
        path = node.node_to_root()
        for repetitions in range (len(targets_dict[target_search])):
            targets_op [ targets_dict[target_search][repetitions] ] = path
        return True
    return False

## Astar: Evaluate valid neighbors
def direction_search_astar(parent, x, y, target_x, target_y):

    ## North West
    if ((x-1)>=0 and (y-1)>=0):
        check_direction_astar(parent, x, y, (x-1), (y-1), 14, target_x, target_y) 

    ## North East
    if ((x-1)>=0 and (y+1)<=(matrix_width-1)):
        check_direction_astar(parent, x, y, (x-1), (y+1), 14, target_x, target_y)

    ## North
    if ((x-1)>=0 and (y)>=0):
        check_direction_astar(parent, x, y, (x-1), (y), 10, target_x, target_y)

    ## East
    if ((x)>=0 and (y+1)<=(matrix_width-1)):
        check_direction_astar(parent, x, y, (x), (y+1), 10, target_x, target_y)

    ## West
    if ((x)>=0 and (y-1)>=0):
        check_direction_astar(parent, x, y, (x), (y-1), 10, target_x, target_y)

    ## South West
    if ((x+1)<=(matrix_height-1) and (y-1)>0):
        check_direction_astar(parent, x, y, (x+1), (y-1), 14, target_x, target_y)
    
    ## South East
    if ((x+1)<=(matrix_height-1) and (y+1)<=(matrix_width-1)):
        check_direction_astar(parent, x, y, (x+1), (y+1), 14, target_x, target_y) 
    
    ## South
    if ((x+1)<=(matrix_height-1) and (y)>=0):
        check_direction_astar(parent, x, y, (x+1), (y), 10, target_x, target_y)

## Astar: Check directions
def check_direction_astar(parent , old_x, old_y, x , y , cost, target_x, target_y):
    delta_elevation = abs( matrix[x][y]-matrix[old_x][old_y] )
    if (delta_elevation <= max_z):
        new_node = Node(parent, x, y, (cost + parent.cost + delta_elevation) , compute_heuristic(x, y, target_x, target_y) )
        check_if_visited_astar(new_node)

## A*: Check if already visited, if not add to queues
def check_if_visited_astar(new_node):
    check_string = str(new_node.x) + "," + str(new_node.y)
    if check_string in visited_dict:
        if (new_node.cost < (visited_dict[check_string]).cost) :
            (visited_dict[check_string]).cost = new_node.cost
            (visited_dict[check_string]).parent = new_node.parent
    else:
        priority_queue.put(new_node)
        visited_dict[check_string] = new_node 

## Compute A* Tree
def compute_astar_tree(current_target):

    ## Initialize current target coordinates
    current_target_x = current_target.split(',')[0]
    current_target_y = current_target.split(',')[1]

    ## Reset related components
    priority_queue.queue.clear()
    visited_dict.clear()
    root_node.heuristic = compute_heuristic(root_node.x, root_node.y, current_target_x, current_target_y)
    priority_queue.put(root_node)
    visited_dict[ str(root_node.x) + "," + str(root_node.y) ] = root_node

    while (True):

        ## Expansion node empty condition
        if (priority_queue.empty()):
            return

        ## Extract node from top
        working_node = priority_queue.get()

        ### For the current target, append op[] accordingly
        if_target_found = check_target_astar(current_target_x, current_target_y, working_node)
        if(if_target_found):
            return

        ## Check valid neighbouring node
        direction_search_astar (working_node, working_node.x, working_node.y, current_target_x, current_target_y)  


"""
Common: Identify method and compute tree accordingly
"""

## BFS & UCS: Check if node is a target, if yes push to op[]
def check_target(node):
    target_search = str(node.x) + "," + str(node.y)
    if(target_search in targets_dict):
        path = node.node_to_root()
        for repetitions in range( len(targets_dict[target_search]) ):
            targets_op[ targets_dict[target_search][repetitions] ] = path

## Evaluate method and call respective tree functions
def evaluate_tree():
    if (method == 'BFS'):
        compute_bfs_tree()
    if (method == 'UCS'):
        compute_ucs_tree()
    if (method == 'A*'):
        for selected_target in targets_dict:
            compute_astar_tree(selected_target)

## This prints final output file
def end_code(print_list):
    file = open('output.txt', 'w+')
    file.write(print_list[0])
    for line in print_list[1:]: 
        file.write("\n"+line)
    file.close()
    sys.exit()


"""
Perform The Algorithm / Execute the code !
"""

## Parse input
parse_input()

## Evaluate Tree according to the provided input
evaluate_tree()

## Print to output file
end_code(targets_op)