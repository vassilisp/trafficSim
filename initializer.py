from trafficSim import Simulator, GridArea

class Initializer(object):

    m_cycles = None
    m_persons = []

    m_area = None

    m_name = "defaultInitializer"

    def __init__(self):
        pass


    def getInitializerName(self):
        return self.m_name

    def getPersons(self):
        return self.m_persons
    
    def getDuration(self):
        return m_cycles

    def getArea(self):
        return m_area

#----------------------------------------
# methods to build the initializer

    def initiliazerName(self, name):
        self.m_name = name
    def defineDuration(self, cycles):
        self.m_cycles = cycles

    def addPerson(self, person):
        self.m_persons.append(person)

    def addPersons(self, persons):
        self.m_persons.extend(persons)

    def defineArea(self, xDimension, yDimension):
        self.m_area = GridArea(xDimension, yDimension)
#----------------------------------------
