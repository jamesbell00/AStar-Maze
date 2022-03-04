from queue import PriorityQueue


def h(cell1, cell2):
    (x1, y1) = cell1
    (x2, y2) = cell2

    return abs(x1 - x2) + abs(y1 - y2)


def greedy(m):
    initial = (m.rows, m.cols)

    # initializing max values to gn and 0 to initial node
    for cell in m.grid:
        gn = {cell: float('inf')}
    gn[initial] = 0

    # initializing max values for fn and heuristic for initial node
    fn = {cell: float('inf') for cell in m.grid}
    fn[initial] = h(initial, (1, 1))

    frontier = PriorityQueue()
    frontier.put((h(initial, (1, 1)), h(initial, (1, 1)), initial))

    fwdPath = {}  # forward path ( a reverse of the backwards path)
    aPath = {}  # backwards path from goal to initial
    searchPath = [initial]  # all cells explored

    while not frontier.empty():

        # cell = frontier.get()[2]  # get next cell in queue
        next = frontier.get()
        cell = next[2]
        searchPath.append(cell)  # add to search path

        if cell == (1, 1):  # if cell is goal, break
            break

        for direction in 'ESNW':  # checks if cell hit wall and redirects
            if m.maze_map[cell][direction]:
                if direction == 'E':
                    nextCell = (cell[0], cell[1] + 1)
                if direction == 'W':
                    nextCell = (cell[0], cell[1] - 1)
                if direction == 'N':
                    nextCell = (cell[0] - 1, cell[1])
                if direction == 'S':
                    nextCell = (cell[0] + 1, cell[1])

                tmp_gn = gn[cell] + 1  # add 1 to real cost

                if tmp_gn < fn[nextCell]:  # if new calculated cost less than prev calculated cost, update next cell
                    aPath[nextCell] = cell
                    gn[nextCell] = tmp_gn
                    fn[nextCell] = tmp_gn
                    frontier.put((tmp_gn, h(nextCell, (1, 1)), nextCell))

    cell = (1, 1)  # goal cell
    while cell != initial:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]

    return searchPath, aPath, fwdPath
