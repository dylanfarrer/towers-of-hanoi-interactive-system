
import os

from tower_of_hanoi.state import State
from tower_of_hanoi.a_star import hanoi_a_star
from tower_of_hanoi.comparators import compare_PDB, comparison
from tower_of_hanoi.bfs import hanoi_bfs

"""
main.py

Entry point for module.
"""

def main():
    """
    The main function that runs the Towers of Hanoi program.
    
    This function prompts the user for the type of execution they want to perform:
    - Type 0: Compare A* and Bfs on Towers of Hanoi with increasing tower size n.
    - Type 1: Run an interactive session with A* and Bfs.
    - Type 2: Show the performance of A* using a PDB with 7 discs, with disks increasing from 7.
    """

    print("\n\nCS4960 Final Project - Towers of Hanoi on 4 pillars - ZHAC134\n\n")
    while(True):
        run_type = int(input("\nExecution type:\n"
                                "type '0' ---- For comparison table between A* and Bfs on Towers of Hanoi, with increasing "
                                "tower size n (can take up to 10 mins)\n"
                                "type '1' ---- For interactive session with A* and Bfs\n"
                                "type '2' ---- Show performance of A* using a PDB with 7 discs, with disks increasing from 7."
                                " Finishing when an individual call takes more than 10 mins.\n\n"
                                "Enter a number to pick the execution type.\n\n> "))
        if run_type == 0:
            comparison()

        elif run_type == 1:
            num_discs = int(input("Enter the number of discs.\n\n> "))

            # Initialize the towers
            towers = [[] for _ in range(4)]

            # Populate the source tower with discs
            towers[0] = list(range(num_discs, 0, -1))

            initial_state = State(towers)
            goal_state = State([row for row in towers[::-1]])

            initial_state.print_tower(num_discs)

            search_type = int(input("\nSearch type:\n"
                                    "type '0' ---- A* search\n"
                                    "type '1' ---- Bfs search\n\n"
                                    "Enter a number to pick the search type.\n\n> "))
            result = None
            if search_type == 0:
                heuristic_type = int(input("\nHeuristic type:\n"
                                            "type '0' ---- Number of misplaced disks\n"
                                            "type '1' ---- The size of the largest pile of disks that is not in the goal state\n"
                                            "type '2' ---- Max value of (width of misplaced disk + number of disks on top of it)\n"
                                            "type '3' ---- Using PDB (where max m is 7)\n\n"
                                            "Enter a number to pick the heuristic.\n\n> "))

                result, timeTaken = hanoi_a_star(initial_state, goal_state, num_discs, heuristic_type)

            elif search_type == 1:
                result, timeTaken = hanoi_bfs(initial_state, goal_state)

            if result:
                print("Solution found:\n")
                for state in result:
                    State(state).print_tower(num_discs)
                print("Finished with {} states in the result. Time taken = {} seconds.".format(len(result), timeTaken))
            else:
                print("No solution found.")
        
        elif run_type == 2:
            compare_PDB()

        exit_string = input("press any key to continue. Type 'exit' to exit. Type 'clear' to clear screen.\n\n> ")
        if exit_string.lower() == "exit":
            break
        elif exit_string.lower() == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')

    print("exiting...")

if __name__ == "__main__":
    main()
