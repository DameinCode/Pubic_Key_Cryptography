f = open("generated.txt", "a")

for i in range(90, 10000000, 90):
    f.write(str(i))
    f.write(" ")

f = open("generated.txt", "r")
print(f.read())