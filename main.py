from pyamaze import maze, agent, COLOR
from astar import *
from greedy import greedy

m = maze(8,8)

m.CreateMaze()
searchPath, fwdPath = astar(m)
gSearchPath, gFwdPath = greedy(m)

a = agent(m, footprints=True, color=COLOR.blue, filled=True)
c = agent(m, footprints=True, color=COLOR.red, shape='square')

# Path tracers for visualization
m.tracePath({a: searchPath}, delay=100)     # traces all cells explored (blue)
m.tracePath({c: fwdPath}, delay=100)        # traces path from initial to goal

print("ASTAR:\nCells explored ", len(searchPath), " cells\n")
print("Greedy Best First Search:\nCells explored ", len(gSearchPath), " cells")

m.run()
