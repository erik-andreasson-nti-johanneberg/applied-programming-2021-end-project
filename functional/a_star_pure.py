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

def astar(start,end): #pathfinding system
    open_list = []
    closed_list = []
    path = []

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list.append(start_node)
    previous_nodes_list = []

    # Get the current node
    while True:
        current_node = open_list[0]
        current_index = 0
        # print(open_list)
        for index, item in enumerate(open_list):
            # print("F_values")
            # print("value for checked item is : {}".format(item.f))
            # print("value for current node is : {}".format(current_node.f))
            # print('')
            # print("item cords and f value")
            # print(item.position)
            # print(item.f)
            # print("")
            if item.f < current_node.f:
                current_node = item
                current_index = index
        # print("")
        # print("")
        # print("f value of current node")
        # print(current_node.f)
        # print("current node cords")
        # print(current_node.position)
        # print("")
        
         # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        previous_nodes_list.append(current_node)

        # Found the goal
        # if current_node == end_node:
        #     pass

        current = current_node
        if current is not None:
            path.append(current.position)

        # print(current.position)

        if current_node == end_node:
            return path

        children = []
        print("")
        print("new current node:")
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(map) - 1) or node_position[0] < 0 or node_position[1] > (len(map[len(map)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            # print('')
            # print(map[node_position[0]][node_position[1]])
            if map[node_position[0]][node_position[1]] != 0:
                # print('passed')
                # print('node_position after checking walkable:')
                # print(node_position)
                # print('')
                continue

            # Create new node
            # print(node_position)
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

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
            print("")
            print("new child")
            # print(previous_nodes_list)
            for previous_node in previous_nodes_list:
                if previous_node == child:
                    prev_node_same_child = True
                    break
            if prev_node_same_child:
                continue

            print("child position")
            print(child.position)

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

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