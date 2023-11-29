"""
The State class

This class represents a state in the Towers of Hanoi problem.
The state is held as a 2D list of integers. The first element of 
an internal list is the base disk, then the second is one on top of that etc.
"""
class State:
    def __init__(self, state):
        """
        Initializes a new instance of the class.
        """
        self._state = state
    
    def get_state(self):
        """
        Get the state of the object.
        """
        return self._state

    def __hash__(self):
        """
        Compute the hash value of the object.
        """
        return hash(tuple(tuple(tower) for tower in self._state))

    def __eq__(self, other):
        """
        Compares the current `State` object with another object to check if they are equal.
        """
        if isinstance(other, State):
            return self._state == other.get_state()
        return False

    def print_tower(self, num_discs):
        """
        Prints a tower of discs based on the given number of discs.
        """
        print()
        for level in range(num_discs - 1, -1, -1):
            print("| ", end='')
            for peg in range(4):
                if level < len(self._state[peg]):
                    disc_value = self._state[peg][level]

                    # print disc value
                    print(" " + str(disc_value) + " ", end='')

                    # print peg separator
                    if peg < 3:
                        print(" | ", end='')
                else:
                    # print empty peg
                    print("   ", end='')

                    # print peg separator
                    if peg < 3:
                        print(" | ", end='')
            print(" |")

        # print base of towers
        print(' ' + ('-' * 23))
        print()

    def get_neighbours(self):
        """
        Generates a list of neighboring states based on the current state.
        """
        neighbours = []

        for source in range(4):
            for target in range(4):
                if source != target and self._state[source]:
                    if not self._state[target] or self._state[target][-1] > self._state[source][-1]:
                        new_state = [list(peg) for peg in self._state]
                        disk = new_state[source].pop()
                        new_state[target].append(disk)
                        neighbours.append(State(new_state))

        return neighbours
