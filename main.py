import sys

from graph import UndirectedGraph, AdjList

paths = UndirectedGraph(AdjList())
kandy = "1"


def initialize():
    cities, roads = list(map(int, input().split(maxsplit=2)))
    if cities > 100:
        print("cities must be less than or equal to 100")
        sys.exit(-1)

    for x in range(roads):
        c1, c2, p = input().split(maxsplit=3)
        p = int(p)
        if p <= 1:
            print("P must be greater than 1")
            sys.exit(-1)

        paths.add_edge(c1, c2, p)

    print()


def solve():
    path, min_size = paths.shortest_path(kandy)

    # printing the path like a string of numbers
    for i in path:
        print(i, end=" ")
    print()

    # calculating the number of trips
    trips = students // min_size
    if students % min_size != 0:
        trips = trips + 1
    # printing the minimum number of trips
    print(trips)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # header
    students = int(input("Enter the number of foreign students: "))
    aiesec = int(input("Enter the number of AIESEC students: "))

    initialize()
    solve()
