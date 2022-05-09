#!/usr/bin/env python3
# Created By: Titwech Wal
# Date: Mat.2.2022

# program that generates the rgb
# colours fro 200-255


def main():
    # initialize the colours
    red = 0
    blue = 0
    green = 0

    # display opening message
    print("Here are RGB colour variations from 0-50:")
    print("")

    # determines the different colour codes
    # displays results to the console
    for blue in range(0, 51, 1):
            print("RGB ({}, {}, {})" .format(red, green, blue))
            if blue == 50:
                print("")
                for green in range(1, 51, 1):
                    blue = 0
                    print("RGB ({}, {}, {})" .format(red, green, blue))
                    if green == 50:
                        print("")
                        for red in range(1, 51, 1):
                            green = 0
                            print("RGB ({}, {}, {})" .format(red, green, blue))


if __name__ == "__main__":
    main()
