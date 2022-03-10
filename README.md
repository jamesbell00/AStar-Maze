# AStar Maze
A visual demonstration of the A* algorithm compared with Greedy Best First Search using pyamaze 

Python3 required 

## Details

To visually see the A star algorithm's process, I implemented it on a maze to study how the algorithm works given a set of barriers and walls. After investigating python libraries that would support this type of problem, I came across pyamaze, a library used to create random mazes with other useful functionalities as well. The proposed problem implements A* search but with boundaries in place. The heuristic function is simply the manhattan distance between one cell and the goal cell. Since the maze travels by cell in cell, the real cost from one cell to any other adjacent cell is 1. After implementing the algorithm, I noticed a pattern between greedy best first search and a star. Since the cost from one cell to any adjacent cell is 1, the greedy algorithm would move 1 cell in each open path, given the path was not blocked off. With A* algorithm, however, since the heuristic cost was also taken into consideration, the algorithm did as expected and moved according to the addition of the real cost and the heuristic. Overall, the A* algorithm tended to visit less cells than the greedy algorithm.


Here is the visualization of the search path in blue and the solution path in red for the A* algorithm.

![maze_ex](https://user-images.githubusercontent.com/59170647/157768437-2e110b6f-d30b-4327-a93f-92ac4ea1506a.png)
