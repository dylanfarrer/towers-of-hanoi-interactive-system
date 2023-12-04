import time

from .state import State
from .bfs import PDB_bfs

"""
a_star.py

This file contains all A* related methods in the module.

hanoi_heuristic() contains all heuristic logic.

hanoi_a_star() solves the Tower of Hanoi puzzle using A* search and
utilises hanoi_heuristic to do so.
"""

def hanoi_heuristic(state, num_discs, heuristic_type, PDB):
    """
    Calculates the heuristic value for the given state in the Tower of Hanoi problem.
    """
    # number of misplaced disks
    if heuristic_type == 0:
        """
        misplaced_disks_not_on_goal_state = num_discs - len((state.get_state())[3])
        if len((state.get_state())[3]) > 1 and (state.get_state())[3][0] != num_discs:
           return misplaced_disks_not_on_goal_state + len((state.get_state())[3])
        return misplaced_disks_not_on_goal_state
        """

        correct_discs = 0
        for disc in range(len(state.get_state()[3])):
            if state.get_state()[3][disc] == num_discs - disc:
                correct_discs += 1
        return num_discs - correct_discs


    # double the size of the largest pile of disks that is not a partial or complete goal state then minus one
    if heuristic_type == 1:
        max_length = 0
        state_list = state.get_state()
        for tower in range(len(state_list) - 1):
            if len(state_list[tower]) > max_length:
                max_length = len(state_list[tower])
        
        if len((state.get_state())[3]) > max_length and \
           (state.get_state())[3][0] != num_discs:
            max_length = len((state.get_state())[3])
           
        return (max_length * 2) - 1
    
    # max width of misplaced disk + number of disks on top of it
    if heuristic_type == 2:
        state_list = state.get_state()
        max_width = 0
        for tower in range(len(state_list) - 1):
            for disk in range(len(state_list[tower])):
                if state_list[tower][disk] > max_width:
                    max_width = state_list[tower][disk] + len(state_list[tower][disk + 1:])
        return max_width

    if heuristic_type == 3:
        if num_discs > 7:
            # copy current state to new list
            # loop thorugh it, remove all larger values then 7
            # then compare
            trimmed_state = [[disc for disc in tower if disc <= 7] for tower in state.get_state()]
            return PDB[State(trimmed_state)]

        return PDB[state]

def hanoi_a_star(initial_state, goal_state, num_discs, heuristic_type, PDB=None):
    """
    Performs A* search on the Tower of Hanoi problem, using the given heuristic.
    """
    open_list = {initial_state}
    closed_list = set()

    path_length = {}
    path_length[initial_state] = 0

    parents = {}
    parents[initial_state] = initial_state

    if heuristic_type == 3 and PDB is None:
        print("Creating PDB (can take up to 2 minutes)...")
        if num_discs < 8:
            PDB = PDB_bfs(goal_state)
        else:
            towers = [[] for _ in range(4)]
            towers[0] = list(range(7, 0, -1))
            PDB = PDB_bfs(State([row for row in towers[::-1]]))

    print("Calculating...")
    startTime = time.time()
    
    while len(open_list) > 0:
        n = None

        for state in open_list:
            if n == None or path_length[state] + hanoi_heuristic(state, num_discs, heuristic_type, PDB) < \
                            path_length[n] + hanoi_heuristic(n, num_discs, heuristic_type, PDB):
                n = state

        if n == None:
            print('Path does not exist!')
            return None
        
        if n.get_state() == goal_state.get_state():
            finalTime = time.time() - startTime
            reconst_path = []
            while parents[n] != n:
                reconst_path.append(n.get_state())
                n = parents[n]
            
            reconst_path.append(initial_state.get_state())

            reconst_path.reverse()

            return reconst_path, finalTime
        
        for m in n.get_neighbours():
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                path_length[m] = path_length[n] + 1

            else:
                if path_length[m] > path_length[n] + 1:
                    path_length[m] = path_length[n] + 1
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)
        
        open_list.remove(n)
        closed_list.add(n)

    print('Path does not exist!')
    return None
