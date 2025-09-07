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
