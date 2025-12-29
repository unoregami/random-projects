# if i is divisible by 3 = Fizz
# if i is divisible by 5 = Buzz
# if i is divivisible by both = FizzBuzz

n = int(input("N: "))

for i in range(1, n+1):
    output = ""
    if i%3 == 0:
        output = "Fizz"
    if i%5 == 0:
        output = output + "Buzz"
    if not output:
        output = i
    
    print(output)