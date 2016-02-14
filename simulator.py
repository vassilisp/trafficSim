
class simulator(object):

    m_gridArea = None

    m_participants = []
    m_executors = []

    m_visualize = None
    def __init__(self, xDimensions=100, yDimension=100, visualize=False):
        self.m_visualize = visualize
        self.m_gridArea = GridArea(xDimension, yDimension)

    def addPerson(self, person):
        person.addAreaDimensions(xDimension, yDimension)
        m_participants.append(person)

    def nextCycle(self):
        """ do next cycle """

        for person in m_participants:
            oldPos = person.getPosition()
            person.nextMove()
            newPos = person.getPosition()

            updateGrid(oldPos, newPos)
            run_endCycleExecutors()
            if self.m_visualize : self.m_gridArea.showGrid()

    def updateGrid(self, oldPos, newPos):
        m_gridArea.reset(oldPos)
        m_gridArea.set(newPos)
        
#----------------------------------------        
    def run_endCycleExecutors(self):
        for executor in m_executors:
            executor.execute()

    def addEndCycleExecutor(self, executor):
        m_executors.append(executor)
#----------------------------------------        

if __name__ == "__main__":
    pass

