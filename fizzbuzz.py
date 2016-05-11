# Tyler Hedegard 5/11/2016
# Thinkful.com Python Introduction Lesson 1
# FizzBuzz Assignment

# Note: sorry I couldn't make this on gist.github.com.
# My company isn't allowing that url for one reason or another, so I just added it to github
import sys

if len(sys.argv) == 1:
    n = int(float(input("Enter a number: ")))
else:
    try:
        n = int(float(sys.argv[1]))
    except ValueError:
        n = int(float(input("That is not a valid entry.  Please enter a number: ")))

print("Fizz buzz counting up to {}".format(n))
for i in range(1,n+1):
    if i%3 == 0 and i%5 == 0:
        print("Fizz Buzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)