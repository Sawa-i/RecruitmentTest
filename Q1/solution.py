## Add code below with answer clearly stated
def factorial(x):
    fact = 1
    while(x>1):
        fact*=x
        x-=1
    return fact

def sumDigits(x):
    sum = 0
    while x!=0:
        sum+=x%10
        x=x//10
    return sum


if __name__ == "__main__":
    print("\t{ Question 1 : Sum of Factorial's Digits }\n") 
    n = int(input("Enter n : "))

    fact = factorial(n)
    
    summ = sumDigits(fact)
    
    print("Sum of Digits of Factorial of {} => {}".format(n,summ))
    
