from trafficSim import Simulator
import initializers

class TrafficSim(object):

    m_cycles = None
    def __init__(self):
        simulator = Simulator()

    def start(self):
        for i in xrange(m_cycles):
            simulator.nextCycle()
            

    def setDuration(simMinutes=0, cycles=1):
        self.m_cycles = cycles


if __name__ == "__main__":
    trafficSim = TrafficSim()
    trafficSim.setDuration(cycles=10)
    trafficSim.start()
