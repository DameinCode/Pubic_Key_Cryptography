# gcd(a, b, c) = gcd(a, gcd(b, c)) = gcd(gcd(a, b), c) = gcd(gcd(a, c), b).
# Thus, Euclid's algorithm, which computes the GCD of two integers, suffices to calculate the GCD of arbitrarily many integers.

# import numbers
import re 
import time 

start_time = time.time() 
def callit():
    which = int(input("""Which algorithm you choose?  
    1. The Euclidean Algorithm 
    2. By substruction algorithm
    3. By searching algorithm
"""))
    mainpart(which)
    

def gcd(num1, num2): 
    if(num1 == 0):
        return num2
    elif(num2 == 0):
        return num1
    if(num1 > num2):
        return gcd(num1%num2, num2)
    return gcd(num1, num2%num1)

def subGCD(num1, num2):

    while num1 != num2:
        while num1 > num2:
            num1 -= num2
        while num2 > num1:
            num2 -= num1

    return num1

def mainpart(which):
    if(which > 3 or which < 1):
        print("\n")
        print("--"*50)
        print("Wrong! Type agian")
        callit()

    # n = int(input("Enter number of elements : "))
    # numbers = list(map(int, input().strip().split()))[:n]
    # temp = []

    readFile = open("generated.txt", "r")
    numbers = (re.split("\s", readFile.read()))
    numbers.pop()
    numbers = [int(i) for i in numbers]

    # print(w)

    if(which == 1):
    # Euclidean algorithm 
        while len(numbers) != 1: 
            numbers.append(gcd(numbers[0], numbers[1]))
            a = numbers.pop(0)        
            b = numbers.pop(0)

        print(numbers[0])
    
    elif(which == 2):
    # Find gcd by substraction 
        while len(numbers) != 1: 
            numbers.append(subGCD(numbers[0], numbers[1]))
            a = numbers.pop(0)        
            b = numbers.pop(0)

        print(numbers[0])
    
    else:   
    # Dumb serching for it 
        numbers = [x for x in numbers if x != 0]
        minNum = sorted(numbers)[0]
        # print(minNum)
        temp = 0
        for i in range(2, minNum+1, 1):
            res = 0
            for j in numbers:
                if (j%i != 0):
                    res = -1
                    break
            
            if (res == 0):
                temp = i

        if (temp == 0):
            print(1)
            print("--- %s seconds ---" % (time.time() - start_time))
            exit(0)

        print(temp)
    

 
callit()
print("--- %s seconds ---" % (time.time() - start_time))