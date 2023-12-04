import signal
import time

from .state import State
from .bfs import hanoi_bfs, PDB_bfs
from .a_star import hanoi_a_star

"""
comparators.py

This file holds the functions that are used to compare the
performance of the different search algorithms used in this module. 

comparison() compares the performance of the A* heuristics adn BFS with increasing n.

compare_PDB() compares the performance of the PDB heuristic with increasing n.
"""

def handler(signum, frame):
    """
    Handle a timoute exception. Used to exit methods that are taking too long.
    """
    raise Exception("Timeout")

def comparison():
    """
    Compare the performance of A* and Bfs on the Tower of Hanoi problem. With increasing n (up to 7).
    Prints an ascii table at the end.
    """
    # map of search type to times
    results = {
        'bfs' : [],
        'A*1' : [],
        'A*2' : [],
        'A*3' : [],
    }
    n = 1
    # Initialize the towers
    towers = [[] for _ in range(4)]

    while (True):
        if n == 8:
            break

        # Populate the source tower with discs
        towers[0] = list(range(n, 0, -1))

        # bfs
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(180)
        try:
            start_time_bfs = time.time()
            result = hanoi_bfs(State(towers), State([row for row in towers[::-1]]))
            elapsed_time_bfs = time.time() - start_time_bfs

            if result is not None:
                results['bfs'].append(elapsed_time_bfs)
            else:
                results['bfs'].append('N/A')
        except Exception as e:
            results['bfs'].append('N/A')
        signal.alarm(0)
        
        # A*1
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(180)
        try:
            start_time_A_star_one = time.time()
            result = hanoi_a_star(State(towers), State([row for row in towers[::-1]]), n, 0)
            elapsed_time_A_star_one = time.time() - start_time_A_star_one

            if result is not None:
                results['A*1'].append(elapsed_time_A_star_one)
            else:
                results['A*1'].append('N/A')
        except Exception as e:
            results['A*1'].append('N/A')
        signal.alarm(0)
        
        # A*2
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(180)
        try:
            start_time_A_star_two = time.time()
            result = hanoi_a_star(State(towers), State([row for row in towers[::-1]]), n, 1)
            elapsed_time_A_star_two = time.time() - start_time_A_star_two

            if result is not None:
                results['A*2'].append(elapsed_time_A_star_two)
            else:
                results['A*2'].append('N/A')
        except Exception as e:
            results['A*2'].append('N/A')
        signal.alarm(0)
        
        # A*3
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(180)
        try:
            start_time_A_star_four = time.time()
            result = hanoi_a_star(State(towers), State([row for row in towers[::-1]]), n, 2)
            elapsed_time_A_star_four = time.time() - start_time_A_star_four

            if result is not None:
                results['A*3'].append(elapsed_time_A_star_four)
            else:
                results['A*3'].append('N/A')
        except Exception as e:
            results['A*3'].append('N/A')
        signal.alarm(0)
        
        n += 1
    
    print("\n\n\nTime for each heuristic to run (seconds), with increasing n:\n")
    print('-' * 149)
    print("| ", end="")
    n = 1
    for result in results["bfs"]:
        if result == 'N/A':
            print("n = %d, t > 120" % (n), end=" | ")
        else:
            print("n = %d, t = %1.5f" % (n, result), end=" | ")
        n += 1
    print("BFS")
    print('-' * 149)
    print("| ", end="")
    n = 1
    for result in results["A*1"]:
        if result == 'N/A':
            print("n = %d, t > 120" % (n), end=" | ")
        else:
            print("n = %d, t = %1.5f" % (n, result), end=" | ")
        n += 1
    print("Misplaced disk no.")
    print('-' * 149)
    print("| ", end="")
    n = 1
    for result in results["A*2"]:
        if result == 'N/A':
            print("n = %d, t > 120" % (n), end=" | ")
        else:
            print("n = %d, t = %1.5f" % (n, result), end=" | ")
        n += 1
    print("Largest pile")
    print('-' * 149)
    print("| ", end="")
    n = 1
    for result in results["A*3"]:
        if result == 'N/A':
            print("n = %d, t > 120" % (n), end=" | ")
        else:
            print("n = %d, t = %1.5f" % (n, result), end=" | ")
        n += 1
    print("Max misplaced disk plus pile on it")
    print('-' * 149)
    print()

def compare_PDB():
    """
    Compares the performance of A* serarch with a PDB of 7 discs, with increasing disc sizes.
    """
    n_against_time = {}
    towers = [[] for _ in range(4)]
    towers[0] = list(range(7, 0, -1))
    print("Building Pattern Database...")
    PDB = PDB_bfs(State([row for row in towers[::-1]]))
    
    n = 7
    while(True):

        towers[0] = list(range(n, 0, -1))
        print("Attempting " + str(n) + " discs...")
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(3600)
        try:
            start_time = time.time()
            result = hanoi_a_star(State(towers), State([row for row in towers[::-1]]), n, 4, PDB=PDB)
            elapsed_time = time.time() - start_time

            if result is not None:
                n_against_time[n] = elapsed_time
                signal.alarm(0)
            else:
                signal.alarm(0)
                break
        except Exception as e:
            print(str(e))
            signal.alarm(0)
            break
            
        n += 1

        # should not happen, but sanity check
        if n == 10:
            break

    for disc_number, time_taken in n_against_time.items():
        print("n = %d  t = %1.1f" % (disc_number, time_taken))
    print("\n")
