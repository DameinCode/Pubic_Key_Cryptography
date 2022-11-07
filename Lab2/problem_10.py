# Algorithm for determining all generators of the cyclic group (Zn, +), where n ≥ 2 is a natural
# number. A generator of (Zn, +) is an element ˆg ∈ Zn such that for every ˆx ∈ Zn there exists
# k ∈ {0, 1, . . . , n − 1} such that ˆx = kgˆ.

n = int(input()) 

def gcd(num1, num2): 
    if(num1 == 0):
        return num2
    elif(num2 == 0):
        return num1
    if(num1 > num2):
        return gcd(num1%num2, num2)
    return gcd(num1, num2%num1)

# algorithm to find a generators
# <g> = {gk : k ∈ Z}


# for i in range(1, n): 
#     # If they are relatively prime numbers, then g can be the generator of the G (Z/nZ)
#     if(gcd(i, n) == 1): 
#         print("Generator of the cyclic group: ", i)
#         temp = 1
#         print("Subgroup: {", end = " ")
#         while(temp*i%n != 0):
#             print(temp*i%n, end = " ")
#             temp += 1
#         print(0, "}")


# for i in range(1, n): 
#     temp = 1
#     liist = set()
#     while(temp*i%n != 0):
#         liist.add(temp*i%n)
#         temp += 1

#     if(len(liist) == n-1):
#         print("Generator: ", i)

