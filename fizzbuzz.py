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