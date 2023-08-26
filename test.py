# optimize the code below
# 
# import pygame
# import numpy as numpy
# 
# colorAboutToDie = (200, 200, 225)
# colorAlive = (255, 255, 215)
# colorBackground = (10, 10, 40)
# colorGrid = (30, 30, 60)
# 
# def updateGrid(surface, currentGrid, sizeOfCell):
#     nextGrid = numpy.zeros((currentGrid.shape[0], currentGrid.shape[1]))
# 
#     for row, column in numpy.ndindex(currentGrid.shape):
#         numberOfAliveCells = numpy.sum(currentGrid[row - 1:row + 2, column - 1:column + 2]) - currentGrid[row, column]
#         if currentGrid[row, column] == 1 and numberOfAliveCells < 2 or numberOfAliveCells > 3:
#             color = colorAboutToDie
#         elif (currentGrid[row, column] == 0 and numberOfAliveCells == 3) or (currentGrid[row, column] == 1 and 2 <= numberOfAliveCells <= 3):
#             nextGrid[row, column] = 1
#             color = colorAlive
#         color = color if currentGrid[row, column] == 1 else colorBackground
#         pygame.draw.rect(surface, color, (column * sizeOfCell, row * sizeOfCell, sizeOfCell - 1, sizeOfCell - 1))
#     
#     return nextGrid
# 
# def gridInitialize(dimensionOfX, dimensionOfY):
#     cells = numpy.zeros((dimensionOfX, dimensionOfY))
# 
#     # make a numpy p

import pygame
import numpy as numpy

colorAboutToDie = (200, 200, 225)
colorAlive = (255, 255, 215)
colorBackground = (10, 10, 40)
colorGrid = (30, 30, 60)

def updateGrid(surface, currentGrid, sizeOfCell):
    nextGrid = numpy.zeros((currentGrid.shape[0], currentGrid.shape[1]))

    for row, column in numpy.ndindex(currentGrid.shape):
        numberOfAliveCells = numpy.sum(currentGrid[row - 1:row + 2, column - 1:column + 2]) - currentGrid[row, column]
        if currentGrid[row, column] == 1 and numberOfAliveCells < 2 or numberOfAliveCells > 3:
            color = colorAboutToDie
        elif (currentGrid[row, column] == 0 and numberOfAliveCells == 3) or (currentGrid[row, column] == 1 and 2 <= numberOfAliveCells <= 3):
            nextGrid[row, column] = 1
            color = colorAlive
        color = color if currentGrid[row, column] == 1 else colorBackground
        pygame.draw.rect(surface, color, (column * sizeOfCell, row * sizeOfCell, sizeOfCell - 1, sizeOfCell - 1))
    
    return nextGrid

def gridInitialize(dimensionOfX, dimensionOfY):
    cells = numpy.zeros((dimensionOfX, dimensionOfY))

    # make a numpy pattern for an  oscilator in game of life
    pattern = numpy.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);
    position = (3, 3)
    cells[position[0]:position[0] + pattern.shape[0], position[1]:position[1] + pattern.shape[1]] = pattern
    return cells
    
def main(dimensionOfX, dismensionOfY, sizeOfCell):
    pygame.init()
    surface = pygame.display.set_mode((dimensionOfX * sizeOfCell, dismensionOfY * sizeOfCell))
    pygame.display.set_caption("Game of Life")

    cells = gridInitialize(dimensionOfX, dismensionOfY)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(colorGrid)
        cells = updateGrid(surface, cells, sizeOfCell)
        pygame.display.update()

if __name__ == "__main__":
    main(120, 90, 8)
    



