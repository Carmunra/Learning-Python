
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n * factorial(n - 1)

num = 6;
print("Factorial of", num,"is", factorial(num))