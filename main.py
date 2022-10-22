import sys

from graph import UndirectedGraph

paths = UndirectedGraph()
kandy = 1


def initialize():
    cities = int(input("No of cities: "))
    if cities > 100:
        print("cities must be less than or equal to 100")
        sys.exit(-1)
    roads = int(input("No of roads: "))

    for x in range(roads):
        c1, c2, p = list(map(int, input().split(maxsplit=3)))
        if p <= 1:
            print("P must be greater than 1")
            sys.exit(-1)

        paths.add_edge(c1, c2, p)


def solve():
    path = paths.shortest_path(kandy)[0]
    print(path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialize()
    solve()
