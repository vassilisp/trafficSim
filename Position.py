class Position(object):

    m_x = None
    m_y = None

    def __init__(self, x, y):
        self.m_x = x
        self.m_y = y
    
    def setX(self, value):
        self.m_x = value

    def setY(self, value):
        self.m_y = value

    def getX(self):
        return self.m_x

    def getY(self):
        return self.m_y

    def addX(self, value):
        m_x += value

    def addY(self, value):
        m_y += value
