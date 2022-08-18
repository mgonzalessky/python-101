# CLICK LIBRARY 

import click

# @click.secho('Executing exercise 7:', fg='blue', nl=False)
@click.command()
@click.option("--number", default=20, help="Position of the number you want to calculate")
@click.option("--fizz", default=3, help="Divisible number to print fizz")
@click.option("--buzz", default=4, help="Divisible number to print buzz")
def parse_fizzbuzz(number, fizz, buzz):
    for num in range(1,number+1):
        if(num % fizz == 0 and num % buzz == 0 ):
            print("fizzbuzz")
        elif(num % fizz == 0):
            print("fizz")
        elif(num % buzz == 0):
            print("buzz")

        else: 
            print(num)

parse_fizzbuzz()

# to execute: python exercise7.py --number=100 --fizz=21 --buzz=11