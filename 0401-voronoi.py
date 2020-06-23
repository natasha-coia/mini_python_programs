"""
Completed: 22.06.20-23.06.20
Voronoi Diagrams
"""

def voronoi_eu(width, height, seeds):      #creates a voroni diagram using Euclidean distance.
    for y in range(height):
        row = ""
        for x in range(width):
            min_length = 0
            for i in range(len(seeds)):
                length = ((x-seeds[i][0])**2 + (y-seeds[i][1])**2)**0.5
                if i==0 or length<min_length:
                    min_length = length
                    min_seed = i
            row = row + str(min_seed)
        print(row)
    return


def voronoi_man(width, height, seeds):      #creates a voroni diagram using Manhattan distance.
    for y in range(height):
        row = ""
        for x in range(width):
            min_length = 0
            for i in range(len(seeds)):
                x_dist = x - seeds[i][0]
                if x_dist < 0:
                    x_dist = -(x_dist)
                y_dist = y - seeds[i][1]
                if y_dist < 0:
                    y_dist = -(y_dist)
                length = x_dist + y_dist
                if i==0 or length<min_length:
                    min_length = length
                    min_seed = i
            row = row + str(min_seed)
        print(row)
    return


def voronoi_grow(width, height, seeds):     #creates a voronoi diagram through growing expanding regions from each seed.
    grid = []
    for i in range(height):
        row = []
        for j in range (width):
            row.append("x")
        grid.append(row)
    seed_num = []
    for i in range(len(seeds)):
        seed_num.append(str(i))
    length = len(seeds)
    i=0     #iteration number
    while length<(width*height):
        x = seeds[i][0]
        y = seeds[i][1]
        new_seeds = [(x,y), (x, y+1), (x+1, y), (x, y-1), (x-1, y), (x-1, y+1), (x+1, y+1), (x+1, y-1), (x-1, y-1)]
        for point in new_seeds:
            if point == (x,y):
                grid[point[1]][point[0]] = seed_num[i]
            elif 0<=point[0]<=(width-1) and 0<=point[1]<=(height-1) and grid[point[1]][point[0]] == "x":
                grid[point[1]][point[0]] = seed_num[i]
                seed_num.append(seed_num[i])
                seeds.append(point)
                length += 1
        i+=1
    return grid


#grid = voronoi_grow(100,100,[(2,14),(65,32),(3,14),(34,67),(89,1),(43,90),(50,50),(32,12),(27,7),(78,2)])
grid = voronoi_grow(8,8,[(2,3), (7, 5), (5, 7)])
for row in grid:
    roww = ""
    for item in row:
        roww = roww + item
    print(roww)