# string divisible by 3 and 5

n=int(input("ENTER THE NUMBER : "))
result = ""
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        result += "FizzBuzz "
    elif i % 3 == 0:
        result += "Fizz "
    elif i % 5 == 0:
        result += "Buzz "
    else:
        result += str(i) + " "

print(result)
