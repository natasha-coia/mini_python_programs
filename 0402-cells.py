"""
Completed: 25.06.20 - 26.06.20
You have a 2-D grid of pixels, each of which may be black (0) or white (1). White pixels that
are connected form a "cell". We define "connected" using neighbourhood, and two are commonly
used in image processing.
A pixel is connected to another pixel if it's in its neighbourhood. E.g. (x-1, y) is connected
to (x, y).
"""


def restore_image(image):           #restores the image back to its original state.
    for y in range(len(image)):
        for x in range(len(image[0])):
            if image[y][x] != 0:
                image[y][x] = 1
    return image


def get_average_cell(image, neighbourhood=8):       #finds the average size of the cells in image.
    cell_sizes = []
    for y in range(len(image)):
        for x in range(len(image[0])):
            if image[y][x] == 1:
                num_pixels = cell_size(image, x, y, neighbourhood)
                cell_sizes.append(num_pixels)
    average = 0
    for size in cell_sizes:
        average += size
    average = average / len(cell_sizes)
    return average


def label_cells(image, neighbourhood=8):        #labels the cells in order of appearance.
    last_num = 2
    for y in range(len(image)):
        for x in range(len(image[0])):
            if image[y][x] == 1:
                new_cell = True
                new_cells = []
                neighbours = [(x, y+1), (x+1, y), (x, y-1), (x-1, y),
                        (x-1, y+1), (x+1, y+1), (x+1, y-1), (x-1, y-1)]
                for i in range(neighbourhood-1):           #allows you to use either 4- or 8-neighbourhood.
                    new_cells.append(neighbours[i])
                for cell in new_cells:              
                    if (0 <= cell[0] < len(image[0]) and 0 <= cell[1] < len(image)
                                    and image[cell[1]][cell[0]] != 0 and image[cell[1]][cell[0]] != 1):
                        new_cell = False                        #if point is in the bounds of the image, and is
                        image[y][x] = image[cell[1]][cell[0]]           # NOT a 1 (has already been labelled).
                        break
                if new_cell:
                    image[y][x] = last_num
                    last_num += 1
    return image


def count_cells(image, neighbourhood=8):        #counts the number of cells in image.
    num_cells = 0
    for y in range(len(image)):
        for x in range(len(image[0])):
            num_pixels = cell_size(image, x, y, neighbourhood)
            if num_pixels != 0:
                num_cells += 1
    return num_cells


def cell_size(image, x, y, neighbourhood=8):        #finds the size of a cell, given the coordinates of a point (if that point isn't a 
    num_pixels = 0                                                                                  #           cell then it returns zero)
    new_cells = []
    neighbours = [(x, y+1), (x+1, y), (x, y-1), (x-1, y),
                (x-1, y+1), (x+1, y+1), (x+1, y-1), (x-1, y-1)]
    if image[y][x] == 1:
        for i in range(neighbourhood):           #allows you to use either 4- or 8-neighbourhood
            new_cells. append(neighbours[i])
        image[y][x] = "x"
        for cell in new_cells:
            if 0 <= cell[0] < len(image[0]) and 0 <= cell[1] < len(image) and image[cell[1]][cell[0]] == 1:
                num_pixels += cell_size(image, cell[0], cell[1], neighbourhood)     #uses recursion to find the number of points in that cell
    else:
        return 0
    return num_pixels + 1


image = [                                       #the image. 0 indicated empty space, 1 indicates a part of a cell.
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1]
]
image = label_cells(image)
print(image)
image = restore_image(image)
print(image)
