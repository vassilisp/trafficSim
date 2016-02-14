import matplotlib.pyplot as plt
import numpy as np

class GridArea(object):

    m_grid = None

    def __init__(self, xDimension, yDimension):
        self.m_grid  = [[0 for y in xrange(yDimension)] for x in range(xDimension)] 


    def updateGrid(self, oldPos, newPos):
        gridReset(oldPos)
        gridSet(newPos)

    def gridReset(self, position):
        x = position.getX()
        y = position.getY()
        self.m_grid[x][y] = 0

    def gridSet(self, position):
        x = position.getX()
        y = position.getY()
        self.m_grid[x][y] = 1

    def toConsole(self):
        """ m[x][y] 
            len(m) for x
            len(m[0]) for y"""
        
        for row in m:
            print row

    def showGrid():
        #tmp = np.array(self.m_grid)
        plt.imshow(self.m_grid, interpolations = "nearest")
        plt.show(block="false")
