class Person(object):

    m_position = None

    def __init__(self, position):
        try:
            self.m_position = position
        except:
            print "initialize Person with position type"
            print "using default position of (0,0)"
            self.m_position = Position(0,0)

    def nextMove(self):
        #TODO change this to something meaningful
        self.m_position += +1

    def canMove(self, position):
        insideXLimits = (position.getX <= self.maxX) and (position.getX>= 0)
        insideYLimits = (position.getY <= self.maxY) and (position.getY >= 0)
        if insideXLimits and insideYLimits:
            return True
        else:
            return False

    def addAreaDimensions(self, x, y):
        self.maxX = x
        self.maxY = y
        
    def getPosition(self):
        return self.m_position


