import time

def hanoi_bfs(initial_state, goal_state):
    """
    Solve the Tower of Hanoi puzzle using breadth-first search.
    """
    open_list, closed_list = [], []
    open_list.append((initial_state, [initial_state]))

    while open_list:
        current, path = open_list.pop(0)

        closed_list.append(current)

        if (current.get_state() == goal_state.get_state()):
            reconst_path = []
            for state in path:
                reconst_path.append(state.get_state())
            return reconst_path
        else:
            for state in current.get_neighbours():
                present_in_closed_list = False
                for closed_state in closed_list:
                    if closed_state.get_state() == state.get_state():
                        present_in_closed_list = True
                        break

                present_in_open_list = False
                for open_state, _ in open_list:
                    if open_state.get_state() == state.get_state():
                        present_in_open_list = True
                        break

                if not present_in_open_list and not present_in_closed_list:
                    open_list.append((state, path + [state]))

    print('Path does not exist!')
    return None

def PDB_bfs(initial_state):
    """
    Creates a PDB for the Tower of Hanoi problem. Using BFS reversed.
    """
    open_list, closed_map = [], {}
    open_list.append((initial_state, 0))

    start_time = time.time()

    while open_list:
        current, path = open_list.pop(0)
        
        closed_map[current] = path

        for state in current.get_neighbours():
            present_in_closed_map = False
            for closed_state in closed_map:
                if closed_state.get_state() == state.get_state():
                    present_in_closed_map = True
                    break


            present_in_open_list = False
            for open_state, _ in open_list:
                if open_state.get_state() == state.get_state():
                    present_in_open_list = True
                    break

            if not present_in_open_list and not present_in_closed_map:
                open_list.append((state, path + 1))

    print("Finished creating PDB, time taken: " + str(time.time() - start_time))

    return closed_map
