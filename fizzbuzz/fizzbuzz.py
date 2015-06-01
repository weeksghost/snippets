"""Write a program that prints the numbers from 1 to 100.
But for multiples of three print 'Fizz' instead of the number.
For the multiples of five print 'Buzz'.
For numbers which are multiples of both three and five print 'FizzBuzz'."""

from random import randint

def fizzbuzz(num):
  for x in range(1, 101):
    if x % 3 == 0:
        print '%d --> Fizz' % x
    if x % 5 == 0:
        print '%d --> Buzz' % x
    if x % 3 == 0 and x % 5 == 0:
        print '%d --> FizzBuzz' % x


def main():
  fizzbuzz(randint(1, 100))

if __name__ == '__main__':
  main()
