# Program to generate a random number between 0 and 9

# importing the random module
import random
import math

# file2 = open("C:/Users/user/Documents/Semester#7/Public key cryptography/Lab3/ans_doc.txt", "r")


def generator_random_numbers():
    numbers = open("C:/Users/user/Documents/Semester#7/Public key cryptography/Lab3/test.txt", "a")
    for i in range(1, 10000, 1):
        numbers.write(str(random.randint(1200, 2000000)))
        numbers.write("\n")

def fill_to_test():
    file1 = open("C:/Users/user/Documents/Semester#7/Public key cryptography/Lab3/to_test.txt", "a")
    for line in numbers:
        n = int(line)
        prime = True
        for i in range(2, int(math.sqrt(n)+1), 1):
            if(n%i == 0):
                file1.write("No, it definitely is not prime number")
                file1.write("\n")
                prime = False 
                break
        if(prime):
            file1.write("Yes, it is probably a prime number!")
            file1.write("\n")
        
def compare():
    is_Fine = True
    for i in range(0, len(brute_lines), 1):
        if(brute_lines[i] != miller_lines[i]):
            print(brute_lines[i], end=" ")
            print('------', miller_lines[i])
            print(numbers[i])
            is_fine = False
            print("Algorithm is not working 🥺😭")
    if(is_Fine):
        print("Algorithm works fine! 🎇💻🆒")

with open("C:/Users/user/Documents/Semester#7/Public key cryptography/Lab3/ans_doc.txt") as f:
    only_lines = f.readlines()

only_lines.pop(0)
only_lines.pop(0)
miller_lines = only_lines[0::4]

with open("C:/Users/user/Documents/Semester#7/Public key cryptography/Lab3/to_test.txt") as f:
    brute_lines = f.readlines()

with open("C:/Users/user/Documents/Semester#7/Public key cryptography/Lab3/test.txt") as f:
    numbers = f.readlines()


compare()
# fill_to_test()
# generator_random_numbers()