for num in range(1,21):
    if(num % 3 == 0 and num % 4 == 0 ):
        print("fizzbuzz")
    elif(num % 3 == 0):
        print("fizz")
    elif(num % 4 == 0):
        print("buzz")

    else:
        print(num)