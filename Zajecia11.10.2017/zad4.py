alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(alfabet)):
    print(alfabet[i].lower() + alfabet[i].upper() + " "),
print()

skip = input("Co ktora liczbe: ")

i = 0
while (i < len(alfabet)):
    if (i % skip == 0):
        print(alfabet[i].lower() + alfabet[i].upper() + " "),
    i = i + 1




