class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def find_opening(start, wall_direction,map):
    # print(wall_direction)
    if wall_direction[1] == 1:
        wall_direction = 1
        position_1 = (1, 0)
        position_2 = (-1, 0)
    elif wall_direction[1] == -1:
        wall_direction = 1
        position_1 = (1, 0)
        position_2 = (-1, 0)
    elif wall_direction[0] == -1:
        wall_direction = 1
        position_1 = (0,1)
        position_2 = (0,-1)
    elif wall_direction[0] == 1:
        wall_direction = 1
        position_1 = (0,1)
        position_2 = (0,-1)
    else:
        print('Something went wrong in find_opening func, wall_direction input incorrect or missing')
        return None
    # if wall_direction[0] == 1:
    #     position_1 = [(-1,1)]
    #     position_2 = [(-1,-1)]
    path_1 = []
    path_2 = []
    # start_node = Node(None, start)
    # start_node.g = start_node.h = start_node.f = 0

    path_1.append(start)
    path_2.append(start)
    # print(path_1)
    # print(path_2)
    
    found_hole = False
    out_of_range_1 = False
    out_of_range_2 = False


    while True:
        if found_hole:
            break
        while True:
            current_node_1 = path_1[-1]
            node_position = (current_node_1.position[0] + position_1[0], current_node_1.position[1] + wall_direction)

            # Make sure within range
            if node_position[0] > (len(map) - 1) or node_position[0] < 0 or node_position[1] > (len(map[len(map)-1]) -1) or node_position[1] < 0:
                out_of_range_1 = True
                found_hole = True
                break

            # Make sure walkable terrain
            if map[node_position[0]][node_position[1]] != 0:
                node_position = (node_position[0], node_position[1] - wall_direction)
                wall_node = Node(None, node_position)
                path_1.append(wall_node)
            else:
                hole_node = Node(None, node_position)
                path_1.append(hole_node)
                found_hole = True
                break
        while True:
            # print('2')
            current_node_2 = path_2[-1]
            node_position = (current_node_2.position[0] + position_2[0], current_node_2.position[1] + wall_direction)

            # Make sure within range
            if node_position[0] > (len(map) - 1) or node_position[0] < 0 or node_position[1] > (len(map[len(map)-1]) -1) or node_position[1] < 0:
                out_of_range_2 = True
                found_hole = True
                break

            # Make sure walkable terrain
            if map[node_position[0]][node_position[1]] != 0:
                node_position = (node_position[0], node_position[1] - wall_direction)
                wall_node = Node(None, node_position)
                path_2.append(wall_node)
            else:
                hole_node = Node(None, node_position)
                path_2.append(hole_node)
                found_hole = True
                break
    # print('path1:')
    # print(path_1)
    # print('path2')
    # print(path_2)
    if out_of_range_1:
        return path_2
    if out_of_range_2:
        return path_1
    if len(path_1) > len(path_2):
        return path_2
    else:
        return path_1



        

def astar(start,end,map): #pathfinding system
    open_list = []
    closed_list = []
    path = []

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list.append(start_node)
    previous_nodes_list = []
    found_wall = False

    # Get the current node
    while True:
        if found_wall:
            # print('closed list prior')
            # print(closed_list)
            for node in path_to_opening:
                path.append(node.position)
                closed_list.append(node)
                previous_nodes_list.append(node)
            current_node = closed_list[-1]
            found_wall = False
            # print('closed list prev')
            # print(closed_list)
        else:
            current_node = open_list[0]
            current_index = 0
            # print(open_list)
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index
            
            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)
            previous_nodes_list.append(current_node)
            current = current_node
            if current is not None:
                path.append(current.position)

        # print(current.position)

        if current_node == end_node:
            return path

        # Found the goal
        # if current_node == end_node:
        #     pass


        children = []
        # print("")
        # print("new current node:")
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares
            if found_wall:
                break

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(map) - 1) or node_position[0] < 0 or node_position[1] > (len(map[len(map)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if map[node_position[0]][node_position[1]] != 0:
                wall_direction = (new_position)
                found_wall = True
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)
        if found_wall:
            start = current_node
            print('')
            print("start for find wall func")
            print(start.position)
            print('wall_direction:')
            print(wall_direction)
            path_to_opening = find_opening(start, wall_direction,map)
            print(path_to_opening)
            continue

        # Loop through children
        for child in children:
            child_on_closed_list = False
            prev_node_same_child = False
            child_on_open_list = False
            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    child_on_closed_list = True
                    break
            if child_on_closed_list:
                continue
            # print("")
            # print("new child")
            # print(previous_nodes_list)
            for previous_node in previous_nodes_list:
                if previous_node == child:
                    prev_node_same_child = True
                    break
            if prev_node_same_child:
                continue

            # print("child position")
            # print(child.position)

            # Create the f, g, and h values
            child.g = current_node.g + 1
            # print("current system")
            # print(child.position[0], child.position[1])
            # print((child.position[0] - end_node.position[0]) ** 2)
            # print((child.position[1] - end_node.position[1]) ** 2)
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h
            # print("")

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    child_on_open_list = True
                    break
            
            if child_on_open_list:
                continue

            # Add the child to the open list
            # print("child position")
            # print(child.position)
            # print("")
            open_list.append(child)
        # print("")
        # print("")