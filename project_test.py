from TestSim import TestSim

def main():
    # Get simulation ready to run.
    s = TestSim()

    # Before we do anything, lets simulate the network off.
    s.runTime(1)

    # Load the the layout of the network.
    s.loadTopo("long_line.topo")

    # Add a noise model to all of the motes.
    s.loadNoise("no_noise.txt")

    # Turn on all of the sensors.
    s.bootAll()

    # Add the main channels. These channels are declared in includes/channels.h
    s.addChannel(s.COMMAND_CHANNEL)
    s.addChannel(s.GENERAL_CHANNEL)

    # Project 1
    s.addChannel(s.FLOODING_CHANNEL)
    s.addChannel(s.NEIGHBOR_CHANNEL)

    # Project 2
    s.addChannel(s.ROUTING_CHANNEL)

    i = 1

    # After sending a ping, simulate a little to prevent collision.
    s.runTime(10)
    s.routeDMP(i)
    s.runTime(10)

    s.runTime(10)
    s.ping(1, 4, "Hello, World1")
    s.runTime(50)

    s.runTime(10)
    s.ping(1, 7, "Hello, World 2")
    s.runTime(50)

    s.runTime(10)
    s.routeDMP(i)
    s.runTime(10)

    s.runTime(10)
    s.ping(1, 13, "Hello, World3")
    s.runTime(50)

    s.runTime(10)
    s.ping(1, 50, "Hello, World4")
    s.runTime(20)

    s.runTime(10)
    s.ping(1, 19, "Hello, World5")
    s.runTime(20)



    for i in s.moteids:
        s.runTime(2)
        s.routeDMP(i)
        s.runTime(2)



if __name__ == '__main__':
    main()