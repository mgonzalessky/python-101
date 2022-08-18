# FIBONACCI FUNCTION 

import sys 

def calculate_fibonacci(to_position):
    current_position = 2
    fib_numbers = [1,2]
    if to_position < 2:
        return fib_numbers[to_position-1]
    while current_position < to_position:
        fib_numbers.append(fib_numbers[current_position-2]+fib_numbers[current_position-1])
        current_position += 1
    return fib_numbers[to_position-1]
        
to_pos = int(sys.argv[1])
print(calculate_fibonacci(to_pos))