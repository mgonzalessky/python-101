import sys 


def parse_fizzbuzz(to_number, fizz_dividable, buzz_dividable):
    for num in range(1,to_number+1):
        if(num % fizz_dividable == 0 and num % buzz_dividable == 0 ):
            print("fizzbuzz")
        elif(num % fizz_dividable == 0):
            print("fizz")
        elif(num % buzz_dividable == 0):
            print("buzz")

        else: 
            print(num)


to_number = int(sys.argv[1])
fizz_dividable = int(sys.argv[2])
buzz_dividable = int(sys.argv[3])
parse_fizzbuzz(to_number, fizz_dividable, buzz_dividable)

# Executions: 
# python exercise5.py 42 6 7