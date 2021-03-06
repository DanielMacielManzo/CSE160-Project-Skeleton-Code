from TestSim import TestSim

def main():
    # Get simulation ready to run.
    s = TestSim();

    # Before we do anything, lets simulate the network off.
    s.runTime(1);

    # Load the the layout of the network.
    s.loadTopo("example.topo");

    # Add a noise model to all of the motes.
    s.loadNoise("no_noise.txt");

    # Turn on all of the sensors.
    s.bootAll();

    # Add the main channels. These channels are declared in includes/channels.h
    s.addChannel(s.COMMAND_CHANNEL);
    s.addChannel(s.GENERAL_CHANNEL);
    
    # Project 1
    s.addChannel(s.FLOODING_CHANNEL);
    s.addChannel(s.NEIGHBOR_CHANNEL);

    for i in s.moteids:
        s.runTime(1);
        s.neighborDMP(i);

    # After sending a ping, simulate a little to prevent collision.
    s.runTime(1);
    s.ping(2, 3, "First, Message");
    s.runTime(1);

    s.ping(1, 10, "Hi!, 1");
    s.runTime(1);


    s.runTime(1);
    s.ping(2, 3, "Second, Message");
    s.runTime(1);

    s.ping(1, 10, "Hi!, 2");
    s.runTime(1);




if __name__ == '__main__':
    main()
