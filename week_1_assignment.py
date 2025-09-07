"""
    Week 1 Assignment
    Sachin Karki
    Satish Penmatsa
    2025 Fall - Algorithms and Data Structures (MSCS-532-M80) - Full Term
    University of the Cumberland – Kentucky
"""

def insert_number():
    numbers_list = []
    while True:
        print("Enter a random number or press 0 to finish adding numbers: ")
        random_int = int(input())

        if random_int == 0:
            break

        numbers_list = numbers_list + [random_int]

    return numbers_list

def insertion_sort(numbers_list):

    for i in range(1, len(numbers_list)):
        key = numbers_list[i]
        j = i - 1

        # Move all the elements smaller than key to the right side.
        while j >= 0 and numbers_list[j] < key:
            numbers_list[j + 1] = numbers_list[j]
            j -= 1

        numbers_list[j + 1] = key

    return numbers_list


numbers = insert_number()
output = insertion_sort(numbers)
print(output)
