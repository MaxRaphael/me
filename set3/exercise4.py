# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""


import math

# import time


def binary_search(low, high, actual_number):
    
    tries = 0
    guess = 0

    guessDic = {"guess": guess, "tries": tries}
    print("Number Finder algorithm activated...")
    print("range is between {0} and {1}".format((low), (high)))
    print("Actual number: {0}".format(actual_number))
    while guess != actual_number:
        print("range is now  {0} and {1}".format((low), (high)))
        mid = (low + high) / 2
        mid = int(mid)
        if mid == actual_number:
            guess = mid
            tries = tries + 1
            print(guess)
        elif mid > actual_number:
            high = mid 
            tries = tries + 1
            mid = mid - 1
            print(mid)
        else:
            low = mid 
            tries = tries + 1
            mid = mid + 1
            print(mid)
        guess = mid
        guessDic = {"guess": guess, "tries": tries, "actual number": actual_number}    

    return guessDic

if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
