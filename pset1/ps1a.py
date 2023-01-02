###########################
# 6.0002 Problem Set 1a: Space Cows
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

# ================================
# Part A: Transporting Space Cows
# ================================

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
    cow_dict = {}
    with open(filename, "r") as content:
        content = content.readlines()
        for line in content:
            line = line.split(",")
            cow_dict[line[0]] = line[1].replace(
                "\n", ""
            )  ## assigning cow name to weight in cow_dict
    return cow_dict


# Problem 2
def greedy_cow_transport(cows, limit=10):
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
    current_limit = limit
    trips_content = []
    trip = []
    copy_cows = dict(sorted(cows.items(), key=lambda item: item[1], reverse=True))

    while len(copy_cows) > 0:
        for cow_name, cow_weight in copy_cows.items():
            if int(cow_weight) <= current_limit:
                current_limit -= int(cow_weight)
                trip.append(cow_name)
        for name in trip:
            del copy_cows[name]
        trips_content.append(trip)
        trip = []
        current_limit = limit

    return trips_content


# Problem 3
def brute_force_cow_transport(cows, limit=10):
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
    best_brute_force_list = []
    current_best = len(list(cows.values()))
    for partition in get_partitions(list(cows.keys())):
        for elem_num, list_partition in enumerate(partition):
            sum_of_list = 0
            for cow_in_list in list_partition:
                sum_of_list += int(cows[cow_in_list])
                if sum_of_list > limit:
                    break

            if sum_of_list <= limit and len(partition) < current_best:
                if elem_num == len(partition) - 1:
                    best_brute_force_list = partition
                    current_best = len(best_brute_force_list)
            else:
                break
    return best_brute_force_list


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
    start = time.time()
    greedy_cow_transport(load_cows("Programming Lessons/MIT 6.0002/ps1_cow_data.txt"))
    print(time.time() - start)
    print(
        greedy_cow_transport(
            load_cows("Programming Lessons/MIT 6.0002/ps1_cow_data.txt")
        )
    )
    start = time.time()
    brute_force_cow_transport(
        load_cows("Programming Lessons/MIT 6.0002/ps1_cow_data.txt")
    )
    print(time.time() - start)
    print(
        brute_force_cow_transport(
            load_cows("Programming Lessons/MIT 6.0002/ps1_cow_data.txt")
        )
    )


dict_cows = load_cows("Programming Lessons/MIT 6.0002/ps1_cow_data.txt")
# greedy_cow_transport(dict_cows)
brute_force_cow_transport(dict_cows)
# debug = 1
compare_cow_transport_algorithms()
