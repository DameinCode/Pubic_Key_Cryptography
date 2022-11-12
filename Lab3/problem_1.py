# Miller-Rabin algorithm. It will work for numbers of arbitrary size. 
# Random numbers ? Big ?? 
# Miller–Rabin primality test

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] 

test = open("C:/Users/user/Documents/Semester#7/Public key cryptography/Lab3/test.txt", "r")
answer = open("C:/Users/user/Documents/Semester#7/Public key cryptography/Lab3/ans_doc.txt", "a")

# n = int(input("Enter the number to test: "))

for line in test:
    n = int(line)
    prime = True
    i = 2 
    s = 0

    while((n-1)%i == 0):
        s += 1
        t = (n-1)//i
        i *= 2

    answer.write(str(n))
    answer.write("\n")
    answer.write("s = " + str(s) + "  t = " + str(t) + "  binary = " + str(bin(t)))
    answer.write("\n")

    for k in range(0, 3):
        temp = 0
        i = 1
        is_ok = False
        while(i <= pow(2, s)):    
            check = pow(prime_numbers[k], i*t, n) 
            if((check == 1 and i == 1) or (check == 1 and temp-n == -1)):
                is_ok = True 
                break
            temp = check 
            i *= 2
        if(is_ok == False):
            answer.write("No, it definitely is not prime number")
            answer.write("\n")
            answer.write("--------------------------------------")
            answer.write("\n")
            prime = False
            break 
    if(prime):
        answer.write("Yes, it is probably a prime number!")
        answer.write("\n")
        answer.write("--------------------------------------")
        answer.write("\n")        