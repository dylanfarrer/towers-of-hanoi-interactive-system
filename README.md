# towers-of-hanoi-interactive-system
A system that uses various heuristics to solve the Towers of Hanoi problem (four disk variant).

# Search types:
- Breadth first search
- A* with heuristic -> The number of mispalced disks (admissible, consistent)
- A* with heuristic -> (The size of the largest pile of disks that is not in the goal state (or a partial goal state) * 2) - 1. (admissible, not consistent)
- A* with heuristic -> Max value of (widtrh of largest misplaced disk + number of disks on top of it) (admissible, not consistent)
- A* with heuristic -> Pattern database up to 7 discs.
