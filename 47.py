'''Write a program to find all the numbers divisible by 5 and 7 between the given range using the lambda function.'''

def find_divisible(start, end):
    return list(filter(lambda x: x % 5 == 0 and x % 7 == 0, range(start, end)))

def main():
    start, end = map(int, input("Enter the range: ").split())
    print("All devisible numbers are : ",find_divisible(start, end))

if __name__ == '__main__':
    main()
