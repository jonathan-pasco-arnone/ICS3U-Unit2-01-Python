#!/usr/bin/env python3

# Created by Jonathan Pasco-Arnone
# Created on November
# This program calculates the Area and perimeter of a circle

import math


def main():
    print("This program calculates the area and perimeter of a circle.")
    number_str = input("Please enter a radius measurement: ")
    number = int(number_str)
    print("")
    print("If a circle has a radius of " + number_str + "mm")
    area = math.pi * number**2
    perimeter = 2 * math.pi * number
    print("Then the Area is {:.2f}mm²".format(area))
    print("And the Perimeter is {:.2f}mm".format(perimeter))


if __name__ == "__main__":
    main()
