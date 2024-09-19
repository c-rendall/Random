import time 
from typing import List, Set

list_of_names: List[str] = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Harry', 'Ivy', 'Jack']

set_of_names: Set[str] = set(list_of_names)

# Function to measure lookup time from a list 
def test_list() -> float: 
    start_time = time.time()
    for _ in range(100_000): 
        'Alice' in list_of_names 
        'Zack' in list_of_names   # A non-existent name 
    end_time = time.time()
    return end_time - start_time 

# Function to measure lookup time from a set 
def test_set() -> float: 
    start_time = time.time()
    for _ in range(100_000):
        'Alice' in list_of_names 
        'Zack' in list_of_names  # A non-existent name 
    end_time = time.time()
    return end_time - start_time 

def main() -> None: 
    list_time = test_list()
    set_time = test_set()
    print("Time taken for membership lookup in list:", list_time)
    print("Time taken for membership lookup in set:", set_time)
    print("Set lookup is {} times faster than list lookup.".format(list_time / set_time))
    print("Chase")

if __name__ == '__main__':
    main()