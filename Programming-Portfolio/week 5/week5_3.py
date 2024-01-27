"""Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.
Hint: Don't overthink this. A good way to find the shortest is just to sort them"""

import sys

def find_shortest_argument(arguments):
    if not arguments:
        return None

    shortest_argument = min(arguments, key=len)
    return shortest_argument

if __name__ == "__main__":
    arguments = sys.argv[1:]

    shortest_argument = find_shortest_argument(arguments)

    if shortest_argument is not None:
        print(f"The shortest argument is: {shortest_argument}")
    else:
        print("No arguments provided.")
