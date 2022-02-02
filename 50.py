'''Write a program to shuffle elements of a list of random numbers between given ranges.'''
import random

def shuffle(lst):
    for i in range(len(lst)):
        j = random.randint(0, len(lst)-1)
        lst[i], lst[j] = lst[j], lst[i]
    return lst

start, end = map(int, input("Enter the start and end range: ").split())
lst = [random.randint(start, end) for i in range(10)]
print("Original list: ", lst)
print("Shuffled list: ", shuffle(lst))
