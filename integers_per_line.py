#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: December 2020
# this program prints out integers from 1000 to 200 with five integers per line


def main():
    # this program prints out integers from 1000 to 200 with five integers
    # per line
    counter = 0

    # process & output
    for counter in range(1000, 2001):
        if (counter + 1) % 5 == 0:
            print("{0} ".format(counter))
        else:
            print("{0} ".format(counter), end="")


if __name__ == "__main__":
    main()
