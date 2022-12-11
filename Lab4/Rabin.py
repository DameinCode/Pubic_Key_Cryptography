import math
import random 
primes_to_get_random = open("C:/Users/user/Documents/Semester#7/Public key cryptography/Lab4/primes.txt", "r")
alphabet = " abcdefghijklmnopqrstuvwxyz"


# Write the numerical equivalents by splitting the plaintext: 
def numerical_equivalents(str):
    if(len(str)%2 != 0):
        str += ' '
    equivalent_blocks = {}
    for index in range(0, len(str), 2):
        temp_evaluation = alphabet.find(str[index].lower())*27 + alphabet.find(str[index+1].lower())
        equivalent_blocks[str[index]+str[index+1]] = temp_evaluation
    return equivalent_blocks 

# Encryption:  (m^2 mod n):
def encrypt():
    encrypted_blocks = []
    for i in equivalent_blocks:
        encrypted_blocks.append(pow(equivalent_blocks[i], 2, public_key_n))
    return encrypted_blocks

# Getting coefficients to get literals
# ax2 +  bx + c = 48841
def getCoefficients(num):
    a = 0 
    b = 0 
    c = 0
    for a in range(0, 600, 1): 
        for b in range(0, 27, 1):
            for c in range(0, 27, 1):
                if((a*pow(27,2) + b*27) == num-c):
                    a = a%27
                    b = b%27
                    c = c%27
                    if(a%27 == 0 and a != 0): 
                        a = 27
                    if(b%27 == 0 and b != 0):
                        b = 27
                    if(c%27 == 0 and c != 0): 
                        c = 27
                    return a, b, c
    return -1, -1, -1

# Write the literal equivalents: with len l=3
# Getting blocks of cipher text: (first_literal*27^2 + second_literal*27 + c) = encrypted block using: m^2 mod n  
def getLiteralEquivalent():
    literal_equivalents = []
    for block_num in encrypted_blocks:
        a, b, c = getCoefficients(block_num)
        literal_equivalents.append(alphabet[a].upper()+alphabet[b].upper()+alphabet[c].upper())
    return literal_equivalents


# Getting num quivalents 
def getNumericalEquivalentsOfCipherText():
    numerical_equivalents_ciphertext = []
    for i in literal_equivalents:
        temp = 0
        for inx, j in enumerate(i):
            temp += alphabet.find(j.lower())*(pow(27, 3-inx-1))
        numerical_equivalents_ciphertext.append(temp)
    return numerical_equivalents_ciphertext


# p - 1 = 2^s*t
def generate_s_t(prime):
    for t in range(1, 100, 2):
        for s in range(100):
            if(prime-1 == pow(2, s)*t):
                return t
    return -1


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

# The method
def quadratic_non_residue(n):
    check_squares = {}
    for i in range(1, n): 
    # If they are relatively prime numbers, then g can be the generator of the G (Z/nZ)
        square_root = (i*i)%n
        if(square_root in check_squares):
            check_squares[square_root] += 1 
        else: 
            check_squares[square_root] = 1 
        if (i in check_squares): 
            cnt = 0
        else: 
            check_squares[i] = 0
        
    for i in check_squares:
        if(check_squares[i] == 0):
            return i
    return 3

def squareRootModulo(temp1, a, p):
    square = a
    if(temp1 == 5):
        # p mod 5 == 5
        if(((p-1)//4)%p == 1):
            square = pow(a, (p+3)//8, p) 
        else:
            t = (p-5)//8
            temp = pow(4*a, t, p)
            print(temp)
            square = pow(2*a*temp, 1, p)
    elif(temp1 == 3 or temp1 == 7): 
        # p mod 5 == 3
        square = pow(a, (p+1)//4, p)
    elif(temp1 == 1): 
        # p mod 8 == 1
        t = generate_s_t(p) 
        d = quadratic_non_residue(p)
        A = pow(a, t, p)
        D = pow(d, t, p)
        k = 0
        i = 0
        while(pow(D, -i, p) != A%p): 
            i+=2
            k+=1
        square = pow(a, (t+1)//2)*pow(D, k)
        square %= p
    return square


def decryption():
    block_temp = []
    for block in numerical_equivalents_ciphertext:
        x1 = block%p
        x2 = block%q
        if (x1 != int(math.sqrt(x1))*int(math.sqrt(x1))):
            temp1 = p%8
            if (p%4 == 3 and (temp1 == 3 or temp1== 7)):
                temp1 = 3
            square = squareRootModulo(temp1, x1, p)
            x1 = [square, -square]
        else: 
            x1 = [int(math.sqrt(x1)), -int(math.sqrt(x1))]
        if (x2 != int(math.sqrt(x2))*int(math.sqrt(x2))):
            temp1 = q%8
            if (p%4 == 3 and (temp1 == 3 or temp1 == 7)):
                temp1 = 3
                # print("wrf")
            square = squareRootModulo(temp1, x2, q)
            x2 = [square, -square]
        else: 
            x2 = [int(math.sqrt(x2)), -(int(math.sqrt(x2)))]

        n1 = q 
        n2 = p

        k1 = pow(n1, -1, p)
        k2 = pow(n2, -1, q)

        # print(k1, k2)
        # print(x1, x2)
        temps = []
        for i in x1:
            for j in x2: 
                temps.append((i*n1*k1+(j*n2*k2))%public_key_n)
        
        block_temp.append(temps)
    
    return block_temp
        
def getCoefficients2(num): 
    a = 0
    b = 0
    for a in range(0, 600, 1): 
        for b in range(0, 27, 1): 
            if(a*27 + b == num): 
                return a%27, b
    return -1, -1

def getPlainText():
    plaintext_blocks = []
    for blocks in probable_block_of_texts:
        for temp in blocks:
            # if(temp >= 27*27):
            #     continue
            a, b = getCoefficients2(temp)
            plaintext_blocks.append(alphabet[a].upper()+alphabet[b].upper())
    return plaintext_blocks

def print_results():
    print("--"*60)
    print("Alice's public key: ", public_key_n)
    print("Alice's private key: ", private_key)
    print("Numerical equivalents: ", equivalent_blocks)
    print("--"*60)
    print("Encryption part started...")
    print("Encrypted blocks: ", encrypted_blocks)
    print("Literal encrypted blocks: ", literal_equivalents)
    print("Cipher text sent to Alice: ", ciphertext)
    print("--"*60)
    print("Decrytion part started...")
    print("Numerical equivalents of ciphertext", numerical_equivalents_ciphertext)
    print("Numerical of probable plain texts: ", probable_block_of_texts)

p = random.randint(1, 5611110)
q = random.randint(p, 5611116)

lines = primes_to_get_random.readlines()
p = int(lines[p])
q = int(lines[q])

p = 31
q = 67

private_key = {
    "p": p,
    "q": q
}

# p = 31
# q = 67
public_key_n = p*q # Alice's public key n:

# Message to be encrypted 

message = input("Message: ")

# print(896%p)
equivalent_blocks = numerical_equivalents(message)
encrypted_blocks = encrypt()
literal_equivalents = getLiteralEquivalent()
numerical_equivalents_ciphertext = getNumericalEquivalentsOfCipherText()
ciphertext = "".join(literal_equivalents)
# print(squareRootModulo(1, 158404, 2081))
# print_results()
probable_block_of_texts = decryption()
print(getPlainText())
print_results()
