'''Write a program to define a function to find all the unique elements of a list hence to find the unique elements of a given list.'''

def unique(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


list = input("Enter a list of elements: ").split()

print('User inputed list is : ',list)
print('Unique list is : ',unique(list))
