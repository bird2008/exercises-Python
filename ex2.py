a = input("a: ")
b = input("b: ")
nwd = 0
it1 = 0
it2 = 0
c = 0
d = 0

try:
    val = int(a)
    c = int(c) + int(a)
    d = int(d) + int(b)
    while c != d:
        it2 += 1
        if c > d:
            c = c - d
        else:
            d = d - c     
    while int(b) > 0:
        it1 += 1
        r = int(a) % int(b)
        a = b
        b = r
    nwd = a
except ValueError:
    print("Wejście musi być liczbą!")
    quit()

print("NWD = ", int(nwd))
print("L_iteracji (I metoda) = {}".format(it1))
print("L_iteracji (II metoda) = {}".format(it2))
