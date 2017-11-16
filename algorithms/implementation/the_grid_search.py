testcases = int(input())


def is_subgrid(grid, i, j, subgrid):
    current_grid_pos = i
    for subgrid_line in subgrid:
        if not grid[current_grid_pos][j:].startswith(subgrid_line):
            return False
        current_grid_pos += 1
    
    return True


for testcase in range(testcases):
    grid_rows, grid_columns = map(int, input().split())
    grid = []
    
    for i in range(grid_rows):
        grid.append(input())
    
    subgrid_rows, subgrid_columns = map(int, input().split())
    subgrid = []
    
    for i in range(subgrid_rows):
        subgrid.append(input())
    
    found = False
    
    for i in range(grid_rows - subgrid_rows + 1):
        for j in range(grid_columns - subgrid_columns + 1):
            if is_subgrid(grid, i, j, subgrid):
                found = True
                break
        if found:
            break
    
    print('YES' if found else 'NO')
