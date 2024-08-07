import sys
from pipeline_sim import MIPSSimulator

'''
Pipeline main loop (not finished)
'''

# Pipeline simulator without hazard handling
def runSimulator(sim):
    while (1):
        sim.tick()
        print(hex(sim.pc.currentAddress()))
        value = sim.dataMemory.memory[sim.pc.currentAddress()]

        # Print register and memory if
        # break instruction is being executed
        if value == 13:
            sim.printRegisterFile()
            sim.printDataMemory()
            print("Code Ran Successfully!")
            exit()

if __name__ == '__main__':
    assert(len(sys.argv) == 2), 'Usage: python %s memoryFile' % (sys.argv[0],)
    memoryFile = sys.argv[1]

    simulator = MIPSSimulator(memoryFile)
    runSimulator(simulator)
    print(sim.nCycles)
    exit()
