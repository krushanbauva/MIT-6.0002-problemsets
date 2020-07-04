###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Krushan Bauva
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    
    cows = {}
    with open(filename) as f:
        for line in f:
            line = line.rstrip("\n")
            x = line.split(",")
            cows[x[0]] = int(x[1])
    return cows



# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    cows_copy = cows.copy()
    trips = []
    while(cows_copy):
        trip = []
        space = limit
        for name,weight in sorted(cows_copy.items(), key=lambda x: x[1], reverse=True):
            if weight <= space:
                trip.append(name)
                space -= weight
                del cows_copy[name]
            if space == 0:
                break
        trips.append(trip)
    return trips



# Problem 3
def valid_trip(trip, cows, limit=10):
    """
    Returns True if the trip is possible i.e. the weights of cows can be carried
    in each individual trip

    Parameters:
        trip - a list of list of names (string)
        cows - a dictionary of name (string), weight (int) pairs
        limit - weight limit of the spaceship (an int)
    """
    
    for individual_trip in trip:
        sum_of_weights = 0
        for i in individual_trip:
            sum_of_weights += cows[i]
        if sum_of_weights > limit:
            return False
    return True



def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    best_trip = []
    min_trips = limit
    names = []
    for i in cows.keys():
        names.append(i)
    for partition in get_partitions(names):
        if valid_trip(partition, cows, limit):
            if len(partition) < min_trips:
                min_trips = len(partition)
                best_trip = partition
    return best_trip



# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    
    cows = load_cows("ps1_cow_data.txt")
    start = time.time()
    trips1 = greedy_cow_transport(cows, 10)
    end1 = time.time()
    trips2 = brute_force_cow_transport(cows, 10)
    end2 = time.time()
    print("For greedy algorithm, time taken =", end1 - start, "s and no. of trips =", len(trips1))
    print("For brute force algorithm, time taken =", end2 - end1, "s and no. of trips =", len(trips2))



if __name__ == '__main__':
    compare_cow_transport_algorithms()